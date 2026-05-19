# Humedales urbanos como algoritmos sociales

Simulación interactiva en Python + Streamlit sobre política comparada, datos
imperfectos y toma de decisiones públicas.

Este proyecto muestra cómo una ley puede leerse como un clasificador: observa
señales, aplica una regla y produce una decisión. No busca determinar dónde hay
humedales reales ni reemplazar análisis jurídico experto. Su objetivo es hacer
visible un dilema institucional: ninguna regla es perfecta; toda regla distribuye
errores.

La pieza fue diseñada como parte de un portafolio profesional que conecta ciencia
política, ciencia de datos e inteligencia artificial aplicada. El foco no está
solo en programar una app, sino en traducir un problema de política pública a una
simulación explicable, medible y comunicable.

## Idea central

Una legislación ambiental puede funcionar como un algoritmo social. Recibe datos
de terreno, aplica criterios y decide si un sitio queda protegido o no. El
problema aparece cuando los datos son imperfectos: una regla amplia puede evitar
daño ambiental irreversible, pero también puede amplificar errores técnicos y
generar bloqueos injustificados.

La pregunta del proyecto no es qué país tiene la regla "correcta". La pregunta
es qué tipo de error acepta cada diseño institucional.

## Tres reglas comparadas

| Caso | Regla simulada | Sesgo institucional | Riesgo principal |
|---|---:|---|---|
| Chile | 1 de 3 criterios | Alta sensibilidad / high recall | Falsos positivos: proteger de más |
| EE.UU. | 3 de 3 criterios | Alta precisión jurídica | Falsos negativos: dejar humedales fuera |
| Colombia | 2 de 3 criterios | Concurrencia intermedia | Balance imperfecto entre ambos errores |

### Chile: lógica OR / 1 de 3

La regla amplia está diseñada para evitar a toda costa el daño ambiental
irreversible. En lenguaje de clasificación, maximiza sensibilidad o recall:
prefiere detectar casi todo antes que arriesgarse a dejar un humedal fuera.

El costo es que, si los datos técnicos o municipales tienen ruido, una sola señal
errónea puede activar protección. En la práctica, eso puede traducirse en falsos
positivos: sitios eriazos o terrenos sin valor ecosistémico bloqueados por error,
con efectos sobre vivienda, inversión pública o gestión urbana.

### EE.UU.: lógica AND / 3 de 3

La regla estricta exige concurrencia completa de criterios. Su prioridad es la
certeza jurídica y la protección de la propiedad privada: solo se protege cuando
la evidencia observada es fuerte.

El costo aparece por el lado contrario. Al exigir demasiada evidencia, puede
dejar fuera ecosistemas intermitentes, estacionales o difíciles de observar. En
términos de matriz de confusión, reduce falsos positivos, pero aumenta falsos
negativos.

### Colombia: lógica 2 de 3

La regla intermedia busca una solución de concurrencia: no basta una señal
aislada, pero tampoco se exige la presencia perfecta de todos los criterios. Es
un intento de equilibrio institucional entre protección ambiental, certeza
técnica y resiliencia frente a datos imperfectos.

## El experimento: ruido en datos de terreno

La app permite modificar el nivel de "error en datos de terreno". Ese control es
clave para el argumento del proyecto.

Cuando los datos observados tienen ruido, la regla amplia de Chile no solo se
vuelve más sensible: puede amplificar el error de forma no lineal. Un problema
de medición se convierte entonces en un problema de burocracia: la incertidumbre
técnica termina produciendo arbitrariedad administrativa y parálisis de
proyectos.

Esta es la hipótesis pedagógica más importante del proyecto: el diseño de reglas
no puede evaluarse sin simular la calidad de los datos sobre los que esas reglas
van a operar.

## Cómo leer las métricas

| Métrica en la app | Equivalente técnico | Lectura de política pública |
|---|---|---|
| Acierto al proteger | Precision | De lo que el Estado protege, cuánto correspondía proteger |
| Humedales detectados | Recall | De los humedales existentes, cuántos logra encontrar la regla |
| Protege de más | Falsos positivos | Costos administrativos, urbanos o sociales por sobrerregulación |
| Deja fuera humedales | Falsos negativos | Riesgo de daño ambiental no prevenido |

