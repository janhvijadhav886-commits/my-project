"""
View route handlers rendering SOC dashboard templates with server-side context.
"""

from flask import Blueprint, render_template, abort
from core.database import db_service

views_bp = Blueprint("views", __name__)

@views_bp.route("/")
def dashboard():
    return render_template("dashboard.html", active_page="dashboard")

@views_bp.route("/actors")
def actors():
    return render_template("actors.html", active_page="actors")

@views_bp.route("/actors/<actor_id>")
def actor_detail(actor_id):
    actor = db_service.get_actor_by_id(actor_id)
    if not actor:
        abort(404, description=f"Threat Actor '{actor_id}' not found.")
    return render_template("actor_detail.html", actor=actor, active_page="actors")

@views_bp.route("/actor-intelligence")
def actor_intelligence():
    # Helper direct redirect or alias to actors
    return render_template("actors.html", active_page="actor_intelligence")

@views_bp.route("/infrastructure")
def infrastructure():
    return render_template("infrastructure.html", active_page="infrastructure")

@views_bp.route("/relationships")
def relationships():
    return render_template("relationships.html", active_page="relationships")

@views_bp.route("/persona")
def persona():
    return render_template("persona.html", active_page="persona")

@views_bp.route("/timeline")
def timeline():
    return render_template("timeline.html", active_page="timeline")

@views_bp.route("/sources")
def sources():
    return render_template("sources.html", active_page="sources")

@views_bp.route("/risk")
def risk():
    return render_template("risk.html", active_page="risk")

@views_bp.route("/reports")
def reports():
    return render_template("reports.html", active_page="reports")

@views_bp.route("/settings")
def settings():
    return render_template("settings.html", active_page="settings")
