import pytest
from core.persona_engine import persona_engine

def test_extract_text_features():
    sample_text = "Selling high-tier domain admin access. Escrow accepted through Dread admin only. Check PGP signature."
    features = persona_engine.extract_text_features(sample_text)
    
    assert features["avg_sentence_len"] > 0
    assert features["avg_word_len"] > 0
    assert 0.0 <= features["type_token_ratio"] <= 1.0
    assert features["punctuation_density"] > 0

def test_analyze_personas():
    actor_a = {
        "primary_handle": "NightFalcon",
        "primary_language": "Russian",
        "sample_corpus": "Selling verified VPN domain admin access. Escrow only through Dread or Exploit admin.",
        "posting_frequency_score": 88.0,
        "signature_phrases": ["work through escrow only", "guaranteed clean domain admin"]
    }

    actor_b = {
        "primary_handle": "ShadowByte",
        "primary_language": "Russian",
        "sample_corpus": "Offering corporate access with domain admin credentials. Strict escrow terms on XSS or Dread.",
        "posting_frequency_score": 82.0,
        "signature_phrases": ["escrow accepted", "domain admin verified"]
    }

    report = persona_engine.analyze_personas(actor_a, actor_b)

    assert "overall_similarity" in report
    assert 0 <= report["overall_similarity"] <= 100
    assert report["confidence"] in ["Low", "Medium", "High", "Very High"]
    assert "Potential analytical linkage" in report["analytical_disclaimer"]
    assert "evidence" in report
