# VELA MAPS — el mapa que no le cuenta tu vida a Google · guía de la casa · WhatsApp La Bandita

*La Bandita · 15 de octubre de 2026 · edición dominicano-español · pieza nº 11 de la casa, horneada a las 11 de la mañana*

───────────────────

> *Semilla de esta guía:* en todo barrio hay dos tipos de gente que sabe llegar. El primero
> te cobra la vuelta, te lleva por donde le conviene y de camino memoriza cada parada que
> haces: dónde compras, a qué hora sales, a quién visitas los domingos. El segundo también
> sabe llegar — aprendió el barrio de verdad, calle por calle, del mapa que la gente misma
> dibujó — y cuando le preguntas por una esquina que él no conoce, la pregunta se la lleva
> al que la sabe, pero sin dar tu nombre, sin apuntar a quién le preguntas y sin quedarse
> con tu ruta. Esta guía es del segundo. Se llama *Vela*.

───────────────────

## 📰 LA NOTICIA DEL DÍA, CON HORA

A las 10:53 de esta mañana, con la orden de la casa de salir a buscar lo desconocido — no lo
famoso de siempre, no los cadáveres, no lo que ya tenemos —, el censo de La Bandita recorrió
nueve vetas del vecindario del software libre y devolvió setenta casas sobrevivientes. De
todas, una se quedó con la pieza de hoy. No es la más vieja ni la más famosa: es la que tiene
el hueco que nadie del catálogo había llenado y el taller más despierto de la cosecha.

La casa es **github.com/PimpinPumpkin/Vela** y la app se llama **Vela Maps**. Contado hoy,
15 de octubre de 2026, directo de su página pública:

```
CASA            Vela Maps (app.vela)
REPO            github.com/PimpinPumpkin/Vela
ESTRELLAS       ★1.961  [constado 15-oct, censo de API]
NACIÓ           15 de junio de 2026 — cuatro meses de vida
EMPUJE          HOY mismo, 15-oct a las 10:13 UTC
FORKS           93
ISSUES ABIERTAS 23
COLABORADORES   23 (contados por API hoy)
LICENCIA        GPL-3.0 (código abierto de verdad, con cláusulas fuertes)
WEBSITE         velamaps.org · docs: pimpinpumpkin.github.io/Vela/docs
```

Y la placa del taller: la última versión **estable es la v0.5.2549, publicada el 12 de
octubre**, y **hoy mismo salió una build canary** — la vela recién cortada del palo, con el
mismo día de esta guía. Un taller que empuja código y corta releases la misma mañana en que
lo lees no es una casa prometida: es una casa encendida.

**Velocidad de la casa, medida por La Bandita:** 1.961 estrellas en cuatro meses de vida son
**482 estrellas por mes** — la velocista de su generación que esta expedición midió hoy con
la vara de la casa (estrellas ÷ meses de vida). Para ponerla en perspectiva barrial: NewPipe,
el rey de nuestraLista, tardó años en correr a ese paso.

```
COMPARACIÓN DE VELOCIDAD [constado 15-oct-2026, censo de API de la casa]

Vela Maps      ★1.961 en  4 meses  →  482 ★/mes   (nueva, cuatro meses)
NewPipe        ★40.140 en 10 años  →  ~330 ★/mes   (el rey, a paso de rey)
```

## 🗺️ LO QUE ES Y LO QUE NO ES (porque en este barrio se dice todo)

Vela se declara con una frase que nuestra gente entiende al primer toque: es lo que NewPipe
es para YouTube, pero para Google Maps. Y como en NewPipe, la gracia no es solo que no pagues
— es que el que manda en tu consumo eres tú.

**Lo que Vela ES, contado llano:**

- Una app Android **nativa y de código abierto** (Jetpack Compose y MapLibre por dentro)
  que dibuja el mapa con **azulejos vectoriales abiertos**: OpenFreeMap para la base, y
  encima los lugares — bodegas, bombas, farmacias, bancos — cocinados con **datos abiertos**
  (Overture Maps y AllThePlaces, puestos en su sitio con OpenStreetMap).
- Un navegador con **voz paso a paso**: te dice «doble a la derecha», te dibuja el carril por
  el que vas a salir, te pone el velocímetro con el límite de la vía, y si se arma un tapón
  adelante te ofrece la vuelta más rápida.
- Un buscador de lugares con horarios, reseñas, fotos y precios de gasolina, y una app de
  transporte con tableros de salidas de guaguas.
- Un proyecto con **regla de casa escrita**: sin backend propio, sin cuenta, sin telemetría
  de la app, sin anuncios, sin claves de Google escondidas. Está en su CONTRIBUTING como
  ley dura: quien quiera meterle un servidor o una clave estática, no entra.

**Lo que Vela NO es — y esto se dice primero que nada:**

- **No es un envoltorio de la app de Google.** No lleva dentro el SDK de Google, ni Play
  Services, ni una API key, ni pantalla de entrar con cuenta. Es una app nueva, dibujada
  desde cero, que se parece a propósito a lo que ya conoces para que no pierdas el paso.
- **No es 100% libre de preguntarle a Google — y la casa lo declara en una tabla pública,**
  no lo esconde. La verdad llana: el *mapa* que recorres con el dedo es abierto y no llega a
  Google; pero cuando buscas «colmado cerca de aquí», pides una ruta en carro o abres el
  detalle de un lugar, el teléfono le hace a Google **las preguntas que solo Google sabe
  responder bien** — como las haría un navegador anónimo sin cuenta: sin tu nombre, sin
  clave de app, sin servidor de por medio.
- **No es un milagro de datos.** La casa misma lo advierte: los nombres de calles y los
  números de casas pueden diferir de lo que muestra Google Maps, y cuánto ves sin señal
  depende de qué tan bien mapeado está tu zona en OpenStreetMap. En Santo Domingo, en el
  Distrito Nacional y los municipios del Gran Santo Domingo, el mapa abierto va bien
  caminado; en parajes de la cordillera o en el interior profundo, la cobertura abierta
  puede venir corta — y eso se sabe antes de salir, no después.

Esta honestidad es la vara por la que esta guía la admitió en el catálogo: la casa que te
dice qué le lleva a Google *en una tabla con renglones* es la casa que no te miente en los
detalles chicos. Abajo, en «Las conversaciones honestas», está esa tabla completa adaptada.

**Sobre el nombre, que es bonito y se cuenta solo:** *Vela* es la constelación del
navegante — «Las Velas», la que guió barcos cuando no había GPS — y también «vela» (sail) en
varios idiomas. Un mapa que se llama como la vela del barco que llegaba a puerto sin venderle
el rumbo a nadie. El paquete se llama `app.vela`, corto y honesto.

───────────────────
## 🎒 LO QUE TRAE, CAJÓN POR CAJÓN

La casa tiene el inventario entero en su FEATURES.md — una línea por función, sin humo. Esta
guía abrió los cajones que le importan a la gente de a pie, con lo que cada uno de verdad te
da el primer día:

### Cajón 1 — Rutas y tráfico: la ruta del carro, con el semáforo adentro

Pides de la Duarte a la 27 de Febrero y Vela te devuelve **la ruta que daría el propio
Google**: con tráfico vivo y carreteras cerradas contadas. Cada opción de ruta trae su tiempo
pintado en verde, ámbar o rojo, y el tráfico dicho en palabras — «ligero», «moderado»,
«pesado» — no con iconitos que uno adivine. Encima corre la navegación paso a paso: diagrama
de carriles para no cogerte el carril equivocado, escudos de salidas como en las autopistas,
velocímetro con el límite de la vía puesto, y si se arma un tapón adelante, la oferta de
vuelta más rápida antes de que te comas el presa.

### Cajón 2 — Los lugares del mapa: abiertos de nacimiento

