"""Simplified legal decision rules for comparative policy analysis.

Source mapping and legal caveats are documented in docs/legal_sources/README.md.
"""

from __future__ import annotations

from collections.abc import Callable
import re

import pandas as pd


OBSERVED_CRITERIA = [
    "hidrologia_obs",
    "suelo_hidrico_obs",
    "vegetacion_hidrofita_obs",
]


def ley_chile(row: pd.Series) -> bool:
    """Broad OR rule: one observed criterion is enough."""

    return bool(
        row["hidrologia_obs"] == 1
        or row["suelo_hidrico_obs"] == 1
        or row["vegetacion_hidrofita_obs"] == 1
    )


def ley_eeuu(row: pd.Series) -> bool:
    """Strict AND rule: all three observed criteria must be present."""

    return bool(
        row["hidrologia_obs"] == 1
        and row["suelo_hidrico_obs"] == 1
        and row["vegetacion_hidrofita_obs"] == 1
    )


def ley_colombia(row: pd.Series) -> bool:
    """Intermediate concurrence rule: at least two criteria must be present."""

    return bool(
        row["hidrologia_obs"]
        + row["suelo_hidrico_obs"]
        + row["vegetacion_hidrofita_obs"]
        >= 2
    )


LEGAL_RULES: dict[str, Callable[[pd.Series], bool]] = {
    "Chile: regla amplia (1 de 3)": ley_chile,
    "EE.UU.: regla estricta (3 de 3)": ley_eeuu,
    "Colombia: regla intermedia (2 de 3)": ley_colombia,
}


def apply_legal_rule(data: pd.DataFrame, rule_name: str) -> pd.Series:
    """Apply one rule and return an integer prediction series."""

    if rule_name not in LEGAL_RULES:
        available = ", ".join(LEGAL_RULES)
        raise ValueError(f"Unknown rule '{rule_name}'. Available rules: {available}")

    return data.apply(LEGAL_RULES[rule_name], axis=1).astype(int)


def apply_all_rules(data: pd.DataFrame) -> pd.DataFrame:
    """Return a copy with one prediction column per legal rule."""

    scored = data.copy()
    for rule_name in LEGAL_RULES:
        column_name = prediction_column(rule_name)
        scored[column_name] = apply_legal_rule(scored, rule_name)
    return scored


def prediction_column(rule_name: str) -> str:
    """Create a stable column name from a human-readable rule name."""

    slug = re.sub(r"[^a-z0-9]+", "_", rule_name.lower()).strip("_")
    return f"pred_{slug}"
