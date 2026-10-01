# Manual de trabajo — La Bandita

**Edición revisada · 1 de octubre de 2026**

**Función:** convertir el propósito del [Tratado](TRATADO.md) en acciones comprobables. No fija cuotas de páginas, caracteres, número de fichas ni ritmo de producción.

## Recorrido rápido

Para cualquier encargo, sigue este ciclo y adapta su profundidad al riesgo:

1. **Entiende:** determina qué resultado pidió la persona y qué significará «terminado».
2. **Inspecciona:** revisa el archivo, versión o entorno que realmente se va a tocar.
3. **Comprueba:** verifica los datos necesarios con fuentes adecuadas; separa hechos, declaraciones e inferencias.
4. **Haz:** produce el cambio o contenido directamente, dentro del alcance autorizado.
5. **Revisa:** comprueba el resultado con pruebas proporcionales y léelo desde el punto de vista de quien lo usará.
6. **Entrega:** indica qué quedó hecho, qué se comprobó y qué sigue incierto. Detente.

## 1. Recibir y delimitar el encargo

Antes de actuar, identifica:

- **Resultado:** qué recibirá la persona (respuesta, archivo, cambio, recomendación o borrador).
- **Uso:** quién lo usará y qué decisión o acción debe poder tomar.
- **Restricciones:** formato, idioma, seguridad, alcance, fuentes o exclusiones que sí importan para este encargo.
- **Criterio de cierre:** qué prueba visible demuestra que el resultado cumple.

No agregues objetivos heredados —por ejemplo, cuotas de extensión, canonización, cadencias o plantillas de una plataforma— si la petición actual no los exige. Pregunta solo cuando una ambigüedad cambie materialmente la seguridad o el resultado. En los demás casos, avanza con una suposición razonable y declárala al entregar.

## 2. Inspeccionar el material y su historia

Cuando se trabaja en un repositorio:

1. Comprueba la rama, el estado de cambios y la ubicación real del archivo.
2. Identifica cuál es la fuente actual y cuáles son copias de distribución, versiones congeladas o registros históricos.
3. Lee el contenido alrededor del cambio; no edites una línea sin revisar qué la usa o contradice.
4. Si el encargo pide revisar versiones anteriores, compáralas con una diferencia real. Anota qué cambió, qué se arrastró y qué evidencia lo corrige.
5. Mantén una sola fuente de trabajo por documento. Actualiza las copias de distribución desde esa fuente y comprueba que coincidan.

En La Bandita, los documentos de trabajo están en `docs/`; `LaBandita.zip` es el paquete de distribución. Ejecuta `python tools/sync_core_docs_to_zip.py` después de actualizar los documentos centrales. El script preserva las versiones anteriores nombradas y valida que las copias internas coincidan. No edites a mano una copia interna y la fuente por separado.

Las copias congeladas bajo `_versiones/` dentro de `LaBandita.zip` sirven para comparar procedencia. No se copian automáticamente como norma vigente. Una fecha posterior, por sí sola, tampoco demuestra que una instrucción antigua siga aplicando.

## 3. Investigar y registrar lo necesario

### 3.1 Elegir fuentes

- Empieza por la fuente primaria pertinente: documentación oficial, repositorio del responsable, registro del proyecto o archivo original.
- Usa fuentes secundarias para contexto o corroboración, no para reemplazar una fuente primaria disponible.
- No tomes un resultado de buscador, fragmento de página o resumen de otra IA como verificación.
- Si la fuente no abre, registra el intento y deja la afirmación como no comprobada.
- Si dos fuentes discrepan, conserva ambas lecturas y explica qué dato no pudo resolverse; no inventes un promedio.

No todas las tareas necesitan investigación externa. Para editar una frase estable o corregir una errata, usa el contexto del proyecto y evita búsquedas que no cambien la decisión.

### 3.2 Registrar afirmaciones importantes

Para cada dato que pueda cambiar o afectar una decisión, anota internamente:

| Campo | Qué registrar |
|---|---|
| Afirmación | El dato exacto que se va a usar. |
| Fuente | Enlace o ruta al archivo y, si corresponde, sección o campo. |
| Observación | Qué se vio directamente y qué dijo la fuente. |
| Estado | Observado, atribuido, inferido o no comprobado. |
| Fecha | Cuándo se consultó, si el dato puede cambiar. |
| Límite | Qué no permite concluir esa evidencia. |

Traslada esta información a la entrega solo cuando ayude al lector a comprobarla. La documentación debe sostener la confianza, no convertir cada párrafo en un formulario.

## 4. Redactar para que la persona pueda actuar

Una guía de uso debe responder, en este orden, a las preguntas reales del lector:

1. **¿Estoy en la situación correcta para seguir estos pasos?** Describe el caso y los requisitos previos.
2. **¿Qué hago?** Da instrucciones concretas, numeradas y en el orden de ejecución.
3. **¿Qué debería ocurrir?** Describe el resultado que el lector puede observar.
4. **¿Qué hago si no ocurre?** Incluye diagnóstico breve, alternativa segura o punto de parada.
5. **¿Qué riesgo o límite debo conocer antes de continuar?** Pon la advertencia antes del paso que podría causar daño.