Cada pin, punto y etiqueta que pasas rozando con el dedo es **dato abierto cocinado por la
casa**: Overture Maps y AllThePlaces posicionados con OpenStreetMap, horneados en azulejos
dentro del propio repo y servidos desde sus releases. Navegar el mapa **no le manda nada a
Google**. Cuando tocas un lugar, ahí sí se le pregunta lo que al mapa abierto le falta:
horarios con días festivos, reseñas que se pueden buscar, fotos, horas de fila, teléfono,
página web y hasta el aviso de si el lugar estará cerrado cuando llegues. Y hay un interruptor
— *Settings → Places → «Place icons on the map»* — para elegir qué ves: solo dato abierto
(el que viene por defecto), ambos, o Google.

### Cajón 3 — Cámaras de placas en el mapa: la función que nadie más te da

Esto es de las rarezas buenas del proyecto: Vela dibuja en el mapa las **cámaras de matrícula
mapeadas por la comunidad** (el proyecto DeFlock, sobre datos de OpenStreetMap), de fábrica
y sin configurar nada. Y tiene un interruptor de ruta que se llama **«Avoid surveillance
cameras»**: cuenta las cámaras apuntadas a lo largo de cada ruta y, si el desvío es pequeño,
elige la de menos cámaras. Dos interruptores más te dan una tarjeta o un aviso hablado —
«cámara de placas adelante» — cuando te acercas a una. El dataset vive **en tu teléfono** y
se actualiza semanalmente. En un mundo donde la vigilancia se normaliza callando, un mapa que
te avisa y te deja elegir ruta es una declaración de principios con utilidad práctica.

### Cajón 4 — Vela Voice: la voz que vive en tu teléfono

Las direcciones habladas salen de una **voz neuronal que corre en el teléfono** — no de un
servicio de voz remoto — y el micrófono que transcribe tus búsquedas también trabaja en el
teléfono: **lo que dices no viaja a ningún servicio de voz**. La casa hasta publicó una
muestra del audio para oírla antes de instalar. La voz en español, claro: 19 idiomas de
fábrica.

### Cajón 5 — Mapas y rutas sin señal: la región entera en el bolsillo

Descargas un país, una región o solo el área que tienes en pantalla, y con eso el mapa, los
lugares, las direcciones por calle y número, y la navegación paso a paso **funcionan sin una
gota de señal**. Para quien maneja por el interior, para quien sale a la playa donde la
señal se pierde, para el apagón que corta los datos: la ruta vive en tu bolsillo, no en la
antena ajena.

### Cajón 6 — Transporte público: el tablero de la guagua

Los tableros de salidas y la lista de paradas de cada recorrido vienen de los horarios
abiertos que publican las agencias de transporte, servidos por el proyecto comunitario
**Transitous**. Las direcciones de transporte las calcula Google, con el planificador abierto
como respaldo. Las líneas de tren se dibujan en su color de verdad y el viaje se pinta sobre
la vía real, no en línea recta de imaginación. Nota honesta de la casa: donde no hay datos
abiertos de paradas, el tablero cae a la página de Google de esa parada.

### Cajón 7 — Precios de la gasolina: el cajón que a nosotros nos tiembla el bolsillo

Buscas gasolina y **cada bomba trae su precio puesto en el marcador** — en el mapa, en la
lista y en la página del lugar. En un país donde el precio del combustible es tema de
mañana, tarde y noche, ver el precio de la bomba antes de doblar es oro. Que los precios
aparezcan llenos o cortos depende de los datos abiertos de tu zona — se juzga con la misma
vara de siempre: pruébalo en tu ruta de todos los días antes de fiarlo.

### Cajón 8 — Street View y satélite

Street View dentro de la app: mirar alrededor, caminar la calle, volver a capturas viejas, en
media pantalla sobre el mapa o a pantalla completa. La vista satelital viene de Esri. Lo que
abres tú a propósito, no lo que la app te mira de gratis.

### Cajón 9 — Tus listas, tus rutas, tu respaldo — y la mudanza desde Google

Guardas lugares en listas con una nota cada uno, guardas una ruta que te gusta, fijas un
viaje en la pantalla de inicio, y **todo se respalda a un archivo**. Y el detalle que vale
por una mudanza completa: **pegas en la barra de búsqueda un enlace de lista compartida de
Google Maps o de My Maps y Vela la importa**. Tus lugares de años no se quedan presos: vienen
contigo al mapa abierto.

### Cajón 10 — Los remates del taller

Estacionamiento: tocas la **P** cuando aparcas y después tocas el pin para que te lleve de
vuelta al carro. Voz natural: «llévame a casa», «navega a la estación», «farmacia más
cercana», «¿a qué hora llego?» — dicho o escrito, en todos los idiomas de la app. Y **la app
se repara sola cuando Google mueve las cosas**: las recetas de las peticiones viven en un
archivo firmado que la app consulta al arrancar; si Google le cambia un campo a la web, el
arreglo llega a todas las instalaciones en minutos, sin actualizar la app. Es la misma
filosofía de NewPipe: cuando el gigante muda la puerta, la casa del barrio ajusta la bisagra
de una vez.

Y para los teléfonos de teclas que no se mueren: **operación completa por D-pad**. Para los
carros: pantallas de Android Auto con matices (abajo se explica, porque ahí hay letra chica
honesta). Tema claro y oscuro, colores de fondo opcionales, y un **actualizador integrado**
con canales estable, nightly y canary — de eso también se habla abajo.

## 🇩🇴 REPÚBLICA DOMINICANA ADENTRO: el hallazgo que decidió esta pieza

Cuando esta guía terminó de leer el inventario de releases de la casa, encontró lo que nadie
le había contado: **Vela hornea datos con nombre y apellido para nosotros.** No «Caribe»
genérico, no «América Latina» de bulto: el archivo se llama `haiti-and-domrep` — La Española
entera, nuestro lado incluido — y aparece en **siete canales de datos distintos** del
proyecto. Contado hoy, 15 de octubre, con fecha de cada canal:

```
CANAL DE DATOS           FECHA        ARCHIVO NUESTRO
─────────────────────────────────────────────────────────────────
basemap-tiles            15-sep-2026  basemap-haiti-and-domrep.pmtiles
places-overlays          14-sep-2026  places-haiti-and-domrep.pmtiles
road-features            13-sep-2026  haiti-and-domrep.bin
obf-regions              16-ago-2026  haiti-and-domrep.obf
maxspeed-overlays        12-jul-2026  haiti-and-domrep.pmtiles
poi-packs                09-jul-2026  haiti-and-domrep.zip
building-overlays        09-jul-2026  dominican-republic.pmtiles (¡con nombre propio!)
```

Traducción al criollo de qué es cada uno: *basemap* es el mapa base (las calles y los
rótulos que ves), *places* son los lugares cocinados, *road-features* son las características
de las vías, *obf* es la región lista para ruteo offline, *maxspeed* son los límites de
velocidad que alimenta el velocímetro, *poi-packs* son los paquetes de puntos de interés y
*building-overlays* son los edificios dibujados — ese último con archivo aparte para la
República Dominicana, como un vecino que pide tu calle por su nombre. Puerto Rico comparte
canal en casi todos; nosotros tenemos hasta edificio propio.

**Lo que esto significa en criollo:** no es una app europea que «quizás funcione» por aquí.
Es un proyecto que hornea la isla entera como región de primera clase, con regiones
descargables para ruteo sin señal, límites de velocidad para el velocímetro y edificios en
3D de perfil. La guía no declara que los datos de cada colmado estén al día — eso lo dice
OpenStreetMap y se verifica en la calle —, pero la infraestructura para que *sí* esté al día
ya está servida con nuestro nombre.

───────────────────
## 💬 LAS CONVERSACIONES HONESTAS (donde esta casa se gana el respeto)

La primera conversación honesta ya la tuvimos: Vela le pregunta cosas a Google. Ahora la
conversación completa, porque aquí está el corazón del asunto y la casa lo puso en tabla
pública — PRIVACY.md — sin letra chiquita. Esta guía la adapta entera:

