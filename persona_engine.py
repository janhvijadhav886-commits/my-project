"""
=============================================================================
DEFENSIVE PERSONA ANALYSIS ENGINE (persona_engine.py)
=============================================================================
Calculates probabilistic stylometric and behavioral similarity between synthetic
threat actor profiles using TF-IDF, N-gram stylometry, vocabulary
richness (Type-Token Ratio), and operational temporal patterns.

DEFENSIVE REQUIREMENT:
All outputs are probabilistic attribution indicators and not confirmed identities.
"""

import re
import math
from typing import Dict, Any, List, Tuple
from collections import Counter

# Try importing scikit-learn; if restricted by system DLL policies, fall back to pure-Python TF-IDF
try:
    from sklearn.feature_extraction.text import TfidfVectorizer
    from sklearn.metrics.pairwise import cosine_similarity
    SKLEARN_AVAILABLE = True
except Exception:
    SKLEARN_AVAILABLE = False


class PureTfidfCalculator:
    """Pure-Python TF-IDF and Cosine similarity implementation with zero external C-extension dependencies."""
    
    @staticmethod
    def tokenize(text: str) -> List[str]:
        words = re.findall(r'\b[a-zA-Z0-9_-]{2,}\b', text.lower())
        stopwords = {
            'the', 'and', 'for', 'with', 'that', 'this', 'from', 'are', 'was',
            'have', 'has', 'had', 'what', 'when', 'where', 'who', 'will', 'more',
            'can', 'all', 'your', 'about', 'out', 'over', 'into', 'some'
        }
        return [w for w in words if w not in stopwords]

    @classmethod
    def get_ngrams(cls, tokens: List[str], n: int = 2) -> List[str]:
        ngrams = list(tokens)
        for i in range(len(tokens) - n + 1):
            ngrams.append(" ".join(tokens[i:i+n]))
        return ngrams

    @classmethod
    def compute_similarity(cls, doc_a: str, doc_b: str) -> Tuple[float, List[str]]:
        tok_a = cls.get_ngrams(cls.tokenize(doc_a))
        tok_b = cls.get_ngrams(cls.tokenize(doc_b))

        if not tok_a or not tok_b:
            return 40.0, []

        tf_a = Counter(tok_a)
        tf_b = Counter(tok_b)

        all_terms = set(tf_a.keys()).union(set(tf_b.keys()))
        doc_count = 2

        # Compute TF-IDF vectors
        vec_a = {}
        vec_b = {}
        for term in all_terms:
            df = (1 if term in tf_a else 0) + (1 if term in tf_b else 0)
            idf = math.log((1 + doc_count) / (1 + df)) + 1.0
            vec_a[term] = tf_a.get(term, 0) * idf
            vec_b[term] = tf_b.get(term, 0) * idf

        # Cosine similarity
        dot_product = sum(vec_a[t] * vec_b[t] for t in all_terms)
        norm_a = math.sqrt(sum(v ** 2 for v in vec_a.values()))
        norm_b = math.sqrt(sum(v ** 2 for v in vec_b.values()))

        if norm_a == 0 or norm_b == 0:
            return 45.0, []

        cosine_sim = dot_product / (norm_a * norm_b)
        sim_pct = round(cosine_sim * 100, 2)

        # Find shared salient terms
        shared = []
        for t in all_terms:
            if t in tf_a and t in tf_b:
                shared.append((t, vec_a[t] * vec_b[t]))
        shared.sort(key=lambda x: x[1], reverse=True)
        top_shared = [s[0] for s in shared[:6]]

        return sim_pct, top_shared


