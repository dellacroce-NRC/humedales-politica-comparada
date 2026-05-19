"""Metrics for comparing legal rules against the synthetic reference label."""

from __future__ import annotations

import pandas as pd
from sklearn.metrics import confusion_matrix, precision_score, recall_score

from src.legal_rules import LEGAL_RULES, apply_legal_rule


REFERENCE_COLUMN = "humedal_real_simulado"


def compute_rule_metrics(
    data: pd.DataFrame,
    rule_name: str,
    reference_column: str = REFERENCE_COLUMN,
) -> dict[str, float | int | str]:
    """Compute policy-facing metrics for one legal rule."""

    y_true = data[reference_column].astype(int)
    y_pred = apply_legal_rule(data, rule_name)
    tn, fp, fn, tp = confusion_matrix(y_true, y_pred, labels=[0, 1]).ravel()

    return {
        "regla": rule_name,
        "precision": precision_score(y_true, y_pred, zero_division=0),
        "recall": recall_score(y_true, y_pred, zero_division=0),
        "verdaderos_positivos": int(tp),
        "falsos_positivos": int(fp),
        "falsos_negativos": int(fn),
        "verdaderos_negativos": int(tn),
        "casos_protegidos": int(y_pred.sum()),
        "casos_totales": int(len(data)),
    }


def compare_rules(data: pd.DataFrame) -> pd.DataFrame:
    """Compare all available legal rules."""

    return pd.DataFrame(
        [compute_rule_metrics(data, rule_name) for rule_name in LEGAL_RULES]
    )


def noise_sensitivity_curve(
    base_data: pd.DataFrame,
    noise_values: list[float],
    seed: int = 42,
) -> pd.DataFrame:
    """Measure how each rule behaves as field-data noise increases."""

    from src.data_generator import apply_measurement_noise

    rows = []
    for index, noise_level in enumerate(noise_values):
        noisy = apply_measurement_noise(
            base_data,
            noise_level=noise_level,
            seed=seed + index,
        )
        metrics = compare_rules(noisy)
        metrics["nivel_ruido"] = noise_level
        rows.append(metrics)

    return pd.concat(rows, ignore_index=True)

