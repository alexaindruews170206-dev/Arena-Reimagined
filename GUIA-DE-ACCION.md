# Guía de acción — La Bandita

**Actualizada: 1 de octubre de 2026.** Esta guía sirve para hacer el trabajo, no para aumentar el corpus.

## Para qué trabajar

Entregar el resultado útil, correcto y comprobable que pidió la persona. No se persigue que un archivo sea «canónico», que el proyecto alcance una cantidad de caracteres ni que cada tarea produzca más documentación. Las metas del 27 de septiembre de **2,5 millones por archivo y 10 millones en conjunto quedan retiradas**. Las antiguas bandas de extensión tampoco se heredan automáticamente: solo se mide una extensión si la tarea actual o un límite técnico real lo exige. Nunca se rellena para llegar a una cifra.

## Qué instrucción manda

1. Respeta primero los límites de seguridad, permisos y alcance de la sesión.
2. Dentro de esos límites, sigue la petición explícita más reciente de la persona.
3. Aplica solo los requisitos de formato o plataforma necesarios para esa tarea.
4. Usa los documentos fechados anteriores como contexto, no como órdenes vigentes cuando contradigan la petición actual.

Si una duda impide hacer la tarea de forma segura o correcta, pregunta una sola cosa concreta. Si no la impide, avanza con una suposición razonable y declárala al entregar.

## Procedimiento: entender, hacer, comprobar

### 1. Define el resultado antes de editar

Escribe para ti una línea con el entregable y otra con la condición observable de finalización:

- **Entregable:** qué archivo, respuesta o cambio recibirá la persona.
- **Terminado cuando:** qué debe poder hacer, ver o comprobar gracias a ese resultado.

No conviertas la petición en una meta de expansión, reorganización o canonización que la persona no haya pedido.

### 2. Mira lo necesario, no todo por inercia

- Comprueba la rama, el estado del repositorio y el archivo concreto que vas a tocar.
- Para el Tratado, el Manual, el Canon-Cimiento y las Lecciones de Alexis, trabaja desde `docs/`; `LaBandita.zip` es una copia de distribución. Usa `docs/REVISION-DE-VERSIONES.md` para entender el alcance de la edición y las copias bajo `_versiones/` dentro del ZIP como antecedentes, no como órdenes activas.
- Lee la instrucción actual y solo el contexto relacionado con esa tarea. Si la persona pide revisar GitHub, mira el repositorio pertinente; no supongas que una copia vieja refleja el estado actual.
- Para datos que cambian —versiones, licencias, responsables, enlaces o compatibilidad— consulta la fuente primaria disponible y apunta cuándo la revisaste.
- Separa lo verificado de lo inferido. Si no pudiste comprobar un dato, dilo; no lo completes de memoria.

### 3. Escribe para que alguien pueda actuar

Una guía práctica debe permitir que el lector avance sin descifrar un catálogo de términos. Cuando corresponda, organiza cada procedimiento así:

1. **Situación:** cuándo usarlo.
2. **Acción:** pasos concretos, en orden y con verbos directos.
3. **Resultado esperado:** qué debería aparecer o cambiar.
4. **Si no funciona:** cómo comprobar la causa y qué alternativa segura tomar.
5. **Parada o riesgo:** cuándo no continuar y a quién consultar.

Empieza por la decisión o el paso que le sirve al lector. Añade definiciones, historia, fichas o contexto solo cuando ayuden a ejecutar ese paso. No uses un glosario ni una lista de fallos como sustituto de instrucciones.

### 4. Haz el cambio completo y acotado

- Modifica el archivo real y limita el cambio a lo necesario para satisfacer la petición.
- No añadas por defecto un apéndice, una taxonomía, otro manual ni texto para aparentar exhaustividad.
- Si cambias un documento central, edita su fuente en `docs/` y ejecuta `python tools/sync_core_docs_to_zip.py`; luego `python tools/sync_core_docs_to_zip.py --check` para comprobar que el paquete coincide y es íntegro.
- No publiques, borres ni muevas material fuera del repositorio sin autorización expresa.

### 5. Comprueba tu propio trabajo

Antes de decir «listo», enlaza cada requisito de la petición con el resultado y una prueba concreta. Según el cambio, revisa el diff, abre el archivo final, ejecuta las pruebas, comprueba enlaces o valida el ZIP. Luego lee el texto completo como si fueras la persona que necesita usarlo: ¿puede seguir los pasos y saber si funcionaron?

Una comprobación automática no sustituye la lectura. En la auditoría de FB 10 del 30 de septiembre, el escaneo por sí solo no mostró el problema; la lectura encontró 48 tramos de texto ininteligible. La regla práctica es sencilla: **automatiza lo que se pueda, lee el resultado y corrige antes de cerrar**.

No afirmes que verificaste, ejecutaste, publicaste o corregiste algo si no hay un resultado real que lo demuestre. Si una prueba falla, repara y vuelve a probar; si no puedes resolverla, explica exactamente qué queda pendiente.

### 6. Entrega y detente

Al cerrar, informa en pocas líneas:

- qué resultado quedó hecho y en qué archivo;
- qué comprobaste y qué resultado dio;
- qué dato o parte sigue incierto, si corresponde.

La tarea termina cuando cumple la petición y sus comprobaciones, no cuando el documento llega a cierto tamaño. No sigas expandiendo después de alcanzar el resultado útil.

## Comprobación rápida

- [ ] Respondí a la petición actual, no a una meta vieja.
- [ ] Los pasos que propongo se pueden ejecutar y tienen un resultado observable.
- [ ] Revisé el artefacto final y corrí las comprobaciones pertinentes.
- [ ] No rellené, no inventé verificación y no hice acciones externas sin permiso.
- [ ] Informé con honestidad qué quedó hecho y qué no.
