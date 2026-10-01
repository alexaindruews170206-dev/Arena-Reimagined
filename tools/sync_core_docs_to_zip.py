#!/usr/bin/env python3
"""Synchronize La Bandita's maintained documents into the distribution ZIP.

The Markdown/HTML files under docs/ are the working sources. Before replacing
older active ZIP entries, preserve their exact bytes under _versiones/ once.
The script does not remove or rewrite unrelated archive members.
"""

from __future__ import annotations

import argparse
import copy
import os
import stat
import sys
import tempfile
import zipfile
from collections import Counter
from pathlib import Path
from typing import Dict, Iterable, List, NoReturn, Tuple

ROOT = Path(__file__).resolve().parents[1]
ARCHIVE = ROOT / "LaBandita.zip"

SOURCE_MAP = {
    "docs/TRATADO.md": "00-CANON/TRATADO.md",
    "docs/MANUAL-COMPLETO.md": "00-CANON/MANUAL-COMPLETO.md",
    "docs/CANON-CIMIENTO.html": "00-CANON/CANON-CIMIENTO.html",
    "docs/LECCIONES-ALEXIS.md": "00-CANON/LECCIONES-ALEXIS.md",
    "docs/REVISION-DE-VERSIONES.md": "00-CANON/REVISION-DE-VERSIONES.md",
    "docs/INICIO-PAQUETE.md": "00-CANON/INICIO-PAQUETE.md",
    "GUIA-DE-ACCION.md": "00-CANON/CUATRO-ARCHIVOS/ARCHIVO-3-GUIA-DE-ACCION.md",
}

# Preserve the exact pre-edit bytes of active/duplicated entries. Existing
# snapshots are never overwritten by a later run.
SNAPSHOT_MAP = {
    "00-CANON/TRATADO.md": "_versiones/TRATADO-V005-congelada-2026-09-22.md",
    "00-CANON/MANUAL-COMPLETO.md": "_versiones/MANUAL-V2.1-congelado-2026-09-22.md",
    "00-CANON/LECCIONES-ALEXIS.md": "_versiones/LECCIONES-ALEXIS-V22-congelada-2026-09-22.md",
    "00-CANON/CUATRO-ARCHIVOS/ARCHIVO-1-CODIGO-DE-REGLAS.md": (
        "_versiones/ARCHIVO-1-CODIGO-DE-REGLAS-congelado-2026-10-01.md"
    ),
    "00-CANON/CUATRO-ARCHIVOS/ARCHIVO-2-MANUAL-DE-USO.md": (
        "_versiones/ARCHIVO-2-MANUAL-DE-USO-congelado-2026-10-01.md"
    ),
    "00-CANON/CUATRO-ARCHIVOS/ARCHIVO-4-LECCIONES-DE-ALEXIS.md": (
        "_versiones/ARCHIVO-4-LECCIONES-DE-ALEXIS-congelado-2026-10-01.md"
    ),
}

LEGACY_POINTERS = {
    "00-CANON/CUATRO-ARCHIVOS/ARCHIVO-1-CODIGO-DE-REGLAS.md": (
        "# Archivo 1 — referencia histórica\n\n"
        "La fuente de trabajo vigente es [`TRATADO.md`](../TRATADO.md). "
        "Este archivo antes contenía una compilación extensa de reglas; se conserva "
        "sin cambios en [`_versiones/ARCHIVO-1-CODIGO-DE-REGLAS-congelado-2026-10-01.md`](../../_versiones/ARCHIVO-1-CODIGO-DE-REGLAS-congelado-2026-10-01.md).\n\n"
        "Los volúmenes históricos de Archivo 1 permanecen en `volumenes/`. "
        "No uses el snapshot como norma vigente si contradice la petición actual "
        "o el Tratado revisado.\n"
    ),
    "00-CANON/CUATRO-ARCHIVOS/ARCHIVO-2-MANUAL-DE-USO.md": (
        "# Archivo 2 — referencia histórica\n\n"
        "La fuente de trabajo vigente es [`MANUAL-COMPLETO.md`](../MANUAL-COMPLETO.md). "
        "Este archivo antes contenía un manual compilado; se conserva sin cambios en "
        "[`_versiones/ARCHIVO-2-MANUAL-DE-USO-congelado-2026-10-01.md`](../../_versiones/ARCHIVO-2-MANUAL-DE-USO-congelado-2026-10-01.md).\n\n"
        "Los volúmenes históricos de Archivo 2 permanecen en `volumenes/`. "
        "No uses el snapshot como norma vigente si contradice la petición actual "
        "o el Manual revisado.\n"
    ),
    "00-CANON/CUATRO-ARCHIVOS/ARCHIVO-4-LECCIONES-DE-ALEXIS.md": (
        "# Archivo 4 — referencia histórica\n\n"
        "La fuente de trabajo vigente es [`LECCIONES-ALEXIS.md`](../LECCIONES-ALEXIS.md). "
        "Este archivo antes repetía lecciones y ejemplos; se conserva sin cambios en "
        "[`_versiones/ARCHIVO-4-LECCIONES-DE-ALEXIS-congelado-2026-10-01.md`](../../_versiones/ARCHIVO-4-LECCIONES-DE-ALEXIS-congelado-2026-10-01.md).\n\n"
        "Los volúmenes históricos de Archivo 4 permanecen en `volumenes/`. "
        "No uses el snapshot como norma vigente si contradice la petición actual "
        "o las Lecciones revisadas.\n"
    ),
}


