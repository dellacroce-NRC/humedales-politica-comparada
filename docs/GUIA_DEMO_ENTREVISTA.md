# Guía Para Explicar El Proyecto En Entrevistas

Esta guía es para presentar el proyecto en vivo: abrir GitHub, navegar el
repositorio, explicar la app y conectar el trabajo con tu perfil profesional.
Está pensada para una entrevista, una conversación de portafolio o una revisión
rápida por pantalla compartida.

## Versión corta: 45 segundos

Si tienes poco tiempo, puedes decir:

> Este proyecto convierte una pregunta de política comparada en una simulación
> interactiva. La idea es tratar una ley como si fuera un clasificador: observa
> señales, aplica una regla y decide si protege o no protege un territorio.
> Comparo tres lógicas institucionales: una regla amplia tipo Chile, una regla
> estricta tipo EE.UU. y una regla intermedia tipo Colombia. Luego introduzco
> ruido en los datos de terreno para mostrar cómo cambian los falsos positivos y
> falsos negativos. Lo construí con Python, Streamlit y apoyo de Codex como
> agente de IA, usando un flujo de Vibe Coding dirigido por criterio analítico.

## Versión de entrevista: 2 minutos

Una explicación más completa:

> Mi objetivo no era hacer un dashboard tradicional, sino construir una pieza
> pedagógica para mostrar un trade-off de política pública. Una ley ambiental
> puede entenderse como una regla de decisión: toma datos observados y clasifica
> casos. El problema es que los datos de terreno pueden ser imperfectos.
>
> Entonces comparé tres reglas simplificadas. Chile funciona como una lógica OR:
> basta una señal de humedal. Eso maximiza recall y reduce el riesgo de dejar
> humedales fuera, pero puede generar falsos positivos si los datos son ruidosos.
> EE.UU. funciona como lógica AND: exige tres señales, lo que aumenta precisión
> jurídica pero puede dejar ecosistemas intermitentes sin protección. Colombia
> queda como modelo intermedio de concurrencia.
>
> Lo interesante es que el experimento permite mover el nivel de error en los
> datos y ver cómo la regla amplia amplifica ese ruido. Ahí aparece el punto
> político: un problema técnico de medición puede convertirse en arbitrariedad
> burocrática y bloqueo de proyectos.
>
> También lo conecto con producto digital solo al final: reglas de fraude,
> paywalls o scoring enfrentan el mismo dilema de precision y recall. Si no
> medimos falsos positivos, podemos dañar usuarios legítimos. Esa conexión
> muestra cómo mi formación en ciencia política puede dialogar con datos,
> comportamiento y producto.

## Orden recomendado para mostrar el repositorio

### 1. Abrir el README

Qué mostrar:

- Título: `Urban Wetlands as Social Algorithms`.
- Primeros párrafos.
- Capturas de la app.
- Tabla de las tres reglas comparadas.

Qué decir:

> El README está en inglés porque mi portafolio apunta a audiencias
> internacionales. La app queda en español porque el caso dialoga con política
> pública chilena y latinoamericana. Eso también muestra contexto: no estoy
> ocultando el origen territorial del problema, sino haciéndolo legible para una
> audiencia más amplia.

Idea clave:

> Este no es solo un repositorio técnico. Es la pieza narrativa del proyecto:
> explica el problema, el experimento y por qué importa.

### 2. Mostrar la app desplegada o local

Si la app está en Streamlit Cloud, abre la URL pública. Si no, puedes correr:

```powershell
python -m streamlit run app.py
```

Qué mostrar:

- Selector de criterio legal.
- Slider de terrenos simulados.
- Slider de error en datos de terreno.
- Métricas: `Acierto al proteger`, `Humedales detectados`, `Protege de más`,
  `Deja fuera humedales`.
- Gráficos de matriz de confusión y sensibilidad al ruido.

Qué decir:

> Lo importante es que la persona puede cambiar la regla y el nivel de ruido. No
> le estoy mostrando un resultado fijo, sino una forma de pensar el trade-off.

Cómo explicar las métricas:

- `Acierto al proteger`: equivalente a precision.
- `Humedales detectados`: equivalente a recall.
- `Protege de más`: falsos positivos.
- `Deja fuera humedales`: falsos negativos.

Frase útil:

> Precision y recall dejan de ser métricas abstractas. Acá se vuelven decisiones
> de política pública: qué error acepta el Estado y quién paga el costo.

### 3. Abrir `src/legal_rules.py`

Qué mostrar:

- `ley_chile`: lógica OR.
- `ley_eeuu`: lógica AND.
- `ley_colombia`: al menos 2 criterios.

Qué decir:

> Este archivo es el corazón conceptual del proyecto. Cada regla legal está
> traducida a una función simple. Esa simplicidad es deliberada: permite comparar
> reglas institucionales como clasificadores deterministas.

No profundizar demasiado en código. El objetivo no es demostrar sintaxis, sino
mostrar que el diseño institucional fue convertido en una estructura evaluable.

### 4. Abrir `src/metrics.py`

Qué mostrar:

- `compute_rule_metrics`.
- Precision, recall, falsos positivos, falsos negativos.
- `noise_sensitivity_curve`.

Qué decir:

