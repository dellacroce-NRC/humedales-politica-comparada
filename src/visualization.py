"""Plotly visualizations for the Streamlit case study."""

from __future__ import annotations

import pandas as pd
import plotly.express as px
import plotly.graph_objects as go


COLOR_MAP = {
    "Chile: regla amplia (1 de 3)": "#D1495B",
    "EE.UU.: regla estricta (3 de 3)": "#00798C",
    "Colombia: regla intermedia (2 de 3)": "#EDA92F",
}

METRIC_LABELS = {
    "precision": "Acierto al proteger",
    "recall": "Humedales detectados",
}

RESULT_COLOR_MAP = {
    "Acierto: protege humedal": "#2A9D8F",
    "Protege de más": "#E76F51",
    "Deja fuera humedal": "#9B5DE5",
    "Acierto: no protege": "#6C757D",
}

RULE_THRESHOLDS = {
    "Chile: regla amplia (1 de 3)": 1,
    "EE.UU.: regla estricta (3 de 3)": 3,
    "Colombia: regla intermedia (2 de 3)": 2,
}


def metrics_bar_chart(metrics_df: pd.DataFrame) -> go.Figure:
    """Compare precision and recall across rules with reader-friendly labels."""

    long = metrics_df.melt(
        id_vars="regla",
        value_vars=["precision", "recall"],
        var_name="metrica",
        value_name="valor",
    )
    long["indicador"] = long["metrica"].map(METRIC_LABELS)

    fig = px.bar(
        long,
        x="regla",
        y="valor",
        color="indicador",
        barmode="group",
        text=long["valor"].map(lambda value: f"{value:.0%}"),
        color_discrete_map={
            "Acierto al proteger": "#355070",
            "Humedales detectados": "#2A9D8F",
        },
    )
    fig.update_layout(
        yaxis_tickformat=".0%",
        yaxis_title="Porcentaje",
        xaxis_title="Regla simulada",
        legend_title="Indicador",
        margin=dict(l=20, r=20, t=35, b=20),
    )
    return fig


def false_positive_chart(curve_df: pd.DataFrame) -> go.Figure:
    """Show how over-protection changes with measurement error."""

    fig = px.line(
        curve_df,
        x="nivel_ruido",
        y="falsos_positivos",
        color="regla",
        markers=True,
        color_discrete_map=COLOR_MAP,
    )
    fig.update_layout(
        xaxis_tickformat=".0%",
        xaxis_title="Error en datos de terreno",
        yaxis_title="Casos protegidos de más",
        legend_title="Regla simulada",
        margin=dict(l=20, r=20, t=35, b=20),
    )
    return fig


def precision_recall_noise_chart(curve_df: pd.DataFrame) -> go.Figure:
    """Show accuracy and detection coverage under rising measurement error."""

    long = curve_df.melt(
        id_vars=["regla", "nivel_ruido"],
        value_vars=["precision", "recall"],
        var_name="metrica",
        value_name="valor",
    )
    long["indicador"] = long["metrica"].map(METRIC_LABELS)

    fig = px.line(
        long,
        x="nivel_ruido",
        y="valor",
        color="regla",
        line_dash="indicador",
        color_discrete_map=COLOR_MAP,
    )
    fig.update_layout(
        xaxis_tickformat=".0%",
        yaxis_tickformat=".0%",
        xaxis_title="Error en datos de terreno",
        yaxis_title="Porcentaje",
        legend_title="Regla e indicador",
        margin=dict(l=20, r=20, t=35, b=20),
    )
    return fig


def confusion_matrix_figure(metrics: dict[str, float | int | str]) -> go.Figure:
    """Create a compact human-readable map of hits and errors."""

    z = [
        [metrics["verdaderos_negativos"], metrics["falsos_positivos"]],
        [metrics["falsos_negativos"], metrics["verdaderos_positivos"]],
    ]
    text = [
        ["Acierto<br>No protege", "Protege<br>de más"],
        ["Deja fuera<br>humedal", "Acierto<br>Protege"],
    ]
    fig = go.Figure(
        data=go.Heatmap(
            z=z,
            text=[
                [
                    f"{label}<br>{value}"
                    for label, value in zip(text_row, value_row, strict=True)
                ]
                for text_row, value_row in zip(text, z, strict=True)
            ],
            texttemplate="%{text}",
            colorscale=[[0, "#F7F7F2"], [1, "#2A9D8F"]],
            showscale=False,
        )
    )
    fig.update_layout(
        xaxis=dict(
            title="Decisión de la regla",
            tickmode="array",
            tickvals=[0, 1],
            ticktext=["No protege", "Protege"],
        ),
        yaxis=dict(
            title="Realidad simulada",
            tickmode="array",
            tickvals=[0, 1],
            ticktext=["No humedal", "Humedal"],
            autorange="reversed",
        ),
        margin=dict(l=20, r=20, t=20, b=20),
        height=320,
    )
    return fig


def territorial_scatter(
    data: pd.DataFrame,
    prediction_column: str,
    rule_name: str,
) -> go.Figure:
    """Map simulated cases by urban pressure and observed environmental signal."""

    plot_data = data.copy()
    actual = plot_data["humedal_real_simulado"]
    predicted = plot_data[prediction_column]

    plot_data["resultado"] = "Acierto: no protege"
    plot_data.loc[(actual == 1) & (predicted == 1), "resultado"] = (
        "Acierto: protege humedal"
    )
    plot_data.loc[(actual == 0) & (predicted == 1), "resultado"] = "Protege de más"
    plot_data.loc[(actual == 1) & (predicted == 0), "resultado"] = (
        "Deja fuera humedal"
    )
    plot_data["senales_observadas"] = plot_data["criterios_observados"]

    fig = px.scatter(
        plot_data,
        x="presion_urbana",
        y="senales_observadas",
        color="resultado",
        opacity=0.72,
        color_discrete_map=RESULT_COLOR_MAP,
        hover_data={
            "presion_urbana": ":.0f",
            "senales_observadas": True,
            "criterios_observados": True,
            "humedal_real_simulado": True,
        },
        labels={
            "presion_urbana": "Presión urbana simulada",
            "senales_observadas": "Cantidad de señales observadas",
            "resultado": "Resultado",
            "humedal_real_simulado": "Humedal simulado",
            "criterios_observados": "Criterios observados",
        },
    )
    threshold = RULE_THRESHOLDS.get(rule_name)
    if threshold is not None:
        fig.add_hrect(
            y0=threshold - 0.45,
            y1=3.45,
            fillcolor="#2A9D8F",
            opacity=0.08,
            line_width=0,
            annotation_text=f"Protege desde {threshold} de 3",
            annotation_position="top left",
        )
        fig.add_hline(
            y=threshold - 0.5,
            line_dash="dash",
            line_color="#ADB5BD",
            line_width=1,
        )
    fig.update_layout(
        yaxis=dict(
            tickmode="array",
            tickvals=[0, 1, 2, 3],
            ticktext=["0 de 3", "1 de 3", "2 de 3", "3 de 3"],
            range=[-0.45, 3.45],
            title="Cantidad de señales observadas",
        ),
        legend_title="Resultado",
        margin=dict(l=20, r=20, t=35, b=20),
    )
    return fig
