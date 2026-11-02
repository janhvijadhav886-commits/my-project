import pytest
from core.risk_engine import risk_engine

def test_risk_calculation_weights():
    # 4 factors at 100 should yield 100
    res = risk_engine.calculate_risk(100, 100, 100, 100)
    assert res["total_risk_score"] == 100.0
    assert res["risk_level"] == "Critical"

    # 4 factors at 0 should yield 0
    res_zero = risk_engine.calculate_risk(0, 0, 0, 0)
    assert res_zero["total_risk_score"] == 0.0
    assert res_zero["risk_level"] == "Low"

def test_risk_tiers():
    # Critical: 80 - 100
    assert risk_engine.get_risk_level(85.0) == "Critical"
    assert risk_engine.get_risk_level(80.0) == "Critical"

    # High: 60 - 79
    assert risk_engine.get_risk_level(75.0) == "High"
    assert risk_engine.get_risk_level(60.0) == "High"

    # Medium: 30 - 59
    assert risk_engine.get_risk_level(45.0) == "Medium"
    assert risk_engine.get_risk_level(30.0) == "Medium"

    # Low: 0 - 29
    assert risk_engine.get_risk_level(25.0) == "Low"
    assert risk_engine.get_risk_level(5.0) == "Low"

def test_risk_mitigation_generation():
    res = risk_engine.calculate_risk(85, 90, 80, 85)
    assert len(res["recommended_mitigations"]) > 0
    assert "Critical" in res["risk_level"]
