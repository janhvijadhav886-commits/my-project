"""
RESTful API endpoints for the NTRO Threat Actor Intelligence Platform.
All responses follow consistent JSON formatting and proper HTTP status codes.
"""

import logging
from flask import Blueprint, jsonify, request
from core.database import db_service
from core.persona_engine import persona_engine
from core.risk_engine import risk_engine

logger = logging.getLogger(__name__)
api_bp = Blueprint("api", __name__, url_prefix="/api")

# -----------------------------------------------------------------------------
# 1. DASHBOARD & SYSTEM
# -----------------------------------------------------------------------------
@api_bp.route("/dashboard/stats", methods=["GET"])
def get_dashboard_stats():
    try:
        stats = db_service.get_dashboard_stats()
        return jsonify({
            "status": "success",
            "data": stats
        }), 200
    except Exception as e:
        logger.error(f"Error in /api/dashboard/stats: {e}", exc_info=True)
        return jsonify({"status": "error", "message": "Failed to retrieve dashboard statistics"}), 500

@api_bp.route("/system/status", methods=["GET"])
def get_system_status():
    try:
        status_info = db_service.get_status()
        return jsonify({"status": "success", "data": status_info}), 200
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

@api_bp.route("/system/reset-demo", methods=["POST"])
def reset_demo_data():
    try:
        db_service.reset_synthetic_data()
        return jsonify({"status": "success", "message": "Synthetic demo dataset successfully reset"}), 200
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

# -----------------------------------------------------------------------------
# 2. THREAT ACTORS
# -----------------------------------------------------------------------------
@api_bp.route("/actors", methods=["GET"])
def get_actors():
    try:
        search = request.args.get("search", None)
        risk = request.args.get("risk", None)
        category = request.args.get("category", None)
        status = request.args.get("status", None)

        actors = db_service.get_actors(
            search=search,
            risk_filter=risk,
            category_filter=category,
            status_filter=status
        )
        return jsonify({
            "status": "success",
            "count": len(actors),
            "data": actors
        }), 200
    except Exception as e:
        logger.error(f"Error in /api/actors: {e}")
        return jsonify({"status": "error", "message": "Failed to fetch threat actors"}), 500

@api_bp.route("/actors/<actor_id>", methods=["GET"])
def get_actor_detail(actor_id):
    try:
        actor = db_service.get_actor_by_id(actor_id)
        if not actor:
            return jsonify({"status": "error", "message": f"Threat actor '{actor_id}' not found"}), 404
        return jsonify({"status": "success", "data": actor}), 200
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

@api_bp.route("/actors/<actor_id>/handles", methods=["GET"])
def get_actor_handles(actor_id):
    try:
        handles = db_service.get_actor_handles(actor_id)
        return jsonify({"status": "success", "count": len(handles), "data": handles}), 200
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

@api_bp.route("/actors/<actor_id>/pgp", methods=["GET"])
def get_actor_pgp(actor_id):
    try:
        pgp = db_service.get_actor_pgp(actor_id)
        return jsonify({"status": "success", "count": len(pgp), "data": pgp}), 200
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

@api_bp.route("/actors/<actor_id>/wallets", methods=["GET"])
def get_actor_wallets(actor_id):
    try:
        wallets = db_service.get_actor_wallets(actor_id)
        return jsonify({"status": "success", "count": len(wallets), "data": wallets}), 200
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

@api_bp.route("/actors/<actor_id>/marketplaces", methods=["GET"])
def get_actor_marketplaces(actor_id):
    try:
        marketplaces = db_service.get_actor_marketplaces(actor_id)
        return jsonify({"status": "success", "count": len(marketplaces), "data": marketplaces}), 200
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

@api_bp.route("/actors/<actor_id>/infrastructure", methods=["GET"])
def get_actor_infrastructure(actor_id):
    try:
        infra = db_service.get_actor_infrastructure(actor_id)
        return jsonify({"status": "success", "count": len(infra), "data": infra}), 200
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

@api_bp.route("/actors/<actor_id>/relationships", methods=["GET"])
def get_actor_relationships(actor_id):
    try:
        relationships = db_service.get_actor_relationships(actor_id)
        return jsonify({"status": "success", "count": len(relationships), "data": relationships}), 200
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

# -----------------------------------------------------------------------------
# 3. GLOBAL INFRASTRUCTURE & SOURCES
# -----------------------------------------------------------------------------
@api_bp.route("/infrastructure", methods=["GET"])
def get_all_infrastructure():
    try:
        itype = request.args.get("type", None)
        search = request.args.get("search", None)
        indicators = db_service.get_infrastructure(indicator_type=itype, search=search)
        return jsonify({"status": "success", "count": len(indicators), "data": indicators}), 200
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

