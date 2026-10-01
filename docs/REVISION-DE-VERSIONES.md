# Revisión editorial de versiones anteriores

**Fecha de revisión: 1 de octubre de 2026**

**Alcance:** Tratado, Manual, Canon-Cimiento, Lecciones de Alexis y sus copias principales dentro de `LaBandita.zip`.

Esta revisión no intenta hacer crecer el archivo ni certificar que el texto anterior fuese correcto. Compara las versiones congeladas con las activas, identifica problemas heredados y explica qué se consolidó en esta edición. Las copias históricas se conservan; no son instrucciones vigentes por el mero hecho de seguir dentro del ZIP.

## Hallazgos por documento

### Tratado: V.0.05 y V.0.04

- La comparación literal encontró que casi todas las líneas extensas de la edición activa V.0.05 ya estaban en V.0.04. Los cambios principales eran portada, índice y tres erratas más, no una reconstrucción integral del cuerpo.
- El cuerpo activo mezclaba capas históricas (U, H, D, F, G y V19), módulos propuestos, recursos y matrices de 180 celdas. La edición presentaba ese material como un único tratado operativo, aunque contenía textos de épocas y estados distintos.
- La misma fórmula de «adaptación por nivel de IA» y la misma verificación aparecían repetidas a través de las 180 celdas. La repetición demostraba cobertura, pero dificultaba encontrar la decisión que correspondía a una tarea real.
- El Libro 7 mantenía artículos en un orden no secuencial (N-701, N-702, N-703, N-706, N-704, N-705) y varias capas conservaban sus propios índices y glosarios.

**Decisión editorial:** consolidar propósito, alcance, precedencia, principios, evidencia, autorización y corrección en una sola edición breve. Las capas anteriores quedan como antecedentes en `_versiones/`; no se reproducen dentro del cuerpo activo.

### Manual: V2.1 y V1

- La comparación literal encontró que V2.1 conservaba casi todo el cuerpo largo de V1 y añadía, sobre todo, una sección editorial dominicana y un registro de cambios.
- El Manual integraba a la vez procedimientos, checklists y las 75 fichas de fallos. El mismo catálogo aparecía también en el Tratado y en `MANUAL-FICHAS-FALLOS.md`.
- La sección añadida heredó requisitos fechados de longitud, anatomía de publicaciones y formato por plataforma. Esos requisitos se mezclaban con operaciones reutilizables y podían seguir pareciendo obligatorios aun cuando el encargo cambiara.
- La estructura saltaba de las secciones 1–4 a la 6; el propio historial tuvo que aclarar que no faltaba una sección 5. La edición revisada elimina esa numeración heredada.

**Decisión editorial:** el Manual nuevo se centra en el flujo de trabajo, la investigación, la redacción accionable, la revisión de versiones, las pruebas y la entrega. El catálogo de fallos permanece separado como consulta; no hay que recorrerlo completo para terminar una tarea.

### Lecciones de Alexis: V.22 y copia del 20 de septiembre

- V.22 agregó cuatro entradas del 22 de septiembre y actualizó índice, temas y referencias; la mayoría de las lecciones anteriores quedó igual.
- La tabla de conexión remitía a una sección `§5.4.8` que el registro posterior ya señalaba como no definida en el corpus. Las nuevas lecciones evitan depender de ese número y enlazan por nombre de documento.
- Varias entradas mezclaban palabras de Alexis, interpretaciones editoriales y frases atribuidas a canciones u obras ajenas. Esa mezcla podía hacer difícil distinguir una cita literal de una síntesis.
- Los ejemplos de versiones, conteos y plataformas describían situaciones fechadas, no datos actuales.

**Decisión editorial:** conservar las enseñanzas duraderas, fechar su origen, separar cita de interpretación y convertir cada una en una práctica comprobable. Los ejemplos fechados no se reutilizan como hechos actuales.

### Canon-Cimiento V28-sep

- Reunía 12 pilares, 8 operaciones y una puerta de aceptación; tenía la intención valiosa de traducir doctrina a trabajo diario.
- La misma página acumulaba estados de septiembre, dos bandas de caracteres distintas, una revisión futura, pausa de publicaciones y reglas de «append-only». Esos estados ya no describen el encargo actual.
- Algunos controles eran cuantificables pero no medían utilidad para el lector; por ejemplo, el tamaño del documento o el número de elementos presentes.

**Decisión editorial:** mantener una página visual autocontenida como mapa de acción, retirar la puerta por tamaño y dejar solo controles que indiquen qué hacer y cómo comprobarlo. La versión V28-sep queda como referencia histórica fechada.

## Integridad del corpus y duplicaciones

`ARCHIVO-1`, `ARCHIVO-2` y `ARCHIVO-4` repetían el Tratado, el Manual y las Lecciones con volúmenes agregados; las fuentes y los volúmenes fechados correspondientes ya existen por separado en el ZIP. Mantener cuatro copias largas creaba riesgo de divergencia. En la nueva estructura, esos tres nombres remiten a la fuente actual; los bytes de cada compilación anterior se preservan en `_versiones/ARCHIVO-1-CODIGO-DE-REGLAS-congelado-2026-10-01.md`, `_versiones/ARCHIVO-2-MANUAL-DE-USO-congelado-2026-10-01.md` y `_versiones/ARCHIVO-4-LECCIONES-DE-ALEXIS-congelado-2026-10-01.md`.

La revisión también encontró que el índice y la prosa de algunos documentos no coincidían con sus referencias cruzadas. La sincronización actualiza las fuentes del paquete desde los archivos de trabajo y comprueba que sean idénticas, en vez de corregir dos copias a mano.

## Qué queda vigente y qué queda como historia

- **Fuentes de trabajo en el repositorio:** `docs/TRATADO.md`, `docs/MANUAL-COMPLETO.md`, `docs/CANON-CIMIENTO.html` y `docs/LECCIONES-ALEXIS.md`.
- **Copias vigentes en el paquete:** `00-CANON/TRATADO.md`, `00-CANON/MANUAL-COMPLETO.md`, `00-CANON/CANON-CIMIENTO.html` y `00-CANON/LECCIONES-ALEXIS.md` dentro de `LaBandita.zip`.
- **Guía breve para ejecutar:** `GUIA-DE-ACCION.md` en el repositorio y su copia en `00-CANON/CUATRO-ARCHIVOS/ARCHIVO-3-GUIA-DE-ACCION.md` dentro del ZIP.
- **Referencia opcional del ZIP:** `00-CANON/MANUAL-FICHAS-FALLOS.md`; se consulta cuando ayuda a resolver un fallo concreto, no como tarea que haya que completar.
- **Antecedentes dentro del ZIP:** los documentos de `_versiones/` y las bitácoras fechadas de `02-ARCHIVO/`.

No se fija una cuota de extensión, una fecha automática de «canonización» ni un porcentaje de perfección. La revisión termina cuando cada documento cumple su función, sus referencias coinciden y las pruebas pertinentes pasan.