> Acá evalúo cada regla contra una referencia sintética. Lo importante es que no
> entrené un modelo predictivo. Traté reglas legales fijas como clasificadores y
> medí qué errores producen.

Frase útil:

> Es una traducción entre lenguajes: de derecho y política pública a ciencia de
> datos.

### 5. Abrir `src/data_generator.py`

Qué mostrar:

- Generación de realidad sintética.
- Aplicación de ruido de medición.
- Columnas observadas con `_obs`.

Qué decir:

> Como no estoy clasificando humedales reales, genero un territorio sintético. Lo
> importante es separar la realidad simulada de los datos observados. Esa
> diferencia permite modelar un problema muy real: los datos institucionales no
> siempre son limpios.

Idea clave:

> El proyecto no depende de datos reales porque es una simulación pedagógica. Eso
> permite aislar el trade-off y comunicarlo mejor.

### 6. Abrir `tests/test_policy_simulation.py`

Qué mostrar:

- Tests de ruido.
- Tests de reglas.
- Tests de métricas.

Qué decir:

> Incluí pruebas básicas porque, aunque el proyecto sea pedagógico, necesitaba
> asegurar que las reglas y métricas respondieran de forma consistente. Eso le da
> trazabilidad al análisis.

Frase útil:

> No es solo una visualización bonita; hay una lógica validada detrás.

### 7. Abrir `docs/GUIA_EXPLICACION_LINKEDIN.md`

Qué mostrar:

- Guion breve.
- Explicación de IA agentica.
- Puente con producto.

Qué decir:

> Este archivo lo uso como material de comunicación. Me ayuda a traducir el
> proyecto para LinkedIn o para una conversación no técnica.

## Cómo explicar el uso de IA sin sonar dependiente

Evita decir:

> Lo hizo la IA.

Mejor decir:

> Lo construí con apoyo de Codex en un flujo human-in-the-loop. Yo definí la
> pregunta, el marco comparado, los supuestos y la interpretación. Codex ayudó a
> acelerar la implementación, ordenar el código, generar pruebas y mejorar la
> documentación.

Otra formulación:

> Mi valor no está en escribir cada línea manualmente, sino en saber dirigir una
> herramienta de IA para convertir una pregunta analítica en un artefacto
> funcional, revisable y publicable.

## Cómo conectar con tu perfil profesional

Puedes resumirlo así:

> Este proyecto junta tres partes de mi perfil: ciencia política comparada,
> ciencia de datos aplicada e inteligencia artificial para construir prototipos
> explicables. Además, permite conectar el análisis institucional con producto y
> comportamiento, porque en ambos mundos diseñamos reglas que clasifican personas
> o casos bajo datos imperfectos.

Para una organización pública o internacional:

> Muestra capacidad para traducir dilemas institucionales en herramientas
> analíticas comprensibles.

Para una empresa o equipo de producto:

> Muestra capacidad para razonar sobre reglas, errores, incentivos y efectos en
> usuarios o actores reales.

Para un rol de datos:

> Muestra capacidad para estructurar una simulación, construir métricas y
> comunicar resultados sin perder el contexto del problema.

## Preguntas que podrían hacerte

### ¿Esto usa datos reales?

Respuesta:

> No. Usa datos sintéticos porque el objetivo no es diagnosticar humedales
> reales, sino aislar y explicar un trade-off institucional. Eso permite controlar
> el nivel de ruido y comparar reglas de forma transparente.

### ¿Entrenaste un modelo de machine learning?

Respuesta:

> No. Y esa es parte de la gracia. Las reglas legales funcionan como
> clasificadores deterministas. Uso métricas de machine learning para evaluarlas,
> pero no entreno un modelo predictivo.

### ¿Por qué Chile, EE.UU. y Colombia?

Respuesta:

> Porque permiten representar tres lógicas institucionales distintas: regla
> amplia, regla estricta y regla intermedia. La comparación es pedagógica, no una
> reconstrucción jurídica exhaustiva.

### ¿Cuál regla es mejor?

Respuesta:

> El proyecto no busca declarar una regla ganadora. Busca mostrar que cada regla
> acepta un tipo de error distinto. La mejor regla depende del costo social,
> ambiental y jurídico que una institución esté dispuesta a asumir.

### ¿Cuál fue el rol de la IA?

Respuesta:

> La IA fue un acelerador técnico. Me permitió pasar de una intuición analítica a
> una app funcional, pero el criterio de diseño, la pregunta y la interpretación
> fueron humanos.

### ¿Qué mejorarías en una siguiente versión?

Respuesta:

> Incorporaría fuentes normativas primarias, escenarios territoriales más ricos,
> validación con expertos y quizá una versión bilingüe de la app. También podría
> agregar un módulo para comparar reglas con distintos costos sociales asignados
> a falsos positivos y falsos negativos.

## Cierre recomendado

Para cerrar una demo:

> Para mí, este proyecto resume una forma de trabajar: tomar una pregunta
> institucional, traducirla a datos, construir una herramienta interactiva y usar
> IA para acelerar la ejecución sin perder criterio analítico. Es una pieza de
> portafolio, pero también una muestra de cómo quiero trabajar: conectando
> política pública, comportamiento, datos y tecnología.
