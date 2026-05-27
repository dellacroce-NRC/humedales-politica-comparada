# Guía De Repaso Para Entrevistas

Esta guía es para repasar el proyecto antes de una entrevista, una conversación
de portafolio o una demo rápida. No está pensada como documentación pública
principal, sino como una chuleta personal para explicar el proyecto con soltura.

## Pitch En 30 Segundos

Este proyecto toma un debate de política pública y lo convierte en una
simulación interactiva. La idea central es tratar una ley como un clasificador:
observa señales, aplica una regla y produce una decisión pública. Comparo tres
lógicas institucionales inspiradas en Chile, EE.UU. y Colombia, y uso métricas de
clasificación como precision, recall, falsos positivos y falsos negativos para
mostrar qué tipo de error acepta cada diseño.

## Pitch En 90 Segundos

El proyecto nace del debate chileno sobre humedales urbanos y planificación
territorial. En vez de mirarlo solo como una discusión jurídica o ambiental, lo
planteé como un problema de diseño de reglas bajo datos imperfectos.

En la app, cada terreno simulado tiene una realidad de fondo y señales observadas
con posible error. Luego cada regla decide si protege o no protege. Chile se
modela como una regla amplia de alta sensibilidad: basta uno de tres criterios.
EE.UU. se modela como una regla estricta: exige concurrencia de tres criterios.
Colombia funciona como una abstracción pedagógica intermedia: dos de tres.

La gracia está en mover el parámetro de ruido en datos de terreno. Cuando los
datos técnicos o municipales son imprecisos, una regla amplia puede amplificar
falsos positivos. Eso permite mostrar cómo una incertidumbre técnica puede
convertirse en burocracia, arbitrariedad o bloqueo de proyectos. La app no busca
decir qué país tiene razón, sino hacer visible el trade-off institucional.

## Idea Central

Una ley puede leerse como un algoritmo social. No porque sea software, sino
porque clasifica casos reales usando criterios definidos por una institución.

La pregunta política no es solo "qué protege la ley", sino:

> ¿Qué tipo de error está dispuesta a tolerar una institución?

## Cómo Explicar Cada Caso

Chile:

La regla chilena se representa como una lógica OR o 1 de 3. Esto permite una
alta sensibilidad y reduce el riesgo de dejar fuera humedales reales. El costo
aparece cuando los datos observados tienen ruido: una sola señal equivocada
puede activar protección y producir falsos positivos.

Estados Unidos:

La regla USACE se representa como una lógica AND o 3 de 3. Exige hidrología,
suelo hídrico y vegetación hidrófita. Aumenta la precisión jurídica, pero puede
dejar fuera ecosistemas intermitentes, estacionales o difíciles de observar en
el momento de captura.

Colombia:

La regla colombiana no debe presentarse como una fórmula legal literal. En el
proyecto funciona como una abstracción pedagógica de concurrencia multicriterio,
inspirada en documentos institucionales que combinan dimensiones hidrológicas,
edafológicas, ecológicas y territoriales.

## Cómo Defender El Rigor Legal

Frase útil:

> Las reglas son simplificaciones pedagógicas inspiradas en fuentes oficiales,
> no interpretaciones jurídicas exhaustivas ni herramientas de delimitación real.

Puntos de respaldo:

- Chile está anclado en Ley 21.202 y Decreto 15/2020, especialmente el artículo
  8 del reglamento.
- EE.UU. está anclado en la lógica técnica USACE/EPA de tres parámetros.
- Colombia está documentado como enfoque multicriterio, pero el 2 de 3 es una
  abstracción comparativa.
- Ramsar funciona como marco internacional para entender que los humedales pueden
  ser temporales, artificiales, permanentes o intermitentes.

Si alguien pregunta si "eso es exactamente la ley", responder:

> No. La app traduce criterios oficiales a reglas comparables para observar
> trade-offs. No reemplaza una interpretación legal experta.

## Cómo Explicar Las Métricas

Precision:

De todo lo que la regla protege, cuánto realmente era humedal en la simulación.
En la app aparece como `Acierto al proteger`.

Recall:

De todos los humedales simulados, cuántos logró detectar la regla. En la app
aparece como `Humedales detectados`.

Falsos positivos:

Terrenos protegidos aunque no eran humedal. En política pública representan
costos administrativos, urbanos, sociales o de inversión.

Falsos negativos:

Humedales reales que la regla deja fuera. Representan riesgo de daño ambiental no
prevenido.

## Conexión Con Producto Y Comportamiento

La conexión con producto no es el centro del proyecto, pero sí es un cierre
importante para mi perfil.

En producto digital también diseñamos reglas que clasifican comportamiento:
fraude, scoring, paywalls, moderación, riesgo, elegibilidad o priorización. Si
los datos de tracking tienen ruido y la regla está mal calibrada, aparecen
falsos positivos: usuarios legítimos bloqueados, fricción innecesaria, pérdida de
confianza o churn.

Frase útil:

> Una regla pública mal calibrada puede bloquear desarrollo urbano legítimo; una
> regla de producto mal calibrada puede bloquear usuarios legítimos. En ambos
> casos, el problema es no simular el costo del error.

## Cómo Explicar El Uso De IA

No decir:

> La IA lo hizo.

Decir:

> Usé Codex como copiloto de ejecución en un flujo human-in-the-loop. Yo definí
> la pregunta, el marco conceptual, los supuestos y la interpretación final.
> Codex aceleró la implementación, la documentación, las pruebas y el dossier de
> fuentes.

Punto estratégico:

El proyecto no intenta venderme como programador puro. Muestra que puedo dirigir
herramientas de IA y datos para convertir una pregunta institucional en un
artefacto funcional, documentado y publicable.

## Qué Mostrar En Pantalla

Orden recomendado:

1. App pública:
   `https://humedales-politica-comparada-m4ttyhxjplxfr2zk6e75ai.streamlit.app/`
2. README en GitHub.
3. `docs/legal_sources/README.md`.
4. `src/legal_rules.py`.
5. `src/metrics.py`.
6. `src/data_generator.py`.
7. `tests/test_policy_simulation.py`.

## Preguntas Probables

¿Usa datos reales?

> No. Usa datos sintéticos para aislar el trade-off institucional. El objetivo no
> es diagnosticar humedales reales, sino observar cómo distintas reglas producen
> distintos errores bajo ruido.

¿Es machine learning?

> No entreno un modelo predictivo. Uso métricas de clasificación para evaluar
> reglas legales deterministas como si fueran clasificadores.

¿Cuál regla es mejor?

> No hay una regla ganadora universal. Cada una prioriza un tipo de error. La
> decisión depende del costo social, ambiental, jurídico y territorial que una
> institución esté dispuesta a asumir.

¿Por qué estos tres casos?

> Porque permiten construir una comparación pedagógica entre sensibilidad alta,
> precisión alta y concurrencia intermedia.

¿Qué mejorarías después?

> Incorporaría validación experta, escenarios territoriales más ricos, una versión
> bilingüe de la app y un módulo para asignar costos diferenciales a falsos
> positivos y falsos negativos.

## Cierre Para Entrevista

Este proyecto resume la forma en que quiero trabajar: tomar una pregunta de
ciencia política, traducirla a un problema de datos, construir una herramienta
interactiva y comunicar el resultado de forma entendible para audiencias de
política pública, producto, datos e IA.

No es solo una app. Es una pieza de portafolio sobre cómo pienso reglas,
instituciones, comportamiento y error.
