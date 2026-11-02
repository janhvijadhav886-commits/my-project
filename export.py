"""
Dossier export blueprint for CSV, JSON, and printable HTML/PDF threat actor intelligence reports.
"""

import io
import csv
import json
from datetime import datetime, timezone
from flask import Blueprint, jsonify, request, Response, render_template, abort
from core.database import db_service
from core.risk_engine import risk_engine

export_bp = Blueprint("export", __name__)

def build_full_actor_dossier(actor_id: str):
    actor = db_service.get_actor_by_id(actor_id)
    if not actor:
        return None

    aid = actor["id"]
    handles = db_service.get_actor_handles(aid)
    pgp = db_service.get_actor_pgp(aid)
    wallets = db_service.get_actor_wallets(aid)
    marketplaces = db_service.get_actor_marketplaces(aid)
    infra = db_service.get_actor_infrastructure(aid)
    persona_links = db_service.get_persona_links(aid)
    relationships = db_service.get_actor_relationships(aid)
    timeline = db_service.get_timeline(aid)
    persona_profile = db_service.get_actor_persona_profile(aid)
    risk_assessment = risk_engine.assess_actor(actor, len(handles), len(wallets), len(infra))

    return {
        "metadata": {
            "dossier_classification": "OFFICIAL DEFENSIVE CYBER INTELLIGENCE (SYNTHETIC)",
            "problem_statement_id": "SIH-26151",
            "organization": "National Technical Research Organisation (NTRO)",
            "generated_at": datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC"),
            "disclaimer": "Defensive intelligence indicator dataset. All entities and records are synthetic."
        },
        "actor_summary": actor,
        "risk_assessment": risk_assessment,
        "handles": handles,
        "pgp_keys": pgp,
        "wallets": wallets,
        "marketplaces": marketplaces,
        "infrastructure": infra,
        "persona_links": persona_links,
        "persona_profile": persona_profile,
        "relationships": relationships,
        "timeline_events": timeline
    }

# -----------------------------------------------------------------------------
# 1. JSON EXPORT
# -----------------------------------------------------------------------------
@export_bp.route("/api/export/actor/<actor_id>/json", methods=["GET"])
def export_actor_json(actor_id):
    dossier = build_full_actor_dossier(actor_id)
    if not dossier:
        return jsonify({"status": "error", "message": "Actor not found"}), 404

    actor_code = dossier["actor_summary"].get("actor_code", "ACTOR")
    filename = f"NTRO_{actor_code}_Dossier_{datetime.now(timezone.utc).strftime('%Y%m%d')}.json"

    json_str = json.dumps(dossier, indent=2, default=str)
    return Response(
        json_str,
        mimetype="application/json",
        headers={"Content-Disposition": f"attachment;filename={filename}"}
    )

# -----------------------------------------------------------------------------
# 2. CSV EXPORT
# -----------------------------------------------------------------------------
@export_bp.route("/api/export/actor/<actor_id>/csv", methods=["GET"])
def export_actor_csv(actor_id):
    dossier = build_full_actor_dossier(actor_id)
    if not dossier:
        return jsonify({"status": "error", "message": "Actor not found"}), 404

    actor = dossier["actor_summary"]
    risk = dossier["risk_assessment"]
    output = io.StringIO()
    writer = csv.writer(output)

    # Section 1: Header
    writer.writerow(["# NTRO THREAT ACTOR INTELLIGENCE DOSSIER (SYNTHETIC DEMO)"])
    writer.writerow(["Generated At", dossier["metadata"]["generated_at"]])
    writer.writerow(["Disclaimer", dossier["metadata"]["disclaimer"]])
    writer.writerow([])

    # Section 2: Actor Summary
    writer.writerow(["--- ACTOR PROFILE ---"])
    writer.writerow(["Actor Code", actor.get("actor_code")])
    writer.writerow(["Primary Handle", actor.get("primary_handle")])
    writer.writerow(["Category", actor.get("category")])
    writer.writerow(["Risk Score", actor.get("risk_score")])
    writer.writerow(["Risk Level", risk.get("risk_level")])
    writer.writerow(["Attribution Confidence", f"{actor.get('attribution_confidence')}%"])
    writer.writerow(["Status", actor.get("status")])
    writer.writerow(["Operational Language", actor.get("operational_language")])
    writer.writerow(["Primary Timezone", actor.get("primary_timezone")])
    writer.writerow(["First Seen", actor.get("first_seen")])
    writer.writerow(["Last Seen", actor.get("last_seen")])
    writer.writerow(["Threat Description", actor.get("threat_description")])
    writer.writerow([])

    # Section 3: Handles
    writer.writerow(["--- OBSERVED HANDLES & PLATFORMS ---"])
    writer.writerow(["Handle", "Platform", "Observed Role", "Confidence (%)", "Primary?"])
    for h in dossier["handles"]:
        writer.writerow([h.get("handle"), h.get("platform"), h.get("observed_role"), h.get("confidence"), h.get("is_primary")])
    writer.writerow([])

    # Section 4: Wallets
    writer.writerow(["--- CRYPTOCURRENCY WALLETS ---"])
    writer.writerow(["Currency", "Wallet Address", "Cluster Label", "Total Received (USD)", "Risk Level"])
    for w in dossier["wallets"]:
        writer.writerow([w.get("currency"), w.get("wallet_address"), w.get("cluster_label"), w.get("total_received_usd"), w.get("risk_level")])
    writer.writerow([])

    # Section 5: PGP Keys
    writer.writerow(["--- PGP KEYS ---"])
    writer.writerow(["Key ID", "Fingerprint", "Algorithm", "User ID", "Status"])
    for p in dossier["pgp_keys"]:
        writer.writerow([p.get("key_id"), p.get("key_fingerprint"), p.get("key_algorithm"), p.get("user_id_string"), p.get("revocation_status")])
    writer.writerow([])

    # Section 6: Infrastructure
    writer.writerow(["--- PASSIVE INFRASTRUCTURE INDICATORS ---"])
    writer.writerow(["Indicator Type", "Indicator Value", "Service Banner", "ASN Org", "Confidence (%)"])
    for i in dossier["infrastructure"]:
        writer.writerow([i.get("indicator_type"), i.get("indicator_value"), i.get("service_banner"), i.get("asn_organization"), i.get("confidence")])
    writer.writerow([])

    output.seek(0)
    actor_code = actor.get("actor_code", "ACTOR")
    filename = f"NTRO_{actor_code}_Intelligence_{datetime.now(timezone.utc).strftime('%Y%m%d')}.csv"

    return Response(
        output.getvalue(),
        mimetype="text/csv",
        headers={"Content-Disposition": f"attachment;filename={filename}"}
    )

# -----------------------------------------------------------------------------
# 3. PRINTABLE HTML REPORT (Can be printed to PDF directly via browser Ctrl+P)
# -----------------------------------------------------------------------------
@export_bp.route("/api/report/actor/<actor_id>", methods=["GET"])
def view_actor_report(actor_id):
    dossier = build_full_actor_dossier(actor_id)
    if not dossier:
        return abort(404, description="Threat Actor dossier not found")

    return render_template("report_print.html", dossier=dossier)
