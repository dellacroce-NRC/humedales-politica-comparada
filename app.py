from __future__ import annotations

import numpy as np
import streamlit as st

from src.data_generator import apply_measurement_noise, generate_base_reality
from src.legal_rules import LEGAL_RULES, apply_all_rules, prediction_column
from src.metrics import compare_rules, compute_rule_metrics, noise_sensitivity_curve
from src.visualization import (
    confusion_matrix_figure,
    false_positive_chart,
    metrics_bar_chart,
    precision_recall_noise_chart,
    territorial_scatter,
)


st.set_page_config(
    page_title="Humedales urbanos como algoritmos sociales",
    layout="wide",
)

st.markdown(
    """
    <style>
    .block-container {padding-top: 1.2rem; padding-bottom: 2rem;}
    [data-testid="stMetricValue"] {font-size: 1.75rem;}
    [data-testid="stMetricLabel"] {font-size: 0.9rem;}
    </style>
    """,
    unsafe_allow_html=True,
)


@st.cache_data(show_spinner=False)
def cached_base_reality(n_cases: int, seed: int):
    return generate_base_reality(n_cases=n_cases, seed=seed)


@st.cache_data(show_spinner=False)
def cached_curve(n_cases: int, seed: int):
    base = generate_base_reality(n_cases=n_cases, seed=seed)
    noise_values = [round(value, 2) for value in np.linspace(0, 0.5, 11)]
    return noise_sensitivity_curve(base, noise_values=noise_values, seed=seed + 100)


st.title("Humedales urbanos como algoritmos sociales")
st.caption(
    "Simulación pedagógica con datos sintéticos para observar cómo distintas "
    "reglas legales clasifican una misma realidad territorial cuando los datos "
    "de terreno son imperfectos."
)

with st.sidebar:
    st.header("Escenario")
    selected_rule = st.selectbox("Criterio legal simulado", list(LEGAL_RULES.keys()))
    n_cases = st.slider("Terrenos simulados", 300, 5_000, 1_200, step=100)
    noise_percent = st.slider("Error en datos de terreno", 0, 50, 15, step=1)
    noise_level = noise_percent / 100
    compare_all = st.toggle("Mostrar comparacion entre reglas", value=True)

    with st.expander("Opciones técnicas"):
        seed = st.number_input(
            "Escenario reproducible",
            min_value=1,
            max_value=9999,
            value=42,
            step=1,
        )

base_data = cached_base_reality(n_cases=n_cases, seed=seed)
data = apply_measurement_noise(base_data, noise_level=noise_level, seed=seed + 1)
scored = apply_all_rules(data)
metrics_df = compare_rules(data)
selected_metrics = compute_rule_metrics(data, selected_rule)
selected_prediction = prediction_column(selected_rule)

st.markdown(
    """
    Una ley también puede leerse como un clasificador: observa señales, aplica
    una regla y produce una decisión pública. En esta simulación, cada punto es
    un terreno. Primero existe una realidad sintética; luego aparecen datos de
    terreno con error; finalmente, cada legislación decide si protege o no
    protege.
    """
)

with st.expander("Cómo leer el dilema comparado", expanded=True):
    st.markdown(
        """
        - **Chile: lógica OR / 1 de 3.** Alta sensibilidad institucional:
          prioriza no dejar humedales fuera, pero puede transformar datos
          ruidosos en falsos positivos y bloqueo administrativo.
        - **EE.UU.: lógica AND / 3 de 3.** Alta precisión jurídica:
          protege solo con evidencia concurrente, pero puede dejar sin
          protección ecosistemas intermitentes o estacionales.
        - **Colombia: lógica 2 de 3.** Concurrencia intermedia:
          busca equilibrar protección ambiental, certeza técnica y resiliencia
          institucional.
        """
    )

metric_cols = st.columns(4)
with metric_cols[0]:
    st.metric("Acierto al proteger", f"{selected_metrics['precision']:.1%}")
    st.caption("De cada 100 terrenos protegidos, cuántos sí eran humedal.")
with metric_cols[1]:
    st.metric("Humedales detectados", f"{selected_metrics['recall']:.1%}")
    st.caption("De cada 100 humedales, cuántos logra encontrar la regla.")
with metric_cols[2]:
    st.metric("Protege de más", f"{selected_metrics['falsos_positivos']:,}")
    st.caption("Terrenos protegidos aunque no eran humedal en la simulación.")
with metric_cols[3]:
    st.metric("Deja fuera humedales", f"{selected_metrics['falsos_negativos']:,}")
    st.caption("Humedales simulados que la regla no protege.")

left, right = st.columns([1, 1])
with left:
    st.subheader("Mapa de aciertos y errores")
    st.plotly_chart(confusion_matrix_figure(selected_metrics), width="stretch")
    st.caption(
        "Las casillas muestran cuatro resultados: acertar al proteger, acertar al "
        "no proteger, proteger de más o dejar humedales fuera."
    )
with right:
    st.subheader("Terrenos simulados")
    st.plotly_chart(
        territorial_scatter(scored, selected_prediction, selected_rule),
        width="stretch",
    )
    st.caption(
        "Cada punto es un terreno. El eje vertical muestra cuántas señales de "
        "humedal se observaron: 0, 1, 2 o 3. La zona sombreada marca desde "
        "cuántas señales protege la regla seleccionada."
    )

if compare_all:
    st.subheader("Qué gana y qué pierde cada regla")
    st.plotly_chart(metrics_bar_chart(metrics_df), width="stretch")
    st.caption(
        "Acierto al proteger mide calidad de la decisión. Humedales detectados "
        "mide cobertura ambiental."
    )

st.subheader("Qué pasa cuando los datos vienen con error")
curve_df = cached_curve(n_cases=n_cases, seed=seed)
curve_left, curve_right = st.columns([1, 1])
with curve_left:
    st.plotly_chart(false_positive_chart(curve_df), width="stretch")
    st.caption(
        "Si sube el error de medición, las reglas amplias tienden a proteger "
        "más casos que no eran humedal en la simulación."
    )
with curve_right:
    st.plotly_chart(precision_recall_noise_chart(curve_df), width="stretch")
    st.caption(
        "Las líneas muestran el intercambio: proteger mucho puede bajar el "
        "acierto, y ser muy estricto puede bajar la cobertura."
    )

st.info(
    "Lectura clave: una regla no solo define qué se protege; también define qué "
    "tipo de error acepta. Una regla amplia reduce el riesgo de dejar humedales "
    "fuera, pero aumenta el riesgo de proteger de más cuando los datos tienen error."
)

st.markdown(
    """
    **Coda analítica.** Aunque el caso es de política comparada, el mismo
    lenguaje de precision/recall aparece en producto digital: fraude, paywalls,
    scoring, moderación o reglas de negocio. Cuando los datos de comportamiento
    tienen ruido, una regla mal calibrada puede bloquear usuarios legítimos del
    mismo modo en que una ley mal calibrada puede paralizar proyectos urbanos
    legítimos.
    """
)