@api_bp.route("/sources", methods=["GET"])
def get_sources():
    try:
        sources = db_service.get_sources()
        return jsonify({"status": "success", "count": len(sources), "data": sources}), 200
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

@api_bp.route("/intelligence-events", methods=["GET"])
def get_events():
    try:
        actor_id = request.args.get("actor_id", None)
        limit = request.args.get("limit", None, type=int)
        events = db_service.get_intelligence_events(actor_id=actor_id, limit=limit)
        return jsonify({"status": "success", "count": len(events), "data": events}), 200
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

# -----------------------------------------------------------------------------
# 4. RELATIONSHIP GRAPH & PERSONA
# -----------------------------------------------------------------------------
@api_bp.route("/graph/data", methods=["GET"])
def get_graph_data():
    try:
        graph_data = db_service.get_full_graph_data()
        return jsonify({"status": "success", "data": graph_data}), 200
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

@api_bp.route("/persona-links", methods=["GET"])
def get_persona_links():
    try:
        actor_id = request.args.get("actor_id", None)
        links = db_service.get_persona_links(actor_id=actor_id)
        return jsonify({"status": "success", "count": len(links), "data": links}), 200
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

@api_bp.route("/persona/analyze", methods=["POST"])
def analyze_persona():
    try:
        payload = request.get_json(silent=True) or {}
        actor_a_id = payload.get("actor_a_id")
        actor_b_id = payload.get("actor_b_id")
        custom_text_a = payload.get("custom_text_a")
        custom_text_b = payload.get("custom_text_b")

        actor_a = db_service.get_actor_by_id(actor_a_id) if actor_a_id else {}
        actor_b = db_service.get_actor_by_id(actor_b_id) if actor_b_id else {}

        # Merge with persona profile if available
        if actor_a:
            p_prof = db_service.get_actor_persona_profile(actor_a.get("id"))
            if p_prof:
                actor_a = {**actor_a, **p_prof}

        if actor_b:
            p_prof = db_service.get_actor_persona_profile(actor_b.get("id"))
            if p_prof:
                actor_b = {**actor_b, **p_prof}

        report = persona_engine.analyze_personas(
            actor_a_data=actor_a,
            actor_b_data=actor_b,
            custom_text_a=custom_text_a,
            custom_text_b=custom_text_b
        )

        return jsonify({"status": "success", "data": report}), 200
    except Exception as e:
        logger.error(f"Error in /api/persona/analyze: {e}", exc_info=True)
        return jsonify({"status": "error", "message": f"Persona analysis failed: {str(e)}"}), 500

# -----------------------------------------------------------------------------
# 5. RISK ENGINE
# -----------------------------------------------------------------------------
@api_bp.route("/risk/<actor_id>", methods=["GET"])
def get_actor_risk(actor_id):
    try:
        actor = db_service.get_actor_by_id(actor_id)
        if not actor:
            return jsonify({"status": "error", "message": "Actor not found"}), 404

        handles = db_service.get_actor_handles(actor["id"])
        wallets = db_service.get_actor_wallets(actor["id"])
        infra = db_service.get_actor_infrastructure(actor["id"])

        assessment = risk_engine.assess_actor(actor, len(handles), len(wallets), len(infra))
        return jsonify({"status": "success", "data": assessment}), 200
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

@api_bp.route("/risk/calculate", methods=["POST"])
def calculate_custom_risk():
    try:
        payload = request.get_json(silent=True) or {}
        infra_risk = float(payload.get("infrastructure_risk", 50))
        behaviour_risk = float(payload.get("behavioural_risk", 50))
        network_risk = float(payload.get("network_risk", 50))
        activity_risk = float(payload.get("activity_risk", 50))
        weights = payload.get("weights", None)

        assessment = risk_engine.calculate_risk(
            infra_risk=infra_risk,
            behaviour_risk=behaviour_risk,
            network_risk=network_risk,
            activity_risk=activity_risk,
            custom_weights=weights
        )
        return jsonify({"status": "success", "data": assessment}), 200
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

# -----------------------------------------------------------------------------
# 6. TIMELINE
# -----------------------------------------------------------------------------
@api_bp.route("/timeline/<actor_id>", methods=["GET"])
def get_actor_timeline(actor_id):
    try:
        events = db_service.get_timeline(actor_id)
        return jsonify({"status": "success", "count": len(events), "data": events}), 200
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500