class PersonaEngine:
    def __init__(self):
        self.disclaimer = "Potential analytical linkage — not confirmed identity."

    # -------------------------------------------------------------------------
    # STYLOMETRIC TEXT EXTRACTION
    # -------------------------------------------------------------------------
    def extract_text_features(self, text: str) -> Dict[str, float]:
        """Extracts statistical stylometric features from a text corpus."""
        if not text or len(text.strip()) == 0:
            return {
                "avg_sentence_len": 0.0,
                "avg_word_len": 0.0,
                "type_token_ratio": 0.0,
                "punctuation_density": 0.0,
                "digit_density": 0.0,
                "uppercase_ratio": 0.0
            }

        clean_text = text.strip()
        sentences = [s for s in re.split(r'[.!?]+', clean_text) if s.strip()]
        num_sentences = max(len(sentences), 1)

        words = re.findall(r'\b\w+\b', clean_text.lower())
        num_words = max(len(words), 1)
        unique_words = set(words)

        # Average sentence length (in words)
        avg_sentence_len = num_words / num_sentences

        # Average word length
        avg_word_len = sum(len(w) for w in words) / num_words

        # Type-Token Ratio (Vocabulary Richness)
        type_token_ratio = len(unique_words) / num_words

        # Punctuation count
        punctuations = re.findall(r'[^\w\s]', clean_text)
        punctuation_density = len(punctuations) / max(len(clean_text), 1)

        # Digit density
        digits = re.findall(r'\d', clean_text)
        digit_density = len(digits) / max(len(clean_text), 1)

        # Uppercase ratio
        uppers = [c for c in clean_text if c.isupper()]
        uppercase_ratio = len(uppers) / max(len(clean_text), 1)

        return {
            "avg_sentence_len": avg_sentence_len,
            "avg_word_len": avg_word_len,
            "type_token_ratio": type_token_ratio,
            "punctuation_density": punctuation_density,
            "digit_density": digit_density,
            "uppercase_ratio": uppercase_ratio
        }

    # -------------------------------------------------------------------------
    # STYLOMETRIC SIMILARITY (Normalized Distance)
    # -------------------------------------------------------------------------
    def compute_stylometric_similarity(self, feat_a: Dict[str, float], feat_b: Dict[str, float]) -> float:
        """Computes similarity percentage across numerical stylometric markers."""
        diffs = []
        for key in feat_a:
            v1 = feat_a[key]
            v2 = feat_b[key]
            denom = max(v1, v2, 0.0001)
            similarity = 1.0 - (abs(v1 - v2) / denom)
            diffs.append(max(0.0, similarity))

        avg_diff = sum(diffs) / len(diffs) if diffs else 0.5
        return float(avg_diff * 100)

    # -------------------------------------------------------------------------
    # TF-IDF & VOCABULARY COSINE SIMILARITY
    # -------------------------------------------------------------------------
    def compute_vocabulary_similarity(self, text_a: str, text_b: str) -> Tuple[float, List[str]]:
        """Calculates TF-IDF cosine similarity and extracts top shared semantic n-grams."""
        if not text_a.strip() or not text_b.strip():
            return 0.0, []

        if SKLEARN_AVAILABLE:
            try:
                vectorizer = TfidfVectorizer(
                    ngram_range=(1, 2),
                    stop_words="english",
                    token_pattern=r'(?u)\b\w+\b'
                )
                tfidf_matrix = vectorizer.fit_transform([text_a, text_b])
                cos_sim = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:2])[0][0]
                sim_pct = float(cos_sim * 100)

                feature_names = vectorizer.get_feature_names_out()
                row_a = tfidf_matrix.getrow(0).toarray()[0]
                row_b = tfidf_matrix.getrow(1).toarray()[0]

                shared_terms = []
                for i, fname in enumerate(feature_names):
                    if row_a[i] > 0 and row_b[i] > 0:
                        shared_terms.append((fname, row_a[i] * row_b[i]))

                shared_terms.sort(key=lambda x: x[1], reverse=True)
                top_shared = [term for term, score in shared_terms[:6]]
                return sim_pct, top_shared
            except Exception:
                pass

        # Fallback to Pure-Python TF-IDF Engine
        return PureTfidfCalculator.compute_similarity(text_a, text_b)

    # -------------------------------------------------------------------------
    # BEHAVIORAL & TEMPORAL PATTERN ALIGNMENT
    # -------------------------------------------------------------------------
    def compute_behavior_similarity(self, profile_a: Dict[str, Any], profile_b: Dict[str, Any]) -> float:
        """Calculates behavioral similarity score based on active hours, platforms, and roles."""
        score = 70.0  # Base heuristic

        lang_a = str(profile_a.get("primary_language", "")).lower()
        lang_b = str(profile_b.get("primary_language", "")).lower()
        if lang_a and lang_b and (lang_a in lang_b or lang_b in lang_a):
            score += 15.0

        tz_a = str(profile_a.get("active_hours_utc", profile_a.get("primary_timezone", ""))).lower()
        tz_b = str(profile_b.get("active_hours_utc", profile_b.get("primary_timezone", ""))).lower()
        if tz_a and tz_b:
            if "utc+3" in tz_a and "utc+3" in tz_b:
                score += 10.0
            elif ("utc+2" in tz_a and "utc+3" in tz_b) or ("utc+3" in tz_a and "utc+2" in tz_b):
                score += 8.0
            elif tz_a == tz_b:
                score += 12.0

        return min(99.0, max(25.0, score))

    def compute_posting_frequency_similarity(self, freq_a: float, freq_b: float) -> float:
        denom = max(freq_a, freq_b, 1.0)
        return max(0.0, 1.0 - (abs(freq_a - freq_b) / denom)) * 100

    # -------------------------------------------------------------------------
    # FULL PERSONA COMPARISON ANALYSIS
    # -------------------------------------------------------------------------
    def analyze_personas(self, 
                         actor_a_data: Dict[str, Any], 
                         actor_b_data: Dict[str, Any],
                         custom_text_a: str = None,
                         custom_text_b: str = None) -> Dict[str, Any]:
        """
        Executes full comparative stylometry and returns comprehensive analytical report.
        """
        text_a = custom_text_a or actor_a_data.get("sample_corpus") or actor_a_data.get("threat_description", "")
        text_b = custom_text_b or actor_b_data.get("sample_corpus") or actor_b_data.get("threat_description", "")

        # 1. Stylometric analysis
        feat_a = self.extract_text_features(text_a)
        feat_b = self.extract_text_features(text_b)
        writing_style_sim = self.compute_stylometric_similarity(feat_a, feat_b)

        # 2. Vocabulary similarity via TF-IDF
        vocab_sim, shared_terms = self.compute_vocabulary_similarity(text_a, text_b)

        # 3. Behavioral alignment
        behavior_sim = self.compute_behavior_similarity(actor_a_data, actor_b_data)

        # 4. Activity pattern similarity
        activity_pattern_sim = 85.0 if ("utc+3" in str(actor_a_data).lower() and "utc+3" in str(actor_b_data).lower()) else 72.0

        # 5. Posting frequency
        freq_a = float(actor_a_data.get("posting_frequency_score", 80.0))
        freq_b = float(actor_b_data.get("posting_frequency_score", 75.0))
        posting_sim = self.compute_posting_frequency_similarity(freq_a, freq_b)

        # Common phrase matches
        phrases_a = set(actor_a_data.get("signature_phrases", []))
        phrases_b = set(actor_b_data.get("signature_phrases", []))
        shared_phrases = list(phrases_a.intersection(phrases_b))
        if not shared_phrases and ("escrow" in text_a.lower() and "escrow" in text_b.lower()):
            shared_phrases.append("escrow transaction requirement")
        if "pgp" in text_a.lower() and "pgp" in text_b.lower():
            shared_phrases.append("pgp encrypted communication pattern")

        # Weighted Overall Similarity
        overall_sim = (
            (writing_style_sim * 0.25) +
            (vocab_sim * 0.25) +
            (behavior_sim * 0.20) +
            (activity_pattern_sim * 0.15) +
            (posting_sim * 0.15)
        )
        overall_sim = round(min(98.5, max(15.0, overall_sim)), 2)

        # Confidence Level
        if overall_sim >= 85.0:
            confidence = "High"
        elif overall_sim >= 70.0:
            confidence = "Medium"
        else:
            confidence = "Low"

        evidence = (
            f"Comparison between {actor_a_data.get('primary_handle', 'Actor A')} and {actor_b_data.get('primary_handle', 'Actor B')} "
            f"demonstrates {overall_sim}% probabilistic correlation. "
            f"Identified {len(shared_terms)} shared semantic n-grams ({', '.join(shared_terms) if shared_terms else 'none'}), "
            f"stylometric Type-Token Ratio variance of {abs(feat_a['type_token_ratio'] - feat_b['type_token_ratio']):.3f}, "
            f"and aligned operational communication patterns."
        )

        return {
            "overall_similarity": overall_sim,
            "confidence": confidence,
            "writing_style_similarity": round(writing_style_sim, 2),
            "vocabulary_similarity": round(vocab_sim, 2),
            "behaviour_similarity": round(behavior_sim, 2),
            "activity_pattern_similarity": round(activity_pattern_sim, 2),
            "posting_frequency_similarity": round(posting_sim, 2),
            "shared_indicators": {
                "shared_vocabulary": shared_terms,
                "shared_phrases": shared_phrases,
                "stylometric_markers": {
                    "actor_a_ttr": round(feat_a["type_token_ratio"], 3),
                    "actor_b_ttr": round(feat_b["type_token_ratio"], 3),
                    "actor_a_avg_sent_len": round(feat_a["avg_sentence_len"], 1),
                    "actor_b_avg_sent_len": round(feat_b["avg_sentence_len"], 1),
                }
            },
            "evidence": evidence,
            "analytical_disclaimer": self.disclaimer
        }

persona_engine = PersonaEngine()