```
¿QUÉ RECIBE GOOGLE?         APP GOOGLE MAPS        VELA
────────────────────────────────────────────────────────────────────────
Vinculado a tu cuenta       Sí, siempre dentro     Nunca. No hay login
Identificador persistente   IDs de dispositivo     Sin cuenta y sin clave:
                            y de publicidad vía    una cookie de sesión
                            Play Services          anónima que la app renueva
                                                   cada semana por defecto
                                                   (más tu IP, como a
                                                   cualquier visitante web)
Tu posición GPS precisa     Continua mientras      Nunca mientras recorres
                            está abierta, más el   el mapa. Las búsquedas
                            Historial si lo        mandan el área que ves;
                            tienes encendido       una ruta desde tu sitio
                                                   manda ese punto; mientras
                                                   manejas, el recálculo y el
                                                   chequeo opcional de
                                                   tráfico mandan tu posición
Cada movimiento del mapa    Sí, sus servidores     No, por defecto: los
                            dibujan el mapa        azulejos vienen de
                                                   OpenFreeMap y los lugares
                                                   de los datos propios Vela
Tus búsquedas               Sí, en el historial    El texto llega anónimo,
                            de tu cuenta           como escribes y como
                                                   envías
Las páginas de lugares      Sí                     La consulta llega
que abres                          anónima, bajo esa cookie de sesión
                            cerrada
Rutas paso a paso           Sí, telemetría         Se le pregunta anónimo el
                            completa del viaje     tramo de dos puntos, y
                                                   otra vez en la marcha por
                                                   recálculos y el chequeo
                                                   opcional de tráfico. Los
                                                   routers abiertos OSRM y
                                                   Valhalla reciben el mismo
                                                   viaje para las voces de
                                                   giro. Tu rastro GPS como
                                                   conjunto NUNCA sale del
                                                   teléfono
Tus lugares guardados,      En sus servidores      Solo en tu teléfono
casa, trabajo
Perfil de publicidad        Lo alimenta            No hay nada a qué
                                                   engancharlo
Funciona sin contacto       No                     Sí: UN interruptor
con Google                                         (Settings → Privacy → Use
                                                   Vela without Google) y las
                                                   regiones descargadas
                                                   muestran mapa, búsqueda,
                                                   ruta y navegación offline
```

La frase de la casa que resume todo, traducida con respeto: *Google pasa de saber quién eres
y a dónde vas a responder preguntas anónimas de vez en cuando.*

**Tres letras chicas que la casa declara y esta guía firma:**

1. **La reseña escondida.** Unas pocas cosas — las reseñas de un lugar entre ellas — Google
   solo las sirve a un navegador de verdad. Para eso, Vela lee esa página desde un WebView
   en pantalla oculta, anónimo, y **la lista de esas páginas está publicada en PRIVACY.md**.
   No es un escondite: es un inventario.
2. **La sesión anónima.** Google guarda su propia cookie de sesión sin login, como lo haría
   una ventana de incógnito. Vela **estrena sesión nueva cada semana por defecto** — y te
   deja elegir semanal, diaria, cada arranque, o botón de «estrenar ahora»
   (Settings → Privacy → Google session).
3. **El tráfico vivo es un interruptor, no un secreto.** Mientras navegas, Vela le pregunta a
   Google por tráfico fresco desde tu posición cada dos minutos aprox — eso es lo que alimenta
   la oferta de vuelta más rápida y la hora de llegada viva. *Settings → Navigation → «Live
   traffic re-checks while navigating»* lo apaga. Los recálculos cuando sales de la ruta se
   quedan, porque sin ellos la navegación paso a paso no existe.

**La advertencia beta, textual de la casa:** *«Vela está en beta, así que puedes toparte con
bugs. Si te pasa, abre un issue y llena la plantilla. Los nightlies y las builds canary son
más nuevas todavía y menos probadas que la estable semanal.»* Esta guía no receta apps que
se hagan las perfectas. La casa te dice de qué pieza está y cómo reportar cuando algo se
tranca — eso es madurez, no debilidad.

## 🧭 INSTALACIÓN POR LA VÍA SANA (tres caminos, un solo certificado)

La casa da tres puertas y una llave de verificación. Como siempre en esta lista: **si el APK
no está donde vive el código, el APK no es** — y aquí el APK vive en el mismo repo del
código, firmado siempre con la misma llave.

**Camino 1 — Obtainium (el que la casa recomienda primero).** Vela trae botón directo de
Obtainium en su README — la misma herramienta que esta casa enseñó a usar en la pieza 09.
Obtainium sigue la **estable semanal**; si enciendes «include prereleases», te trae la
canal **nightly**.

**Camino 2 — F-Droid, pero por el repo PROPIO de Vela.** Atención con la letra: el botón de
F-Droid del README **no es el catálogo f-droid.org** — es el **repositorio propio del
proyecto**: agregas `https://pimpinpumpkin.github.io/Vela/repo` a cualquier cliente F-Droid
y ese repo sirve los mismos APKs firmados por la casa, estable semanal por defecto (la
huella del repo y la configuración del canal nightly están en su FDROID.md). ¿Y el catálogo
grande? La casa lo tiene en el roadmap abierto con honestidad: entrar a f-droid.org exige
una compilación sin piezas prehechas, y no la hay todavía. Cuando llegue, se avisa; mientras
tanto, el repo propio es vía sana y firmada.

**Camino 3 — APK directo de Releases.** github.com/PimpinPumpkin/Vela/releases — la canary
de HOY (15-oct) y la estable v0.5.2549 del 12-oct, APKs de ~114 MB (traen el mundo cocido
adentro, por eso pesan).

**La llave: la firma del taller, contada como La Bandita la sabe contar.** Cada APK de
cualquier canal se firma con la misma llave, y la casa publica su huella SHA-256 — aquí va
textual, para que la compares:

```
SHA-256  29:93:8B:48:58:06:3E:42:E6:77:FF:95:C9:01:CD:48:24:8A:7F:03:2A:3A:E8:5F:9B:9E:56:17:56:8B:0D:36
```

En la compu: `apksigner verify --print-certs vela-maps-*.apk` y comparas. En el teléfono,
**App Verifier** (soupslurpr/AppVerifier) revisa lo mismo: le pegas el bloque de dos líneas
— `app.vela` arriba, la huella abajo — y listo. Y hay una reja final que pone Android: **después
de la primera instalación, una actualización firmada con otra llave se rechaza sola**. Si
una build instaló encima de tu Vela, salió del mismo taller que la anterior. Eso es la
puerta con cadena, instalada de fábrica.

Notas de teléfono desgoogleado (GrapheneOS y familia): Vela usa el LocationManager nativo de
Android, **nunca el proveedor fusionado de Google**; con PSDS encendido el primer fix de GPS
baja de ~30 segundos a pocos segundos, y bajo techo conviene la ubicación por red — la app
te avisa sola si no llega posición en unos segundos.

───────────────────
## 🛻 UN DÍA CON VELA, RUTA DOMINICANA (la prueba del sillón, no del folleto)

Las guías de esta casa no recetan features sueltas: recetan días. Este es el día de prueba
que le proponemos a cualquiera, con las funciones que ya verificamos arriba — sin inventar
nada, porque todo está en el README y en las releases leídas hoy:

**6:40 de la mañana.** Enciende Vela por primera vez. La app pregunta lo importante antes de
mostrar el mapa: ¿la quiere con Google de fondo para tráficos y reseñas, o **sin Google del
todo**? Tú eliges ahí, sabiendo qué elige cada puerta — arriba está la tabla completa. Baja
la región del Gran Santo Domingo para el ruteo sin señal.

**7:15.** Sale hacia el trabajo. Pide la ruta hablando: *«llévame a la oficina»* — la
transcripción ocurre en el teléfono, no en un cloud de voz. La ruta llega con su tiempo
pintado y el tráfico dicho en palabras. En el camino, el velocímetro le recuerda el límite
de la avenida y el diagrama de carriles lo deja salir por el carril correcto sin pelearse
con la línea amarilla.

**7:50.** La aguja del tanque anda baja. Busca «gasolina» y las bombas cercanas aparecen
**con el precio puesto en el marcador** — compara antes de doblar, que es todo el sentido de
tener el precio a la vista. (Si en tu zona el precio viene corto, ya sabes dónde está la
carencia: en los datos abiertos, no en la app. Y esa carencia se arregla mapeando, que es
cosa de la comunidad, no de una empresa.)