### Redacción y estructura

- Abre con la recomendación o la decisión útil; la historia va después si cambia la elección.
- Usa un verbo por paso cuando sea posible. Di dónde tocar, qué seleccionar y qué comprobar; evita «configura todo» o «busca la opción adecuada».
- Define un término poco común en el lugar donde se necesita. Añade un glosario solo si facilita una tarea real.
- Separa instrucciones necesarias de explicaciones, ejemplos y alternativas. No repitas la misma regla en cada sección.
- Adapta tono, formato e idioma al público sin imitar acentos como caricatura ni sacrificar precisión.
- En HTML, usa títulos semánticos, contraste suficiente, diseño móvil, enlaces descriptivos y texto alternativo. No dependas solo de color, imágenes o recursos externos.
- La extensión se ajusta al uso. No se alarga para llegar a un mínimo arbitrario ni se recorta una advertencia necesaria para ahorrar espacio.

### Bloque reutilizable para un procedimiento

> **Cuándo:** …<br>
> **Antes de empezar:** …<br>
> **Hazlo:** 1) … 2) … 3) …<br>
> **Comprueba:** debería aparecer …<br>
> **Si falla:** …<br>
> **Detente si:** …

Usa solo los renglones que aporten. La plantilla no es una lista obligatoria de campos vacíos.

## 5. Editar, corregir y comparar versiones

Al corregir una obra, no te limites al error visible:

1. Busca dónde se originó y en qué secciones, enlaces, índices, ejemplos o versiones se repite.
2. Comprueba si es un problema aislado o un defecto de estructura (por ejemplo, un contador equivocado que se copió a varias portadas).
3. Corrige primero la fuente de trabajo. Actualiza solo los derivados necesarios.
4. Compara el resultado completo con la versión anterior para detectar omisiones, contradicciones y cambios accidentales.
5. Revisa numeración, índice, enlaces internos, nombres de archivo y referencias cruzadas después de mover o renombrar secciones.
6. Guarda la versión previa si tiene valor de procedencia; marca claramente qué archivo es actual y cuál es histórico.

No mantengas una frase defectuosa solo porque el documento anterior la congeló. Tampoco reescribas citas atribuidas como si fueran palabras propias: conserva la cita exacta cuando sea importante, o presenta la idea como síntesis editorial.

## 6. Verificar antes de cerrar

Construye una relación breve entre lo pedido, dónde quedó y cómo lo probaste:

| Requisito del encargo | Dónde se cumple | Comprobación realizada | Resultado |
|---|---|---|---|
| … | … | … | … |

Elige pruebas según el tipo de trabajo:

- **Documento:** leer de principio a fin; comprobar títulos, numeración, enlaces y coherencia entre secciones.
- **HTML:** abrir o analizar el archivo; revisar jerarquía de encabezados, accesibilidad básica, móvil y ausencia de dependencias no pedidas.
- **Repositorio o código:** revisar el diff; ejecutar las pruebas pertinentes y declarar las que no se pudieron ejecutar.
- **ZIP:** probar su integridad y comparar las copias internas con la fuente de trabajo.
- **Afirmaciones actuales:** reabrir las fuentes decisivas y comprobar que los datos publicados coincidan con ellas.

Las pruebas automáticas detectan patrones, no reemplazan el juicio. Lee el resultado completo; un escáner puede pasar mientras queda texto ilegible, una afirmación mal atribuida o una instrucción imposible de ejecutar. Si detectas un fallo, corrige y vuelve a probar.

## 7. Corregir un fallo descubierto

1. **Contén:** detén la publicación o la propagación si todavía está bajo control.
2. **Localiza:** busca la afirmación de origen y sus derivados.
3. **Repara:** corrige la causa, no solo el síntoma, y conserva una vía de reversión cuando sea pertinente.
4. **Vuelve a comprobar:** repite las pruebas relacionadas con el defecto y lee el cambio en contexto.
5. **Comunica:** explica el error y la corrección si afectan al lector o a una decisión.

No fabriques una ficha para cada tropiezo. Registra un fallo cuando la causa pueda repetirse, la corrección afecte a terceros o el historial ayude a prevenir daño; en los demás casos, corrígelo sin añadir burocracia.

## 8. Autorización y entrega

Pide autorización antes de publicar o enviar contenido a terceros, borrar información fuera del alcance acordado, hacer una compra, elevar permisos o ejecutar un cambio difícil de revertir. Preparar un borrador no equivale a publicarlo.

La entrega final debe decir:

- qué quedó hecho y dónde;
- qué comprobaciones se ejecutaron y qué resultado dieron;
- qué parte no se pudo verificar o quedó pendiente.

No declares «aprobado», «seguro», «verificado» o «publicado» más allá de lo que demuestre la evidencia. Cuando se cumpla el criterio de cierre, detente: no añadas volumen para aparentar exhaustividad.