La matriz de confusión permite ver que una regla legal no solo produce
decisiones correctas o incorrectas. Produce tipos distintos de error, y cada
tipo de error tiene consecuencias políticas, sociales y territoriales.

## Coda: de política pública a producto digital

El proyecto no es un caso de product analytics. Su núcleo es la política
comparada. Pero la lógica de precision/recall permite una lectura transferible
al diseño de productos digitales, especialmente para equipos que toman
decisiones automatizadas sobre comportamiento humano.

Sistemas de prevención de fraude, paywalls, moderación, scoring de riesgo o
reglas de negocio también clasifican comportamientos con datos imperfectos.

Si los datos de tracking tienen ruido y una regla es demasiado agresiva, los
falsos positivos pueden bloquear usuarios legítimos, destruir confianza o
empujar abandono. Es el equivalente analítico de una ley mal calibrada que
asfixia proyectos urbanos por tratar como riesgo casos que no lo eran.

La conexión no busca cambiar el tema del proyecto, sino mostrar una capacidad
profesional más amplia: razonar reglas, incentivos, comportamiento y error tanto
en instituciones públicas como en productos digitales. Para un equipo de
producto, esa mirada importa porque muchas decisiones operativas también son
clasificadores: quién pasa un filtro, quién recibe una fricción, quién queda
bloqueado, quién accede a una experiencia y quién es tratado como riesgo.

Esa es la transferencia central: una formación en ciencia política puede aportar
criterio para diseñar sistemas de decisión más conscientes de sus costos,
sesgos, falsos positivos y efectos sobre personas reales.

## Qué demuestra este proyecto

- Capacidad para traducir un problema de ciencia política a una simulación de
  datos reproducible.
- Uso de métricas de clasificación para explicar trade-offs de política pública.
- Diseño de una app interactiva orientada a comunicación ejecutiva y pedagógica.
- Capacidad para conectar dilemas institucionales con criterios transferibles a
  producto, comportamiento y reglas de decisión.
- Capacidad para comunicar análisis complejo a audiencias mixtas: política
  pública, datos, IA, producto y negocio.
- Integración de Python, Streamlit, Plotly, pruebas automatizadas y documentación.
- Uso de IA agentica como apoyo de desarrollo en un flujo human-in-the-loop.

## Rol de la inteligencia artificial

OpenAI Codex fue usado como agente técnico para acelerar arquitectura,
implementación, visualizaciones, pruebas y documentación. El criterio
politológico, el encuadre comparado, la interpretación de resultados y el tono
de la pieza fueron definidos humanamente.

El punto no es delegar pensamiento experto a la IA. El punto es usar IA aplicada
para convertir una pregunta institucional en un prototipo explicable, testeable y
publicable.

## Estructura del proyecto

```text
Humedales_Politica_Comparada/
|-- app.py
|-- README.md
|-- requirements.txt
|-- requirements-dev.txt
|-- data/
|   `-- synthetic_wetlands.csv
|-- docs/
|   |-- GUIA_EXPLICACION_LINKEDIN.md
|   `-- deploy_log.md
|-- notebooks/
|   `-- 01_exploracion_conceptual.ipynb
|-- src/
|   |-- data_generator.py
|   |-- legal_rules.py
|   |-- metrics.py
|   `-- visualization.py
`-- tests/
    `-- test_policy_simulation.py
```

## Ejecutar localmente

```powershell
python -m pip install -r requirements.txt
python -m streamlit run app.py
```

Luego abrir:

```text
http://localhost:8501
```

## Ejecutar pruebas

```powershell
python -m pip install -r requirements-dev.txt
$env:PYTHONDONTWRITEBYTECODE='1'
python -m pytest tests -q -p no:cacheprovider
```

## Limitaciones

- Dataset sintético, no evidencia geográfica real.
- Reglas legales simplificadas con fines pedagógicos.
- No es un clasificador científico, jurídico ni productivo.
- La fidelidad normativa puede ampliarse con fuentes primarias y validación
  experta.

## Estado de publicación

- Repositorio esperado: `dellacroce-NRC/humedales-politica-comparada`
- App en Streamlit Cloud: pendiente de despliegue
- Uso previsto: portafolio profesional, LinkedIn y entrevistas