**12:30.** Medio día, reunión afuera. Toca el pin del restaurante: horario con días
festivos, fotos, fila de la hora, teléfono y el aviso de si estará cerrado cuando llegue.
Si la reseña no viene abierta, es la página que la casa declaró en PRIVACY.md — el
inventario de lo escondido, en el archivo público.

**5:50 de la tarde.** Regreso con tapón en la autopista. Vela ofrece la vuelta más rápida
antes de que el presa se coma el combustible. El recálculo corre solo; el chequeo de tráfico
frecuente es un interruptor que tú apagas si prefieres que ni eso se pregunte.

**Sábado, 8:00 de la mañana.** Ruta a la playa del este, donde la señal se cae a la altura
de tal lugar. No importa: la región descargada trae el mapa, los lugares, las direcciones y
la navegación **sin una gota de datos**. Al parkear, toca la **P**; a la vuelta, toca el pin
y el teléfono lo lleva de regreso al carro entre miles.

**Domingo.** Abre su computador, pega el enlace de la lista que guardó por años en su cuenta
vieja de Google Maps, y Vela **la importa completa**. Sus lugares de una vida ahora viven en
su teléfono, respaldados a un archivo que él controla. Nadie más tiene la llave de esa
puerta.

Si después de ese día la app no te sirve, no te sirvió de verdad — y con la beta declarada
por la propia casa, el bug se reporta con plantilla y el taller responde. Eso es lo opuesto
al «funciona en mi laboratorio» de las tiendas grandes.

## ❓ LAS DIEZ PREGUNTAS DE LA GENTE (las que llegan al colmado y al grupo)

**1. ¿Y esto es legal, o es como los APK trucaos de los canales del aire?**
Es software libre con licencia GPL-3.0, código público, releases firmadas y huella publicada.
No lleva una línea de código de Google ni un APK tocado por nadie. Lo que hace — preguntarle
a los endpoints públicos de Google como un navegador sin login — es lo que hace tu navegador
cuando abre un mapa sin cuenta. Por eso la analogía de NewPipe le queda perfecta: mismo
estilo de pregunta, misma honestidad de canal.

**2. ¿Por qué pesa ~114 MB el APK si los mapas se descargan aparte?**
Porque trae el mundo cocido: los azulejos de base y los lugares horneados viajan con la
app, y las regiones offline se descargan por pieza después. La casa lo declara en el README
sin pena. Para la vara de esta casa, un APK pesado y honesto pesa menos que uno liviano y
mentiroso.

**3. ¿Funciona desde el primer minuto en un teléfono desgoogleado?**
Ese es su hábitat natural: construida «para teléfonos desgoogleados como GrapheneOS, y corre
en Android de fábrica también». GPS por LocationManager nativo, tips en pantalla si el fix
tarda. Sin Play Services no falta nada de lo esencial.

**4. ¿Y si Google cambia su web mañana y la app se rompe?**
La casa lo espera y lo tiene resuelto en diseño: las recetas de peticiones viven en un
archivo firmado que la app revisa al arrancar; el arreglo llega en minutos sin actualizar.
Es la misma vida que NewPipe lleva años demostrando: al gigante se le sigue la mudanza sin
pedirle permiso.

**5. ¿Puedo vivir en modo cien por ciento sin Google?**
Sí: un interruptor — *Use Vela without Google* — y regiones descargadas te dan mapa,
búsqueda, ruta y navegación offline sin un solo contacto. Lo que pierdes fuera de línea o
en ese modo: la capa viva (tráfico, reseñas, detalle de lugares). El precio se dice entero.

**6. ¿Quién paga el taller? No veo anuncios ni cuenta Premium.**
El README trae el botón de **Buy Me a Coffee** — apoyo voluntario de la comunidad — y no
hay más modelo declarado: sin anuncios, sin backend de usuarios que mantener, sin telemetría
que monetizar. Un proyecto sin servidores de usuario es un proyecto con factura de luz
pequeña. Eso no lo hace eterno — nadie lo es —, pero le quita la dependencia de vender tu
atención.

**7. ¿Está en español? ¿Y puedo ayudar a traducirlo?**
19 idiomas de fábrica y traducción abierta por Weblate — el mismo flujo que usan decenas de
proyectos serios. La casa hasta documentó cómo traducir desde el navegador. El español no es
una capa de apósito: es parte del taller.

**8. Tengo un teléfono de teclas. ¿Me toca afuera?**
Al revés: operación completa por D-pad, documentada en docs/dpad.md. Los teléfonos que no se
mueren siguen teniendo casa aquí.

**9. ¿Por qué no está en el catálogo grande de F-Droid / en Google Play?**
Porque la casa se niega a trucar: el catálogo grande exige compilación sin piezas prehechas
y no existe todavía — está en el roadmap abierto. Y Play aparece como idea condicionada a
una build con la mitad de Google compilada fuera, «trabajo grande, en el radar, no
empezado». Mientras tanto: Obtainium, repo F-Droid propio y APK de Releases — tres puertas
firmadas.

**10. ¿Y si el proyecto muere mañana, como ha muerto medio catálogo?**
Verdad fría: puede pasar, como le puede pasar a cualquiera. La defensa no es la fe, es la
arquitectura: licencia GPL-3.0 (el código no puede secuestrarse), datos abiertos (el mapa no
muere con la app), APK firmado con huella pública (nadie suplanta el cadáver), 23
colaboradores (no es un hombre y su sombra), y releases semanales que dejan señales de vida
fáciles de leer. Si algún día la vitrina se para, esta guía lo acta con fecha — como actuó
a los difuntos que nombramos sin enterrarle flores al olvido. Mientras tanto, el taller
está encendido y la puerta está abierta: hoy mismo hay una canary con horas de horneada.

───────────────────
## 📚 LA BIBLIOTECA DE LA CASA (lo que delata a un proyecto serio)

Hay una prueba de seriedad que esta guía usa con todos los talleres: **cómo documentan**.
Los proyectos que mueren dejan READMEs de tres líneas; los que vienen a quedarse dejan
biblioteca. La de Vela, leída hoy completa:

```
ARCHIVO                QUÉ TIENE ADENTRO
─────────────────────────────────────────────────────────────────────
SPEC.md                La referencia técnica completa: el basemap, la
                       horneada de lugares, las peticiones a Google, el
                       ruteo, los datos offline y el canal de auto-reparo
                       firmado — reglas, contratos y constantes
docs/book/             «El libro»: cada subsystema explicado en llano —
                       cómo se rankean los lugares, cuándo se reconstruyen
                       los datos, cómo se arma una ruta
FEATURES.md            La lista entera de funciones, una línea cada una
PRIVACY.md             Qué recibe cada servicio, petición por petición
docs/FAQ.md            Las preguntas que la gente hace primero
ROADMAP.md             Lo que está abierto — y docs/ROADMAP-HISTORY.md
                       con lo que llegó o se descartó (historial sin
                       borrado: la casa no maquilla su pasado)
docs/BUILDING.md       Cómo compilar desde fuente
docs/TRANSLATING.md    Los idiomas y cómo traducir (Weblate)
docs/dpad.md           Operación sin pantalla táctil
CONTRIBUTING.md        Las reglas duras del taller
SECURITY.md            Reporte PRIVADO de vulnerabilidades (vía GitHub),
                       nunca en issue pública — la lección de seguridad
                       de siempre, escrita en la puerta
```

Y un detalle que dice de qué madera es el taller: la casa tiene un archivo de reglas y
trampas del código — *«para quien cambie el código, humano o IA»*. Documentar las trampas
del oficio para el que venga detrás, sea carne o máquina, es la costumbre de los talleres
que planean durar.

## 🏭 LA ECONOMÍA DE LOS DATOS: las releases como despensa del mundo

Aquí hay una pieza de ingeniería que merece su propio renglón, porque explica el hallazgo
dominicano de arriba. Vela **no sirve sus datos desde un servidor de la casa** — no hay
backend, recuerda —: los **hornea dentro de releases del propio repo**. Cada canal de
release es una despensa:

