"""
=============================================================================
NTRO DARK WEB THREAT ACTOR DE-ANONYMIZATION & ATTRIBUTION PLATFORM
PROBLEM STATEMENT ID: 26151
ORGANIZATION: National Technical Research Organisation (NTRO)
THEME: Blockchain & Cybersecurity
=============================================================================
"""

import sys
import logging
from flask import Flask, render_template, jsonify
from config import Config
from routes.api import api_bp
from routes.export import export_bp
from routes.views import views_bp
from routes.auth import auth_bp
from core.database import db_service

# Configure Enterprise Logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
    handlers=[logging.StreamHandler(sys.stdout)]
)
logger = logging.getLogger("ntro_intelligence")

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Register Blueprints
    app.register_blueprint(api_bp)
    app.register_blueprint(export_bp)
    app.register_blueprint(views_bp)
    app.register_blueprint(auth_bp)

    # Template Custom Filters
    @app.template_filter("currency_format")
    def currency_format(value):
        try:
            return f"${float(value):,.2f}"
        except (ValueError, TypeError):
            return "$0.00"

    @app.template_filter("date_format")
    def date_format(value):
        if not value:
            return "N/A"
        try:
            # Handle ISO string
            if "T" in str(value):
                return str(value).split("T")[0]
            return str(value)[:10]
        except Exception:
            return str(value)

    # Centralized Error Handlers
    @app.errorhandler(404)
    def handle_404(e):
        if hasattr(e, 'description') and e.description:
            msg = e.description
        else:
            msg = "The requested threat intelligence resource was not found."
        return render_template("base.html", error_title="404 - Resource Not Found", error_message=msg), 404

    @app.errorhandler(500)
    def handle_500(e):
        logger.error(f"Internal Server Error: {e}", exc_info=True)
        return render_template("base.html", error_title="500 - Internal Analytics Engine Error", error_message="An internal analytical processing error occurred. Check system logs."), 500

    return app

app = create_app()

def print_startup_banner():
    status = db_service.get_status()
    db_mode = status["mode"]
    print("=" * 78)
    print("  _   _ _____ ____   ___    ____   _____ _____ _____ _   _ ____  _____ ")
    print(" | \\ | |_   _|  _ \\ / _ \\  |  _ \\ | ____|  ___| ____| \\ | / ___|| ____|")
    print(" |  \\| | | | | |_) | | | | | | | ||  _| | |_  |  _| |  \\| \\___ \\|  _|  ")
    print(" | |\\  | | | |  _ <| |_| | | |_| || |___|  _| | |___| |\\  |___) | |___ ")
    print(" |_| \\_| |_| |_| \\_\\\\___/  |____/ |_____|_|   |_____|_| \\_|____/|_____|")
    print("=" * 78)
    print(" NTRO Threat Actor De-Anonymization & Attribution Analysis Platform")
    print(" SIH Problem Statement ID: 26151 | Theme: Blockchain & Cybersecurity")
    print("-" * 78)
    print(f" [*] Database Mode      : {db_mode}")
    print(f" [*] Synthetic Records  : {status['total_threat_actors']} Threat Actors | {status['total_infrastructure_indicators']} Passive Indicators")
    print(f" [*] Defense Framework  : Active (Probabilistic Attribution & Defensive Safeguards)")
    print(f" [*] Local Server URL   : http://127.0.0.1:{Config.PORT}")
    print("=" * 78)
    print(" Ready for Hackathon Demonstration & Real-Time SOC Evaluation.\n")

if __name__ == "__main__":
    print_startup_banner()
    app.run(host="127.0.0.1", port=Config.PORT, debug=Config.DEBUG)
