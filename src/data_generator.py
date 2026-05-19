"""Synthetic data generation for the urban wetlands policy simulation.

The dataset is intentionally synthetic. Its purpose is to show how a legal
decision rule reacts when field data are imperfect, not to model real wetlands.
"""

from __future__ import annotations

from pathlib import Path

import numpy as np
import pandas as pd


CRITERIA = ["hidrologia", "suelo_hidrico", "vegetacion_hidrofita"]


def _sigmoid(values: np.ndarray) -> np.ndarray:
    return 1 / (1 + np.exp(-values))


def generate_base_reality(n_cases: int = 1_000, seed: int = 42) -> pd.DataFrame:
    """Create the unobserved synthetic territorial reality.

    `humedal_real_simulado` is the pedagogical reference label against which the
    legal rules are evaluated. It is not changed by measurement noise.
    """

    rng = np.random.default_rng(seed)

    x_coord = rng.uniform(0, 100, n_cases)
    y_coord = rng.uniform(0, 100, n_cases)

    water_gradient = _sigmoid((58 - y_coord) / 11)
    soil_gradient = _sigmoid((x_coord - 38) / 13)
    vegetation_gradient = _sigmoid((70 - np.abs(x_coord - y_coord)) / 16)

    hidrologia_prob = np.clip(0.20 + 0.65 * water_gradient, 0, 1)
    suelo_prob = np.clip(0.15 + 0.65 * soil_gradient, 0, 1)
    vegetacion_prob = np.clip(0.18 + 0.62 * vegetation_gradient, 0, 1)

    hidrologia = rng.binomial(1, hidrologia_prob)
    suelo_hidrico = rng.binomial(1, suelo_prob)
    vegetacion_hidrofita = rng.binomial(1, vegetacion_prob)

    criterio_score = hidrologia + suelo_hidrico + vegetacion_hidrofita
    humedal_prob = np.clip(0.05 + 0.25 * criterio_score, 0, 0.95)
    humedal_real_simulado = rng.binomial(1, humedal_prob)

    presion_urbana = np.clip(
        rng.normal(loc=62 - 18 * humedal_real_simulado + 0.25 * x_coord, scale=16),
        0,
        100,
    )

    return pd.DataFrame(
        {
            "id": np.arange(1, n_cases + 1),
            "x_coord": x_coord.round(2),
            "y_coord": y_coord.round(2),
            "hidrologia": hidrologia,
            "suelo_hidrico": suelo_hidrico,
            "vegetacion_hidrofita": vegetacion_hidrofita,
            "presion_urbana": presion_urbana.round(2),
            "humedal_real_simulado": humedal_real_simulado,
        }
    )


def apply_measurement_noise(
    data: pd.DataFrame,
    noise_level: float = 0.15,
    seed: int = 42,
) -> pd.DataFrame:
    """Flip observed criteria according to a measurement noise level.

    The original criteria and `humedal_real_simulado` remain untouched. Noise is
    applied only to the observed columns ending in `_obs`.
    """

    if not 0 <= noise_level <= 1:
        raise ValueError("noise_level must be between 0 and 1.")

    rng = np.random.default_rng(seed)
    noisy = data.copy()
    noisy["nivel_ruido"] = noise_level

    for criterion in CRITERIA:
        flips = rng.binomial(1, noise_level, len(noisy)).astype(bool)
        observed = noisy[criterion].copy()
        observed.loc[flips] = 1 - observed.loc[flips]
        noisy[f"{criterion}_obs"] = observed.astype(int)

    noisy["criterios_reales"] = noisy[CRITERIA].sum(axis=1)
    noisy["criterios_observados"] = noisy[[f"{c}_obs" for c in CRITERIA]].sum(axis=1)

    return noisy


def generate_synthetic_wetlands(
    n_cases: int = 1_000,
    noise_level: float = 0.15,
    seed: int = 42,
) -> pd.DataFrame:
    """Generate a complete synthetic dataset with observed noisy criteria."""

    reality = generate_base_reality(n_cases=n_cases, seed=seed)
    return apply_measurement_noise(reality, noise_level=noise_level, seed=seed + 1)


def save_synthetic_wetlands(
    output_path: str | Path = "data/synthetic_wetlands.csv",
    n_cases: int = 1_000,
    noise_level: float = 0.15,
    seed: int = 42,
) -> pd.DataFrame:
    """Generate and save the default dataset used in the case study."""

    output = Path(output_path)
    output.parent.mkdir(parents=True, exist_ok=True)
    data = generate_synthetic_wetlands(
        n_cases=n_cases,
        noise_level=noise_level,
        seed=seed,
    )
    data.to_csv(output, index=False)
    return data


if __name__ == "__main__":
    save_synthetic_wetlands()

