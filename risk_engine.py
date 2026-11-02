"""
=============================================================================
DEFENSIVE CYBERSECURITY RISK ENGINE (risk_engine.py)
=============================================================================
Evaluates threat actor risk exposure across 4 core defensive intelligence pillars:
1. Infrastructure Risk (Hosting resilience, C2 complexity, TLS/Tor indicators)
2. Behavioural Risk (Exploit capability, ransomware affiliation, target scope)
3. Network Risk (Blockchain transaction velocity, mixer usage, escrow volume)
4. Activity Risk (Recency of operations, forum frequency, campaign velocity)

Formulas & Tiers:
Total Risk = (Infra * 0.25) + (Behaviour * 0.25) + (Network * 0.25) + (Activity * 0.25)

0-29   = Low
30-59  = Medium
60-79  = High
80-100 = Critical
"""

from typing import Dict, Any, Optional

class RiskEngine:
    def __init__(self):
        self.default_weights = {
            "infrastructure": 0.25,
            "behavioural": 0.25,
            "network": 0.25,
            "activity": 0.25
        }

    def get_risk_level(self, score: float) -> str:
        if score >= 80.0:
            return "Critical"
        elif score >= 60.0:
            return "High"
        elif score >= 30.0:
            return "Medium"
        else:
            return "Low"

    def calculate_risk(self,
                       infra_risk: float,
                       behaviour_risk: float,
                       network_risk: float,
                       activity_risk: float,
                       custom_weights: Optional[Dict[str, float]] = None) -> Dict[str, Any]:
        """
        Calculates weighted composite risk score and produces defensive mitigation recommendations.
        """
        # Clamp inputs to [0, 100]
        i_risk = min(100.0, max(0.0, float(infra_risk)))
        b_risk = min(100.0, max(0.0, float(behaviour_risk)))
        n_risk = min(100.0, max(0.0, float(network_risk)))
        a_risk = min(100.0, max(0.0, float(activity_risk)))

        weights = custom_weights or self.default_weights
        w_i = weights.get("infrastructure", 0.25)
        w_b = weights.get("behavioural", 0.25)
        w_n = weights.get("network", 0.25)
        w_a = weights.get("activity", 0.25)

        total_weight = w_i + w_b + w_n + w_a
        if total_weight <= 0:
            total_weight = 1.0

        # Weighted calculation
        total_risk = (
            (i_risk * w_i) +
            (b_risk * w_b) +
            (n_risk * w_n) +
            (a_risk * w_a)
        ) / total_weight

        total_risk = round(total_risk, 2)
        risk_level = self.get_risk_level(total_risk)

        # Generate actionable defensive mitigations based on highest risk contributors
        mitigations = []
        if i_risk >= 70.0:
            mitigations.append("Deploy automated sinkhole and blocklist rules for associated ASN/IP nodes.")
            mitigations.append("Monitor Certificate Transparency logs for newly registered wildcard domains.")
        if b_risk >= 70.0:
            mitigations.append("Implement virtual patching for known enterprise VPN/Citrix entrypoints.")
            mitigations.append("Enforce hardware MFA tokens and credential rotation for privileged accounts.")
        if n_risk >= 70.0:
            mitigations.append("Flag associated cryptocurrency addresses on blockchain transaction monitoring.")
            mitigations.append("Submit suspicious transaction reports (STR) for mixer/bridge liquidity pools.")
        if a_risk >= 70.0:
            mitigations.append("Elevate SOC alert threshold to Priority-1 for related IOC triggers.")
            mitigations.append("Increase passive forum and marketplace crawler frequency.")

        if not mitigations:
            mitigations.append("Maintain baseline passive surveillance and routine threat telemetry logging.")

        # Rationale string
        highest_factor = max(
            [("Infrastructure", i_risk), ("Behavioural", b_risk), ("Network", n_risk), ("Activity", a_risk)],
            key=lambda x: x[1]
        )

        rationale = (
            f"Overall risk evaluated as {risk_level} ({total_risk}/100). "
            f"Primary risk driver is {highest_factor[0]} Risk ({highest_factor[1]:.1f}/100) with "
            f"balanced multi-factor weighting across passive defensive observables."
        )

        return {
            "total_risk_score": total_risk,
            "risk_level": risk_level,
            "breakdown": {
                "infrastructure_risk": i_risk,
                "behavioural_risk": b_risk,
                "network_risk": n_risk,
                "activity_risk": a_risk
            },
            "weights_used": {
                "infrastructure": w_i,
                "behavioural": w_b,
                "network": w_n,
                "activity": w_a
            },
            "primary_driver": highest_factor[0],
            "rationale": rationale,
            "recommended_mitigations": mitigations
        }

    def assess_actor(self, actor: Dict[str, Any], handles_count: int, wallets_count: int, infra_count: int) -> Dict[str, Any]:
        """Auto-evaluates baseline 4-factor risk for an actor from existing metadata."""
        base_score = float(actor.get("risk_score", 50.0))

        # Infrastructure risk derived from indicator footprint
        infra_risk = min(98.0, 45.0 + (infra_count * 12.0))
        if "Hosting" in actor.get("category", ""):
            infra_risk = max(infra_risk, 92.0)

        # Behavioural risk derived from threat category
        cat = actor.get("category", "")
        if "Exploit" in cat or "Ransomware" in cat:
            behaviour_risk = 94.0
        elif "Initial Access" in cat or "Supply Chain" in cat:
            behaviour_risk = 82.0
        elif "Finance" in cat or "Mixing" in cat:
            behaviour_risk = 78.0
        else:
            behaviour_risk = 60.0

        # Network risk derived from wallet count and financial activity
        network_risk = min(98.0, 50.0 + (wallets_count * 15.0))
        if "Mixing" in cat:
            network_risk = 95.0

        # Activity risk derived from status and recency
        if actor.get("status") == "Active":
            activity_risk = min(95.0, base_score + 5.0)
        elif actor.get("status") == "Monitored":
            activity_risk = 60.0
        else:
            activity_risk = 35.0

        return self.calculate_risk(infra_risk, behaviour_risk, network_risk, activity_risk)

# Singleton
risk_engine = RiskEngine()