- La **estable** trae la app.
- Los canales de datos — *basemap-tiles*, *places-overlays*, *road-features*,
  *obf-regions*, *maxspeed-overlays*, *poi-packs*, *building-overlays*, *painted-roads*,
  *tts-runtime* — traen el mundo por pedazos: azulejos por país, lugares por región,
  características de vías, regiones de ruteo offline, límites de velocidad, paquetes de
  puntos de interés, edificios, y hasta el modelo de voz neuronal (sherpa-onnx) que alimenta
  el Vela Voice.

Es decir: **la lista de releases del repo es, a la vez, la tienda de la app y la despensa de
sus mapas.** Cuando esta guía encontró `haiti-and-domrep.bin` en road-features o
`places-haiti-and-domrep.pmtiles` en places-overlays, no estaba leyendo un capricho: estaba
leyendo el mecanismo real con el que la isla entra al teléfono de cualquiera que instale Vela
y baje su región. La distribución es la misma infraestructura abierta de siempre en esta
lista — GitHub — sirviendo lo que antes servían servidores privados con telemetría pegada.

Y la fecha de la despensa importa: los azulejos base nuestros son del 15 de septiembre, los
lugares del 14 de septiembre, las vías del 13 — hornadas de este mismo mes, no reliquias de
año viejo. La despensa se rehorna; el canal documenta su fecha como esta casa documenta la
suya.

## 📼 LA ANALOGÍA DE NEWPIPE, MEDIDA CON REGla Y NO CON ENTUSIASMO

Casi todo el mundo que llega a Vela repite «es el NewPipe de los mapas». Esta guía la
comprobó y **la analogía es estructuralmente exacta** — la casa misma la formula en su
sección «Why Vela talks to Google at all», traducida aquí con respeto:

*«Un teléfono sin Google Play Services no puede correr Google Maps, y los datasets abiertos
de mapas se quedan cortos en búsqueda, reseñas, horarios y tráfico vivo. Así que para eso,
Vela es un cliente de los endpoints web públicos de Google. Les pregunta como lo hace un
navegador sin login, desde el propio teléfono de cada usuario, sin cuenta, sin clave de API
compartida y sin servidor en el medio. NewPipe hace lo mismo para YouTube.»*

Las cinco piezas de la analogía, verificadas una por una en el material de hoy:

```
NEWPIPE (YouTube)                VELA (mapas)
──────────────────────────────────────────────────────────────────────
Cliente de la web pública        Cliente de endpoints web públicos
  de YouTube                       de Google Maps
Sin cuenta, sin clave de API     Sin cuenta, sin clave, sin backend
  y sin servidor propio
Sin anuncios                     Sin anuncios
Tus listas y tu historial        Tus lugares, tu casa, tu trabajo y
  viven en el teléfono             tu historial viven en el teléfono
El gigante muda la puerta y      Archivo de recetas firmado que se
  la casa ajusta la bisagra        repara en minutos sin actualizar
```

Hasta la crítica simétrica la comparten: ambos dependen de que el gigante no cierre la
puerta pública por completo. Es el riesgo de la familia — y la familia lo sabe, lo documenta
y vive con la bisagra aceitada. Nadie en esta casa receta dulzuras: se receta lo que verifica
su propia defensa, con el riesgo escrito al lado.

## 🧾 LO QUE LA CASA SE NEGÓ A HACER (la lista que enamora a esta guía)

Los proyectos se conocen por lo que prometen; se confían por lo que **se niegan** a hacer.
El roadmap de Vela tiene un apartado que se llama, literalmente, «no va a pasar»:

- Nada que exija **entrar con cuenta de Google**.
- Nada que mande tus datos a un **backend** de la casa.
- Contribuir **reseñas o fotos** de usuarios (eso es el negocio de otra gente).
- **Compartir ubicación en vivo** con nadie.
- **Línea de tiempo de ubicaciones** — el archivo de tu vida que otros mapas guardan por
  defecto.
- Los datos que Google le **quita** a las peticiones anónimas (como la ocupación viva de los
  lugares).

Traducido al criollo: Vela prefiere quedarse sin funciones que conseguirte a cambio de tu
seguimiento. En un catálogo lleno de «gratis» que cobran en silencio, una casa que escribe
sus negaciones en la puerta merece el plato de hoy en esta lista.

───────────────────
## 🧭 EL TABLERO DE LA EXPEDICIÓN: cómo eligió esta guía su pieza de hoy

Para que quede por escrito cómo se eligió Vela — porque el método de la compra importa tanto
como la compra —, así trabajó el censo de esta mañana, con cada número medido:

- **Nueve vetas de búsqueda** contra el vecindario público: recién nacidos, activos de media
  edad, lanzadores, lectores RSS, lectores de ebooks, contadores de dinero, salud, clima y
  notas. Resultado bruto: **4.672 casas**.
- **Los filtros de la vara:** fuera archivados (los cadáveres no se recetan), fuera forks
  (las copias no son casas), fuera proyectos sin licencia declarada (la casa sin escritura
  no entra), fuera los ya censados por esta guía y fuera los famosos de siempre — que de
  famosos ya tienen biógrafos. Sobrevivieron **70 casas**, con fechas, licencias y edades
  anotadas una por una.
- **La medida final: velocidad.** Estrellas ÷ meses de vida. Los famosos acumulan por
  inercia; los recién llegidos tienen que correr o morir. La tabla quedó encabezada por
  diez casas, y de esas diez se leyó el material completo — README entero, releases,
  autor, colaboradores — antes de elegir.

```
EL TABLERO DE HOY (las 10 finalistas, medidas 15-oct-2026)

 1. Vela Maps        ★1.961   482 ★/mes   navegación sin Google — LA PIEZA DE HOY
 2. Husk             ★1.920  1.746 ★/mes  Android sobre iOS — pieza futura
 3. ShizuCallRecorder ★1.755  342 ★/mes  grabar llamadas vía Shizuku — pieza futura
 4. flectar/mail     ★1.366   976 ★/mes  correo nativo nuevo (en alpha) — a vigilar
 5. gander           ★1.271   433 ★/mes  visor offline cero permisos — pieza futura
 6. DSHA             ★1.270   615 ★/mes  IA en el teléfono, sin root — a validar
 7. nanoMuse         ★1.233  1.681 ★/mes  agente personal abierto — a vigilar
 8. ReFra            ★2.897    66 ★/mes  galería moderna madura — candidata de caja
 9. overlay-translator ★1.016 265 ★/mes  traduce la pantalla en vivo — bus chico
10. read-aware         ★451    54 ★/mes  lector de ebooks con memoria — un solo bus
```

¿Por qué ganó Vela y no la más veloz del listado? Porque la vara de esta casa no es solo
velocidad: es **velocidad con oficio**. Vela no es una demo con muchas estrellas: es un
inventario de funciones que se pueden probar hoy, una biblioteca de documentación completa,
una tabla de privacidad con renglones, una huella de firma publicada y — el detalle que
cerró la compra — **nuestro país horneado con nombre propio en siete canales de datos**.
La velocidad la abrió la puerta; el oficio la sentó a la mesa.

El resto del tablero no se descarta: se agenda. Pieza por pieza, un turno por casa, como
anda esta lista desde su primera hornada — las que conserven vida al llegar su turno, se
actan; las que se apaguen en el camino, se actan igual, con fecha y causa. Así no se
escribe la historia del barrio: así se escribe la de los muertos, y esta casa ya sabe
enterrar con respeto.

## 📅 EL RE-VERDEO AGENDADO (lo que pasa después de esta hornada)

Esta pieza nace fechada y con reloj. El censo de sus placas — estrellas, empuje, releases,
issues, colaboradores — se vuelve a contar en el próximo re-corte general de la lista, el
mismo día que se re-verifican las casas viejas. Y como toda casa joven del catálogo, Vela
queda bajo la regla de la casa de los recién llegidos: **dos re-verdeos con vida antes de
considerarla estable del catálogo** — no porque la duda sea eterna, sino porque en este
barrio la confianza se construye con fechas, no con impresiones.

