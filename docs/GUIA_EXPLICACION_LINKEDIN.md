# Guía De Explicación Para LinkedIn Y Entrevistas

## Frase corta del proyecto

Esta app muestra cómo una misma realidad territorial puede producir decisiones
públicas distintas según la regla legal que se use y según la calidad de los
datos de terreno.

También muestra una forma concreta de usar IA agentica: partir desde una
pregunta de ciencia política y convertirla en una aplicación interactiva con
apoyo de Codex como agente técnico.

## Explicación en simple

Imagina que tenemos muchos terrenos. Algunos son humedales y otros no. Como el
objetivo no es diagnosticar territorios reales, construimos una realidad
sintética para observar cómo se comportan distintas reglas.

Después hacemos algo parecido a lo que ocurre en la vida real: los datos de
terreno pueden venir con errores. A eso le llamamos "error en datos de terreno".

Luego aplicamos tres formas de decidir:

- Chile: una regla amplia protege con una sola señal.
- EE.UU.: una regla estricta protege solo con tres señales.
- Colombia: una regla intermedia protege con dos señales.

La pregunta no es cuál regla es perfecta. La pregunta es qué tipo de error
produce cada regla y qué costo institucional acepta.

## Cómo explicar los indicadores

- **Acierto al proteger:** cuando la regla protege un terreno, qué tan seguido
  acierta.
- **Humedales detectados:** de todos los humedales simulados, cuántos logra
  encontrar.
- **Protege de más:** terrenos que la regla protege aunque no eran humedal en la
  simulación.
- **Deja fuera humedales:** terrenos que eran humedal en la simulación, pero la
  regla no protege.

## Cómo explicar las visualizaciones

### Mapa de aciertos y errores

Es una tabla de cuatro resultados posibles:

- Acertó al proteger.
- Acertó al no proteger.
- Protegió de más.
- Dejó fuera un humedal.

Sirve para mostrar que toda regla tiene costos.

### Terrenos simulados

Cada punto es un terreno. Mientras más arriba está, más señales de humedal
aparecieron en los datos observados. El color muestra si la regla acertó o se
equivocó.

Sirve para volver visible que no todos los errores ocurren en el mismo tipo de
territorio.

### Qué gana y qué pierde cada regla

Compara dos cosas:

- Acierto al proteger.
- Humedales detectados.

Si una regla detecta muchos humedales, puede proteger de más. Si una regla es
muy estricta, puede equivocarse menos al proteger, pero también dejar humedales
fuera.

### Qué pasa cuando los datos vienen con error

Muestra que la calidad de los datos importa. Si aumenta el error de medición,
una regla amplia puede empezar a proteger muchos casos que no eran humedal en la
simulación.

## Explicación sobre machine learning

No entrené un modelo. Esto es importante.

Lo que hice fue tratar cada regla legal como si fuera un clasificador:

```text
datos observados + regla legal = decisión
```

Después usé métricas comunes de machine learning para evaluar esas decisiones.
Esas métricas ayudan a traducir un problema de política pública a una pregunta
medible: qué errores produce cada regla.

## Cómo explicar el uso de IA agentica

Este proyecto fue construido con un flujo human-in-the-loop. El criterio
politológico, la pregunta de investigación y el encuadre pedagógico fueron
humanos. Codex apoyó como agente de programación para transformar esa idea en
código, visualizaciones, pruebas y documentación.

Una forma simple de decirlo:

```text
criterio político + ciencia de datos + IA agentica = prototipo explicable
```

La IA no reemplaza el análisis político. Acelera la construcción técnica para
que una idea pueda convertirse en una pieza pública, visual e interactiva.

## Guion breve para presentarlo

Este proyecto no busca decir dónde hay humedales reales. Es una simulación para
explicar algo más general: el diseño de una ley importa.

Si una ley usa una regla muy amplia, puede detectar más humedales, pero también
puede proteger de más cuando los datos no son perfectos. Si usa una regla muy
estricta, puede evitar algunos errores administrativos, pero también puede dejar
ecosistemas fuera.

La gracia del ejercicio es mostrar que Precision y Recall no son solo métricas
técnicas. También pueden leerse como dilemas de política pública. Y, al mismo
tiempo, muestra cómo herramientas de IA agentica pueden ayudar a convertir una
pregunta institucional en una aplicación de ciencia de datos.

## Versión para entrevista

Lo presentaría así:

> Construí una simulación para mostrar cómo una ley ambiental puede entenderse
> como un clasificador. Comparé tres diseños institucionales: una regla amplia,
> una estricta y una intermedia. Luego introduje ruido en los datos de terreno
> para observar cómo cambian los falsos positivos y falsos negativos. Lo
> interesante es que el problema no es solo técnico: cada error representa un
> costo de política pública. Y esa misma lógica aplica a producto digital,
> fraude, paywalls o reglas de negocio, donde una mala calibración puede dañar
> experiencia de usuario.

## Puente con perfil profesional

Este proyecto sirve para posicionar tres capacidades juntas:

- Análisis de política comparada con lenguaje institucional.
- Ciencia de datos aplicada para simular, medir y visualizar trade-offs.
- Uso práctico de IA para acelerar prototipos explicables sin perder criterio
  experto.

La conexión con producto debe aparecer como cierre, no como tema principal. Una
buena formulación sería:

> Aunque el caso es de política pública, la lógica viaja bien al mundo producto:
> cuando diseñamos reglas sobre datos de comportamiento, también estamos
> decidiendo cuántos falsos positivos y falsos negativos aceptamos. Si no
> medimos ese trade-off, una regla puede proteger el sistema, pero dañar la
> experiencia de usuarios legítimos.

Para entrevistas con reclutadores de empresas, el punto no es decir "este es un
proyecto de producto", sino algo más fino:

> Este proyecto muestra cómo razono sistemas de decisión. En política pública,
> una regla legal decide qué se protege y qué queda fuera. En producto, una regla
> de negocio decide qué usuario recibe fricción, qué transacción se bloquea o qué
> comportamiento se considera riesgo. En ambos casos, el desafío no es solo
> optimizar una métrica, sino entender el costo humano e institucional de los
> falsos positivos y falsos negativos.
