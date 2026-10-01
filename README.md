# La Bandita

Este repositorio organiza el trabajo editorial en dos capas: las **fuentes vigentes** están en `docs/`, y [`LaBandita.zip`](LaBandita.zip) es el paquete de distribución con sus antecedentes y materiales relacionados.

## Punto de entrada

Empieza por la [Guía de acción](GUIA-DE-ACCION.md) para trabajar en una tarea concreta. Para la edición central revisada, consulta:

- [`docs/TRATADO.md`](docs/TRATADO.md) — propósito, principios y límites.
- [`docs/MANUAL-COMPLETO.md`](docs/MANUAL-COMPLETO.md) — procedimiento y controles de calidad.
- [`docs/CANON-CIMIENTO.html`](docs/CANON-CIMIENTO.html) — mapa visual e imprimible de acción.
- [`docs/LECCIONES-ALEXIS.md`](docs/LECCIONES-ALEXIS.md) — enseñanzas atribuidas, contexto y aplicación práctica.
- [`docs/REVISION-DE-VERSIONES.md`](docs/REVISION-DE-VERSIONES.md) — auditoría comparativa y decisiones editoriales.
- [`docs/INICIO-PAQUETE.md`](docs/INICIO-PAQUETE.md) — orientación para quien abre el ZIP.

## Fuente y distribución

Edita primero los archivos de `docs/`. Después de cambiar un documento central, ejecuta:

```sh
python tools/sync_core_docs_to_zip.py
python tools/sync_core_docs_to_zip.py --check
```

El sincronizador guarda dentro de `_versiones/` las copias activas anteriores antes de reemplazarlas, actualiza el ZIP desde las fuentes y comprueba que las copias coincidan. No edites por separado las copias internas.

## Alcance y estado

La revisión actual reorganiza el Tratado, el Manual, el Canon-Cimiento y las Lecciones de Alexis. Las demás publicaciones y referencias del paquete **no quedan certificadas como actuales** por esta revisión; comprueba de nuevo cualquier dato cambiante antes de reutilizarlo. Las versiones congeladas sirven para rastrear la historia, no para imponerse a la petición actual.

No se persigue canonización como objetivo separado, ni cuotas de caracteres, palabras o tamaño de archivo. También quedan retiradas las metas antiguas del 27 de septiembre de 2,5 millones de caracteres por archivo y 10 millones en conjunto. La extensión se ajusta al uso y a los requisitos reales del encargo.