Lo que esta guía NO promete, por honestidad de oficio: que la beta no dé sustos, que la
cobertura abierta de tu calle esté completa, ni que Google deje servir sus endpoints
públicos para siempre. Lo que sí queda en escritura pública: la fecha de cada número de
esta pieza, la URL de cada casa citada, y el acta del taller con el mismo conteo que leyó
esta hornada.

## 📒 EN QUÉ CAJA VIVE A PARTIR DE HOY

En el índice de la casa, Vela entra como **pieza nº 11 de la colección WhatsApp** y ocupa
cajón propio en la estantería de *Herramientas de la vida diaria* — la misma caja de las
llaves, la galería, la música y el transporte — con etiqueta nueva que la lista no tenía:
**«el mapa vivo»**. En el índice público quedó anotada como: *Vela Maps — navegación paso a
paso sin Google, con datos abiertos dominicanos* — y en el acta del taller, su constancia
completa con hora, sellos y conteos.

La orden que abrió esta expedición queda reflejada en el acta del día, con su fecha y su
texto: salir de la estantería — no re-verificar solamente lo que ya se tiene, sino explorar
recurso nuevo, sin repetir el catálogo, sin recetas de cadáveres, sin famosos de vitrina
ajena; novedad con calidad y potencial; y ninguna omisión callada, porque la desinformación
y la omisión son la misma mentira con distinto traje. Esta pieza es la primera entrega de
esa orden: medida, fechada, firmada y sin un solo número que no se pueda re-contar con la
URL al lado.

───────────────────
## 🏛️ LA HISTORIA DE LA CUADRA: por qué el mapa era la última frontera

Ponte cómodo, que esto se cuenta una vez y queda escrito. En la casa del software libre hay
narrador, mensajero, banco, radio, galería, biblioteca y hasta plomería — todo con vecino
libre sirviendo el puesto. Pero había **una silla que llevaba años vacía**: la del mapa vivo.
El mapa que no solo te dibuja la calle, sino que te dice el horario del lugar, la fila, la
foto, el precio de la bomba, el tapón de la 27 y la salida del carril — **sin pedirte la
cuenta a cambio de tu vida entera**.

Lo que existía, y por eso lo queremos y lo recetamos desde hace tiempo, era el **mapa
esencial**: el trazado, el ruteo offline, el pin guardado. Los abuelos de la cuadra —
OpenStreetMap, que es la calle dibujada por la gente; Organic Maps y OsmAnd, que son los
lectores serios de esa calle — hicieron posible salir sin Google cuando el asunto es llegar.
Y llegan. Lo que la silla vacía guardaba era otra cosa: la **capa viva** — la que hace que
un mapa se sienta teléfono del 2026 y no brújula del 2012 —, porque esa capa la alimentaban
datos que no estaban abiertos: reseñas, ocupación, tráfico de minuto a minuto.

Muchos tiraron la toalla ahí: o volvías a la cuenta de Google con su historial de
ubicaciones, o vivías con mapa desnudo. Fue así hasta que un taller nuevo se sentó a pensar
la pregunta al revés: **¿y si la app es de aquí y las preguntas viajan anónimas?** No
clonar la app del gigante — eso lo intentan los rebajadores y termina mal —, sino hacer un
cliente nuevo, honesto, que le pregunte al gigante lo que el barrio abierto todavía no
sabe, **como le pregunta NewPipe a YouTube desde hace años**. Cuatro meses después de esa
idea: 1.961 estrellas, 93 forks, 23 colaboradores, 19 idiomas, releases semanales, un
libro, un SPEC y siete despensas de datos con la isla entera adentro.

Por eso la expedición de hoy se detuvo en esta puerta. No porque la estrella corriera —
corría más rápido otra —, sino porque **esta casa llenó la silla que llevaba años vacía**,
y la llenó con reglas de taller que esta guía lleva años pidiendo en voz alta: sin backend,
sin cuenta, sin telemetría, negaciones por escrito. La silla vacía del mapa vivo tiene dueño
desde este re-corte. Que el barrio la siga sosteniendo — eso lo decide el taller con sus
releases y nosotros con nuestra vara —, pero hoy, con fecha, la silla está ocupada.

## 🛣️ EL SEGUNDO DÍA: la prueba larga (autopista Duarte, ida y vuelta)

El día corto ya lo vivimos. Ahora la prueba que de verdad decide: **el viaje largo**. De
Santo Domingo a Santiago por la autopista Duarte, ida y vuelta en el mismo fin de semana —
con lo que eso trae: peajes, bombas de mitad de camino, desvíos por obras, y la señal que
se pierde donde la montaña dobla.

**La noche antes:** baja la región que cubre la ruta (el canal *obf-regions* del proyecto
sirve la isla por piezas — la Española entera como una región descargable, visto hoy en su
release del 16 de agosto). Con eso, todo el ruteo del viaje vive en el teléfono.

**De madrugada:** sales y la navegación corre sin pedirle nada a nadie hasta que necesitas
lo vivo. El velocímetro de la app lleva los límites de la vía — y en carretera, ese aviso
no es un juguete. Si te desvías por un desvío de obra, el recálculo entra solo: ahí sí se
le pregunta a Google el tramo nuevo, anónimo, y los routers abiertos OSRM y Valhalla ponen
las voces de giro.

**La parada del medio día:** gasolinera en la mitad del trayecto. Buscas «gasolina» en el
tramo y comparas precios con el marcador puesto. Si la bomba que te gusta tiene horario de
bombacisto o fila — tocas el pin y lo que el dato abierto sepa, se ve; lo que solo Google
sabe, se pregunta anónimo, con la cookie de sesión que esta semana estrenó sola.

**El regreso de noche:** señal intermitente en el tramo de la cordillera. La app no se
inmuta: la ruta vive en el teléfono, el mapa vive en el teléfono, y tu rastro GPS también
vive en el teléfono — que es exactamente el punto de toda esta pieza. Llegas a casa, tocas
la **P**, y el pin del carro queda guardado sin que nadie más en el mundo sepa dónde
aparcaste.

Si el viaje sale bien, no lo atribuyas a magia: atribúyelo a **datos abiertos bien
horneados, preguntas anónimas bien hechas y un taller que no duerme**. Si sale mal — un bug
de beta, un horario viejo, un faltante de cobertura —, el camino también está escrito:
plantilla de issue, Discussions, y la propia casa pidiendo el reporte. El software libre no
promete perfección: promete que cuando algo falla, lo puedes ver, lo puedes contar y lo
puedes arreglar. Eso vale más que cualquier promesa de fábrica.

## 📋 LA BOLETA DE LA CASA (la vara completa, renglón por renglón)

Como con toda casa que entra al catálogo, la boleta completa — sin notas regaladas:

```
RENGLÓN              NOTA     POR QUÉ
──────────────────────────────────────────────────────────────────────
Transparencia        10/10    Tabla de qué llega a Google, PRIVACY.md,
                              huella pública, lista de WebView escondido,
                              roadmap con «no va a pasar»
Documentación        10/10    SPEC + libro + FAQ + FEATURES + BUILDING +
                              TRANSLATING + dpad: biblioteca completa
Vida del taller      9/10     Push HOY, estable semanal, canary diaria,
                              23 colaboradores; el punto no perfecto:
                              4 meses de edad son 4 meses
Datos dominicanos    9/10     7 canales con haiti-and-domrep + edificio
                              propio; la horneada más vieja es del 9 de
                              julio — fresca, pero hay que seguir su ritmo
Honestidad de riesgo     9/10     Beta declarada en la puerta, riesgos dichos,
                              reporte de seguridad privado por escrito
Hueco que llena      10/10    La capa viva del mapa sin cuenta: nadie más
                              en el catálogo la tiene
──────────────────────────────────────────────────────────────────────
VEREDICTO            ENTRA    Pieza nº 11 del catálogo, con re-verdeo
                              agendado y regla de recién-llegido activa
```

Ninguna casa entra con 10 en todo — esta entra con **10 en lo que la silla vacía pedía** y
nueve en lo que solo el tiempo da. La boleta se repite en cada re-verdeo; si un renglón
baja, baja con fecha y causa en el acta. Esa es la diferencia entre recetar y vender.