def fail(message: str) -> NoReturn:
    print(f"ERROR: {message}", file=sys.stderr)
    raise SystemExit(1)


def read_sources() -> Dict[str, bytes]:
    result: Dict[str, bytes] = {}
    for source, destination in SOURCE_MAP.items():
        path = ROOT / source
        if not path.is_file():
            fail(f"falta la fuente de trabajo: {source}")
        result[destination] = path.read_bytes()
    for destination, text in LEGACY_POINTERS.items():
        result[destination] = text.encode("utf-8")
    return result


def load_archive() -> Tuple[List[zipfile.ZipInfo], Dict[str, bytes], bytes]:
    if not ARCHIVE.is_file():
        fail(f"no existe el paquete: {ARCHIVE.relative_to(ROOT)}")
    try:
        with zipfile.ZipFile(ARCHIVE, "r") as archive:
            infos = archive.infolist()
            names = [info.filename for info in infos]
            duplicates = [name for name, count in Counter(names).items() if count > 1]
            if duplicates:
                fail("el ZIP contiene nombres duplicados: " + ", ".join(duplicates[:5]))
            bad_member = archive.testzip()
            if bad_member is not None:
                fail(f"el ZIP de entrada está dañado; primer miembro inválido: {bad_member}")
            contents = {info.filename: archive.read(info) for info in infos}
            return infos, contents, archive.comment
    except (OSError, zipfile.BadZipFile, RuntimeError) as exc:
        fail(f"no se pudo leer el ZIP: {exc}")


def expected_updates(current: Dict[str, bytes], source_data: Dict[str, bytes]) -> Dict[str, bytes]:
    updates = dict(source_data)
    for old_path, snapshot_path in SNAPSHOT_MAP.items():
        if snapshot_path in current:
            # A snapshot is immutable after its first creation.
            continue
        if old_path not in current:
            fail(f"no se puede preservar {old_path}: la entrada no está en el ZIP")
        updates[snapshot_path] = current[old_path]
    return updates


def describe_differences(current: Dict[str, bytes], updates: Dict[str, bytes]) -> List[str]:
    return [name for name, data in updates.items() if current.get(name) != data]


def check_archive(current: Dict[str, bytes], updates: Dict[str, bytes]) -> int:
    differences = describe_differences(current, updates)
    if differences:
        print("Necesita sincronización:")
        for name in differences:
            print(f"  - {name}")
        print("Ejecuta: python tools/sync_core_docs_to_zip.py")
        return 1
    print(
        "OK: el ZIP está íntegro; las fuentes vigentes, las referencias heredadas "
        "y los snapshots configurados coinciden."
    )
    return 0


def make_zip(
    infos: Iterable[zipfile.ZipInfo],
    old_data: Dict[str, bytes],
    updates: Dict[str, bytes],
    archive_comment: bytes,
) -> None:
    pending = set(updates)
    original_mode = stat.S_IMODE(ARCHIVE.stat().st_mode)
    fd, temp_name = tempfile.mkstemp(
        prefix=f".{ARCHIVE.name}.", suffix=".tmp", dir=ARCHIVE.parent
    )
    os.close(fd)
    try:
        with zipfile.ZipFile(temp_name, "w", allowZip64=True) as output:
            output.comment = archive_comment
            # Keep existing order and metadata. Replace matching entries in
            # place; leave every unrelated entry's bytes and path untouched.
            for info in infos:
                name = info.filename
                if name in pending:
                    replacement_info = copy.copy(info)
                    output.writestr(replacement_info, updates[name])
                    pending.remove(name)
                else:
                    output.writestr(copy.copy(info), old_data[name])
            # New canonical files and first-run snapshots are appended.
            for name in sorted(pending):
                output.writestr(name, updates[name], compress_type=zipfile.ZIP_STORED)
        with zipfile.ZipFile(temp_name, "r") as verify:
            bad_member = verify.testzip()
            if bad_member is not None:
                fail(f"el ZIP reconstruido no pasó integridad: {bad_member}")
            for name, expected in updates.items():
                if verify.read(name) != expected:
                    fail(f"falló la comprobación posterior de {name}")
        os.chmod(temp_name, original_mode)
        os.replace(temp_name, ARCHIVE)
    except BaseException:
        try:
            os.unlink(temp_name)
        except FileNotFoundError:
            pass
        raise


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--check",
        action="store_true",
        help="solo comprueba integridad y coincidencia; no cambia el ZIP",
    )
    args = parser.parse_args()

    infos, current, archive_comment = load_archive()
    updates = expected_updates(current, read_sources())
    differences = describe_differences(current, updates)
    if args.check:
        return check_archive(current, updates)
    if not differences:
        print("Sin cambios: el ZIP ya coincide con las fuentes vigentes.")
        return check_archive(current, updates)

    make_zip(infos, current, updates, archive_comment)
    print("Sincronización completada:")
    for name in differences:
        print(f"  - {name}")
    _, refreshed, _ = load_archive()
    return check_archive(refreshed, expected_updates(refreshed, read_sources()))


if __name__ == "__main__":
    raise SystemExit(main())
