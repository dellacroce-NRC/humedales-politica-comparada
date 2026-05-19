import pandas as pd

from src.data_generator import apply_measurement_noise, generate_base_reality
from src.legal_rules import apply_legal_rule, ley_chile, ley_colombia, ley_eeuu
from src.metrics import compute_rule_metrics


def test_noise_zero_keeps_observed_criteria_equal_to_reality():
    base = generate_base_reality(n_cases=100, seed=1)
    observed = apply_measurement_noise(base, noise_level=0, seed=2)

    assert (observed["hidrologia"] == observed["hidrologia_obs"]).all()
    assert (observed["suelo_hidrico"] == observed["suelo_hidrico_obs"]).all()
    assert (observed["vegetacion_hidrofita"] == observed["vegetacion_hidrofita_obs"]).all()


def test_noise_changes_only_observed_columns_not_reference_label():
    base = generate_base_reality(n_cases=300, seed=3)
    observed = apply_measurement_noise(base, noise_level=0.5, seed=4)

    assert (base["humedal_real_simulado"] == observed["humedal_real_simulado"]).all()
    assert observed["criterios_observados"].ne(observed["criterios_reales"]).any()


def test_legal_rules_match_expected_boolean_logic():
    row = pd.Series(
        {
            "hidrologia_obs": 1,
            "suelo_hidrico_obs": 0,
            "vegetacion_hidrofita_obs": 0,
        }
    )

    assert ley_chile(row) is True
    assert ley_eeuu(row) is False
    assert ley_colombia(row) is False

    row["suelo_hidrico_obs"] = 1
    assert ley_colombia(row) is True

    row["vegetacion_hidrofita_obs"] = 1
    assert ley_eeuu(row) is True


def test_metrics_are_calculated_against_synthetic_reference():
    data = pd.DataFrame(
        {
            "hidrologia_obs": [1, 1, 0, 0],
            "suelo_hidrico_obs": [0, 0, 0, 0],
            "vegetacion_hidrofita_obs": [0, 0, 0, 0],
            "humedal_real_simulado": [1, 0, 1, 0],
        }
    )

    predictions = apply_legal_rule(data, "Chile: regla amplia (1 de 3)")
    metrics = compute_rule_metrics(data, "Chile: regla amplia (1 de 3)")

    assert predictions.tolist() == [1, 1, 0, 0]
    assert metrics["verdaderos_positivos"] == 1
    assert metrics["falsos_positivos"] == 1
    assert metrics["falsos_negativos"] == 1
    assert metrics["verdaderos_negativos"] == 1
    assert metrics["precision"] == 0.5
    assert metrics["recall"] == 0.5