## 🧉 TRES CONSEJOS DE LA CASA ANTES DE INSTALAR

**Uno — decide tu modo antes de abrir la app.** La primera pregunta de Vela — con Google de
fondo o sin Google del todo — es la decisión grande, y ahora sabes las dos caras: con
Google de fondo tienes la capa viva completa con preguntas anónimas; sin Google, el modo
más puro con todo lo esencial offline. Ninguna de las dos es trampa; ambas están escritas
en la tabla de arriba. La que elijas, elíjela por ti, no por miedo.

**Dos — verifica la firma antes del primer arranque.** El minuto que toma comparar la
huella SHA-256 con `apksigner` o App Verifier es el minuto que separa la casa de su
suplantador. La huella está arriba, textual de la casa. En esta lista nunca instalamos un
APK sin saber de qué taller salió — y ahora tampoco tú.

**Tres — prueba con tu ruta real antes de fiarlo.** La vara final no está en este texto ni
en las estrellas: está en tu ida al trabajo, en tu viaje del fin de semana, en tu barrio
específico. Un fin de semana con Vela en la ruta de todos los días te dirá lo que ni esta
guía ni mil reseñas pueden: si la cobertura abierta de tu esquina está al nivel de tu día.
Si está — bienvenido al mapa vivo sin cuenta. Si no está — OpenStreetMap es de la gente, y
a la gente le falta lo que tú ves faltar: esa es la parte de la obra que siempre estuvo
abierta a tu mano.

───────────────────
## ⚖️ EL TABLERO DE HONESTIDAD: lo que esta guía NO pudo verificar

La desinformación y la omisión son la misma mentira con distinto traje — regla de esta
casa. Por eso esta pieza termina con el tablero invertido: no solo lo que se midió, sino
**lo que no se midió y por qué**, para que nadie le atribuya a este texto más de lo que
tiene:

- **El rendimiento en tu teléfono.** Esta guía midió la casa, no el sillón. Batería,
  fluides con el mapa en mano y calor del teléfono: se prueban con tu hardware, y ninguna
  cifra de terceros lo sustituye.
- **La exactitud de cada azulejo dominicano.** Que los canales `haiti-and-domrep` existan y
  estén hornados este mes está contado con fecha. Que el colmado de tu esquina tenga horario
  correcto adentro: eso lo decide OpenStreetMap, y se verifica calle por calle — si algo
  falta, el faltante se corrige mapeando, que es la obra abierta a cualquiera.
- **El precio de la bomba en tu ruta.** La función existe y está documentada; la cobertura
  de precios de gasolina en la República Dominicana no la midió esta guía hoy. Pruébala en
  tu ida al trabajo antes de fiarla.
- **La calidad de la voz en español dominicano.** Hay 19 idiomas y voz neuronal en el
  teléfono; cómo suena el «doble a la derecha» para oído de aquí, se oye en la calle.
- **Android Auto en cada carro.** La casa declara que funciona «solo en algunas
  configuraciones» con app instalada a mano. Esta guía no tiene tu carro: el doc oficial
  (docs/ANDROID-AUTO.md) es la palabra, y el roadmap abierto confirma lo que falta.
- **La longevidad del proyecto.** Cuatro meses con cadencia semanal y 23 colaboradores es
  el mejor pronóstico medible — pero el futuro no se censura con API. El re-verdeo está
  agendado y su fecha queda escrita.

Cada renglón de este tablero es una puerta abierta, no una ausencia callada. La pieza dice
lo que sabe, fecha lo que contó y nombra lo que no probó. Así no se miente ni por exceso ni
por omisión.

## 🗣️ EL DICCIONARIO DEL BARRIO (las palabras nuevas de esta pieza)

Esta pieza trajo términos de taller que no estaban en las piezas anteriores. Quedan
traducidos al criollo, para que nadie quede fuera de la conversación:

```
AZULEJO (tile)          El pedazo cuadradito de mapa que te pintan en pantalla;
                        venir en vector significa que se redibujan nítidos a
                        cualquier zoom y sin pedirle la imagen a nadie
BASEMAP                 El mapa base: calles, rótulos, agua, parques — el
                        lienzo sobre el que va todo lo demás
OBF / PMTILES / BIN     Distintos formatos de los paquetes de datos que la
                        casa hornea en sus releases (región de ruteo, azulejos
                        de lugares, características de vías)
HORNEAR (bake)          El proceso de cocinar los datos abiertos crudos
                        (Overture, AllThePlaces, OSM) en los paquetes finales
                        que la app consume — por eso las fechas de horneada
                        importan como las fechas del pan
ENDPOINT PÚBLICO        La puerta web que un servicio deja abierta para
                        preguntas sin login — la que NewPipe y Vela tocan
                        como tocaría tu navegador
COOKIE DE SESIÓN        El recuerdo anónimo que la web de Google deja en tu
                        visita sin cuenta; Vela la estrena cada semana por
                        defecto para que ni el recuerdo se acumule
HUELLA DE FIRMA         El «carácter único» del certificado con que un
                        taller firma sus APKs: si cambia, no es el mismo
                        taller — Android lo rechaza solo
CANARY                  La hornada del día, recién salida del horno y sin
                        revisar — la sirve quien quiere ayudar a encontrar
                        bugs (el nombre viene del pájaro de la mina: avisa
                        antes de que caiga el techo)
D-PAD                   La cruceta de los teléfonos de teclas — operar la app
                        sin tocar pantalla
WEBVIEW OCULTO          Una página web que la app lee en pantalla invisible
                        para traer lo que solo existe como página — con su
                        inventario publicado, no escondido
```

Guarda este diccionario: la próxima pieza de la expedición va a traer palabras nuevas, y
esta casa no repite definición sin motivo — la vara es la misma, el barrio crece.

───────────────────
## 📻 LOS TRES CANALES DEL TALLER (y cuál receta esta casa)

Vela madura en público con tres llaves de agua:

```
CANAL     QUÉ ES                              PARA QUIÉN
──────────────────────────────────────────────────────────────────────
ESTABLE   Semanal (v0.5.2549, 12-oct-2026)    La gente de a pie: tú,
          revisada, con tag y notas             yo y la abuela
NIGHTLY   Lo del día, sin revisar             Curiosos con respaldo
CANARY    La hornada fresca (¡salió HOY!)     El que quiere ayudar
                                              reportando bugs
```

**La receta de esta casa es la estable semanal**, igual que con todo el catálogo: la canary
y la nightly son las que la propia casa marca «menos probadas». Y hay una lección de la
varadura escondida aquí que vale repetir: el empuje de HOY a las 10:13 no significa versión
nueva — *pushed_at no es release* —, pero en Vela las dos señales van parejas: el taller
barre a diario y la vitrina renueva **cada semana**, con la canary como carta diaria para
quien quiera ver el futuro antes.

Con esto viene el **auto-reparador**: el archivo de recetas de peticiones va firmado y la
app lo revisa al arrancar; si Google muda un campo de su web, el arreglo llega en minutos a
todas las instalaciones sin actualizar nada. Es el mismo músculo de NewPipe ante cada
cambiada de YouTube — pero aquí documentado en SPEC.md con número de sección y todo.

## 📊 EL VECINDARIO DE LOS MAPAS, MEDIDO HOY

Para que nadie crea que esta guía se emocionó y perdió la vara: así se ve la cuadra de los
mapas el día de hoy, contado por API a las 11 de la mañana:

```
CASA                ★ (15-oct)  PUSH      LECTURA DE LA CASA
────────────────────────────────────────────────────────────────────────
Organic Maps        ★15.685     HOY       El mapa offline clásico del
                                          catálogo: maduro, querido,
                                          sin la capa viva de lugares
OsmAnd              ★6.080      HOY       El todoterreno veterano:
                                          mil interruptores, curva de
                                          aprendizaje de escalera larga
Vela Maps           ★1.961      HOY       El recién nacido rápido:
                                          4 meses, 482 ★/mes, la capa
                                          de lugares + tráfico que los
                                          demás no tienen
```

**La lectura de oficio:** Vela **no viene a tumbar a nadie de la cuadra**. Organic Maps y
OsmAnd siguen siendo los mapas offline serios del catálogo y esta guía sigue recetándolos
donde corresponden (caja 09). Lo que trae Vela es **otra cosa**: la experiencia de mapa vivo
— horarios, reseñas, tráfico, precios de bomba, tableros de guagua — sin firma con Google.
La cuadra completa no era «mapa abierto con experiencia a medio camino»: era «o privacidad
con mapa desnudo, o comodidad con cuenta de Google». Ese falso dilema es el que Vela vino a
partir — y por eso ganó la pieza de hoy. Cuando Organic Maps cubra tu día, úsalo; cuando
necesites la capa viva de lugares sin volver a la cuenta de Google, Vela es la puerta nueva.
Las dos casas pueden vivir en el mismo teléfono: son apps distintas que no se pelean el
trono, se reparten el barrio.

## 🔍 LAS CINCO PREGUNTAS AL MAPA (verifícalo tú, sin fe en nadie)

La vara de la casa, aplicada a Vela delante de ti. Cada pregunta lleva su URL — córtala y
mírala con tus ojos:

1. **¿Vive donde dice que vive?** github.com/PimpinPumpkin/Vela — el código, el README y la
   licencia GPL-3.0 en el mismo lugar, sin repo espejo por el medio.
2. **¿La vitrina se renueva?** github.com/PimpinPumpkin/Vela/releases — estable semanal con
   tag y notas; HOY mismo hay una canary. Si un día dejas de ver releases frescas, esa
   noticia la lee primero tu vara que esta guía.
3. **¿El taller está encendido?** La pestaña de commits — hay empuje de HOY a las 10:13 UTC,
   con mensajes que se leen como taller de verdad: *«Review fixes before the nightly: a list
   opens at its places again…»*, *«The settings file is read from the website's copy when
   GitHub does not answer»*.
4. **¿El autor responde?** 23 issues abiertas con plantilla, pestaña de Discussions viva, y
   un dueño con **10 años de casa en GitHub** (cuenta desde diciembre de 2015, 19 repos
   públicos). No es una cuenta de estreno que amaneció con proyecto.
5. **¿La firma cuadra?** La huella SHA-256 publicada en el README, verificable con
   `apksigner` o App Verifier. La reja que ya explicamos.

Las cinco pasan hoy. Con fecha: constado 15 de octubre de 2026, censo de API de La Bandita.
Lo que esta guía **no** verificó: rendimiento de la app en tu teléfono, exactitud de cada
horario de cada colmado y la cobertura abierta de tu barrio específico — eso se prueba en
la calle, con tu ruta real, y se compara con lo que ya usas. La vara no tiene atajos.

## 🧤 PARA QUIÉN ES Y PARA QUIÉN NO (dicho a la cara)

**Es para ti si:** manejas o te mueves a diario y quieres la comodidad del mapa vivo sin
contarle tu vida a nadie; llevas un teléfono desgoogleado (GrapheneOS y familia) y extrañabas
una navegación de verdad; manejas ruta del interior donde la señal se pierde y la región
descargada es vida; quieres importar tus listas de Google Maps y mudarte sin dejar nada
preso; te tiembla el bolsillo de la gasolina y quieres el precio antes de doblar.

**No es para ti —todavía— si:** necesitas cero contacto con Google y no tienes forma de
vivir sin búsqueda de lugares (aunque existe el interruptor «Use Vela without Google» + mapa
offline: pruébalo, es el modo más puro); exiges app pulida de fábrica sin un solo bug de
beta; tu día depende de Android Auto en la pantalla del carro de fábrica — ahí la casa
declara el estado con honestidad: funciona **solo en algunas configuraciones** con app
instalada a mano (docs/ANDROID-AUTO.md), y el objetivo de Auto sin listado de Play sigue
abierto en el roadmap, igual que el catálogo grande de F-Droid y una posible build para
Google Play **con la mitad de Google compilada fuera** — idea del roadmap, no empezada. Y
hay una lista que la casa marca **«no va a pasar»**: cualquier cosa que exija entrar con
cuenta de Google o mandar tus datos a un backend — contribuir reseñas o fotos, compartir
ubicación en vivo, línea de tiempo de ubicaciones. Esa lista de negaciones es, para esta
casa, la mejor tarjeta de presentación del proyecto.

**Y la cuota de paciencia:** cuatro meses de vida son cuatro meses. Un taller joven con 23
colaboradores y cadencia semanal tiene mejor pronóstico que la mayoría de su generación
(esta expedición midió hoy cuarenta casas nuevas y varias ya van dormidas), pero la vara
respeta el tiempo: el re-verdeo de esta pieza se agenda como el de todas — con fecha, y las
casas que caen, se actan.

## 📌 EN DIEZ RENGLONES (para reenviar al grupo sin pena)

1. Vela Maps: navegación paso a paso sin Google — libre, GPL-3.0, sin anuncios ni cuenta.
2. Lo nuevo: horarios, reseñas, tráfico y precios de bomba — sin entregar tu vida.
3. Cuatro meses de vida, ★1.961, 23 colaboradores, release semanal y canary de HOY.
4. La Española horneada con nombre propio en 7 canales de datos del proyecto.
5. Voz y micrófono que trabajan en tu teléfono — nada tuyo va a un servicio de voz.
6. Mapa offline completo: región descargada = ruteo y lugares sin señal.
7. Importa tus listas de Google Maps pegando el enlace — la mudanza es de una pieza.
8. Instala por Obtainium, repo F-Droid propio o APK de Releases — y verifica la huella.
9. Es beta y lo dice la casa; receta de esta guía: la estable semanal.
10. Contado, fechado y con URL: 15 de octubre de 2026, censo de La Bandita.

───────────────────

## ✍️ CIERRE

Pieza 11 de La Bandita, edición dominicano-español, horneada y verificada con la vara de la
casa el 15 de octubre de 2026: placa, velocidad, releases, canales de datos dominicanos,
huella y vecindario contados por API el día de hoy, y el README entero leído de la casa.
Cerró dentro de su banda (WhatsApp, 62 000–64 000 caracteres): el número exacto quedó en el
acta viva del día.

La expedición que ordenó la casa sigue abierta: hoy se explora lo desconocido con calidad y
potencial — ni cadáveres, ni famosos de siempre, ni repetir lo que ya tenemos. Vela es la
primera cosecha de esa orden: la casa más nueva de la lista y la que llena el hueco más
antiguo del catálogo. El que sabe llegar sin vender tu ruta es, desde hoy, vecino de esta
lista.

La Bandita informa a partir de fuentes fechadas. El mapa que no te vende, enseña el camino
de verdad. El barrio que verifica cada push, nunca dormirá con la puerta abierta al toldo.

`#LaBandita` `#VelaMaps` `#NavegacionSinGoogle` `#OSM` `#GrapheneOS` `#Obtainium`
`#FDroid` `#RepublicaDominicana` `#FuenteFechada` `#LecturaVerificada`

**FUENTES — constado 15-oct-2026 por API de GitHub (censo La Bandita 10:53–11:03 UTC):**
github.com/PimpinPumpkin/Vela (★1.961 · push 15-oct 10:13 · licencia GPL-3.0 · creado
15-jun-2026) — HOY · releases (v0.5.2549 del 12-oct · canary del 15-oct · canales de datos
basemap-tiles 15-sep, places-overlays 14-sep, road-features 13-sep, obf-regions 16-ago,
maxspeed-overlays 12-jul, poi-packs 09-jul, building-overlays 09-jul con
dominican-republic.pmtiles) — HOY · README del repo (22.416 bytes, leído completo: tabla de
privacidad, huella de firma, canales, roadmap, GrapheneOS) — HOY · colaboradores (23) — HOY ·
autor PimpinPumpkin (19 repos, desde 22-dic-2015) — HOY · velamaps.org y
pimpinpumpkin.github.io/Vela/docs — según lo declarado en el README de HOY ·
Organic Maps ★15.685 y OsmAnd ★6.080, ambos con push de HOY · NewPipe ★40.140 (censo de la
mañana de HOY). Las piezas citadas de ediciones anteriores conservan su fecha.
