"""
Database abstraction layer with Supabase PostgreSQL integration and
graceful in-memory fallback for standalone hackathon demonstrations.
"""

import logging
import sys
from pathlib import Path
from typing import Dict, List, Any, Optional

if __package__ in (None, ""):
    sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from config import Config
from core.seed_data import get_synthetic_dataset

logger = logging.getLogger(__name__)

class DatabaseService:
    def __init__(self):
        self.is_supabase_active = False
        self.supabase_client = None
        self._memory_data = get_synthetic_dataset()
        self._init_connection()

    def _init_connection(self):
        if Config.is_supabase_configured():
            try:
                from supabase import create_client, Client
                self.supabase_client: Client = create_client(Config.SUPABASE_URL, Config.SUPABASE_KEY)
                # Test query to verify connection
                _ = self.supabase_client.table("threat_actors").select("id").limit(1).execute()
                self.is_supabase_active = True
                logger.info("[DATABASE] Successfully connected to Live Supabase PostgreSQL instance.")
            except Exception as e:
                self.is_supabase_active = False
                logger.warning(f"[DATABASE] Supabase initialization failed ({e}). Falling back to Synthetic In-Memory Mode.")
        else:
            self.is_supabase_active = False
            logger.info("[DATABASE] Running in Standalone Synthetic Mode (No live Supabase credentials configured).")

    def reset_synthetic_data(self):
        """Resets the in-memory dataset to initial clean state."""
        self._memory_data = get_synthetic_dataset()
        return True

    def get_status(self) -> Dict[str, Any]:
        return {
            "mode": "Live Supabase PostgreSQL" if self.is_supabase_active else "Synthetic In-Memory Engine",
            "supabase_configured": Config.is_supabase_configured(),
            "supabase_url": Config.SUPABASE_URL if Config.is_supabase_configured() else "Not configured",
            "total_threat_actors": len(self.get_actors()),
            "total_infrastructure_indicators": len(self.get_infrastructure()),
            "total_intelligence_events": len(self.get_intelligence_events()),
            "safety_mode": "Defensive Intelligence & Synthetic Data Active"
        }

    # -------------------------------------------------------------------------
    # 1. DASHBOARD STATS
    # -------------------------------------------------------------------------
    def get_dashboard_stats(self) -> Dict[str, Any]:
        actors = self.get_actors()
        infra = self.get_infrastructure()
        events = self.get_intelligence_events()
        persona_links = self.get_persona_links()

        high_risk_count = sum(1 for a in actors if float(a.get("risk_score", 0)) >= 60.0)
        active_count = sum(1 for a in actors if a.get("status") == "Active")

        # Category distribution
        categories: Dict[str, int] = {}
        for a in actors:
            cat = a.get("category", "Unassigned")
            categories[cat] = categories.get(cat, 0) + 1

        # Risk tiers
        risk_distribution = {
            "Critical (80-100)": sum(1 for a in actors if float(a.get("risk_score", 0)) >= 80),
            "High (60-79)": sum(1 for a in actors if 60 <= float(a.get("risk_score", 0)) < 80),
            "Medium (30-59)": sum(1 for a in actors if 30 <= float(a.get("risk_score", 0)) < 60),
            "Low (0-29)": sum(1 for a in actors if float(a.get("risk_score", 0)) < 30),
        }

        # Confidence distribution
        confidence_distribution = {
            "Very High (90-100%)": sum(1 for a in actors if float(a.get("attribution_confidence", 0)) >= 90),
            "High (75-89%)": sum(1 for a in actors if 75 <= float(a.get("attribution_confidence", 0)) < 90),
            "Medium (60-74%)": sum(1 for a in actors if 60 <= float(a.get("attribution_confidence", 0)) < 75),
            "Low (<60%)": sum(1 for a in actors if float(a.get("attribution_confidence", 0)) < 60),
        }

        # Infrastructure Types
        infra_types: Dict[str, int] = {}
        for i in infra:
            itype = i.get("indicator_type", "Other")
            infra_types[itype] = infra_types.get(itype, 0) + 1

        # Top 5 highest risk actors
        top_risk_actors = sorted(actors, key=lambda x: float(x.get("risk_score", 0)), reverse=True)[:5]

        return {
            "kpis": {
                "total_threat_actors": len(actors),
                "high_risk_actors": high_risk_count,
                "active_actors": active_count,
                "infrastructure_indicators": len(infra),
                "persona_links": len(persona_links),
                "intelligence_events": len(events)
            },
            "risk_distribution": risk_distribution,
            "category_distribution": categories,
            "confidence_distribution": confidence_distribution,
            "infra_type_distribution": infra_types,
            "top_risk_actors": top_risk_actors,
            "recent_events": events[:6],
            "system_status": {
                "defense_matrix": "Operational",
                "database_mode": "Live Supabase" if self.is_supabase_active else "Synthetic In-Memory",
                "last_update": "2026-08-25T16:28:00Z",
                "active_surveillance_streams": 6
            }
        }

    # -------------------------------------------------------------------------
    # 2. THREAT ACTORS
    # -------------------------------------------------------------------------
    def get_actors(self, search: Optional[str] = None, risk_filter: Optional[str] = None, category_filter: Optional[str] = None, status_filter: Optional[str] = None) -> List[Dict[str, Any]]:
        if self.is_supabase_active:
            try:
                query = self.supabase_client.table("threat_actors").select("*")
                if status_filter and status_filter != "all":
                    query = query.eq("status", status_filter)
                if category_filter and category_filter != "all":
                    query = query.eq("category", category_filter)
                response = query.order("risk_score", desc=True).execute()
                actors = response.data
            except Exception as e:
                logger.error(f"Supabase get_actors error: {e}")
                actors = self._memory_data["actors"]
        else:
            actors = self._memory_data["actors"]

        # Apply filtering
        results = []
        for a in actors:
            # Risk filter
            r_score = float(a.get("risk_score", 0))
            if risk_filter and risk_filter != "all":
                if risk_filter == "critical" and r_score < 80:
                    continue
                elif risk_filter == "high" and not (60 <= r_score < 80):
                    continue
                elif risk_filter == "medium" and not (30 <= r_score < 60):
                    continue
                elif risk_filter == "low" and r_score >= 30:
                    continue

            # Category filter
            if category_filter and category_filter != "all" and a.get("category") != category_filter:
                continue

            # Status filter
            if status_filter and status_filter != "all" and a.get("status") != status_filter:
                continue

            # Search filter (actor_code, handle, language, category, etc.)
            if search:
                s = search.lower().strip()
                matches = (
                    s in a.get("actor_code", "").lower() or
                    s in a.get("primary_handle", "").lower() or
                    s in a.get("category", "").lower() or
                    s in a.get("threat_description", "").lower() or
                    s in a.get("operational_language", "").lower()
                )
                if not matches:
                    # Also search inside actor's handles and wallets if in memory
                    actor_id = a.get("id")
                    handles = [h.get("handle", "").lower() for h in self.get_actor_handles(actor_id)]
                    wallets = [w.get("wallet_address", "").lower() for w in self.get_actor_wallets(actor_id)]
                    pgps = [p.get("key_fingerprint", "").lower() for p in self.get_actor_pgp(actor_id)]
                    if not any(s in h for h in handles) and not any(s in w for w in wallets) and not any(s in p for p in pgps):
                        continue

            results.append(a)

        return sorted(results, key=lambda x: float(x.get("risk_score", 0)), reverse=True)

    def get_actor_by_id(self, actor_id: str) -> Optional[Dict[str, Any]]:
        if self.is_supabase_active:
            try:
                # Can search by UUID or actor_code
                res = self.supabase_client.table("threat_actors").select("*").or_(f"id.eq.{actor_id},actor_code.eq.{actor_id}").limit(1).execute()
                if res.data:
                    return res.data[0]
            except Exception as e:
                logger.error(f"Supabase get_actor_by_id error: {e}")

        for a in self._memory_data["actors"]:
            if a.get("id") == actor_id or a.get("actor_code") == actor_id or a.get("primary_handle", "").lower() == actor_id.lower():
                return a
        return None

    # -------------------------------------------------------------------------
    # 3. ACTOR SUB-INTELLIGENCE
    # -------------------------------------------------------------------------
    def get_actor_handles(self, actor_id: str) -> List[Dict[str, Any]]:
        actor = self.get_actor_by_id(actor_id)
        if not actor:
            return []
        aid = actor["id"]
        if self.is_supabase_active:
            try:
                return self.supabase_client.table("actor_handles").select("*").eq("actor_id", aid).execute().data
            except Exception:
                pass
        return [h for h in self._memory_data["handles"] if h.get("actor_id") == aid]

    def get_actor_pgp(self, actor_id: str) -> List[Dict[str, Any]]:
        actor = self.get_actor_by_id(actor_id)
        if not actor:
            return []
        aid = actor["id"]
        if self.is_supabase_active:
            try:
                return self.supabase_client.table("pgp_keys").select("*").eq("actor_id", aid).execute().data
            except Exception:
                pass
        return [p for p in self._memory_data["pgp_keys"] if p.get("actor_id") == aid]

    def get_actor_wallets(self, actor_id: str) -> List[Dict[str, Any]]:
        actor = self.get_actor_by_id(actor_id)
        if not actor:
            return []
        aid = actor["id"]
        if self.is_supabase_active:
            try:
                return self.supabase_client.table("wallets").select("*").eq("actor_id", aid).execute().data
            except Exception:
                pass
        return [w for w in self._memory_data["wallets"] if w.get("actor_id") == aid]

    def get_actor_marketplaces(self, actor_id: str) -> List[Dict[str, Any]]:
        actor = self.get_actor_by_id(actor_id)
        if not actor:
            return []
        aid = actor["id"]
        
        # Link marketplaces
        links = [m for m in self._memory_data["actor_marketplaces"] if m.get("actor_id") == aid]
        all_markets = {m["id"]: m for m in self._memory_data["marketplaces"]}
        
        result = []
        for l in links:
            mid = l.get("marketplace_id")
            m_info = all_markets.get(mid, {})
            merged = {**m_info, **l}
            result.append(merged)
        return result

    def get_actor_infrastructure(self, actor_id: str) -> List[Dict[str, Any]]:
        actor = self.get_actor_by_id(actor_id)
        if not actor:
            return []
        aid = actor["id"]
        if self.is_supabase_active:
            try:
                return self.supabase_client.table("infrastructure_indicators").select("*").eq("actor_id", aid).execute().data
            except Exception:
                pass
        return [i for i in self._memory_data["infrastructure"] if i.get("actor_id") == aid]

    def get_actor_persona_profile(self, actor_id: str) -> Optional[Dict[str, Any]]:
        actor = self.get_actor_by_id(actor_id)
        if not actor:
            return None
        aid = actor["id"]
        for pp in self._memory_data["persona_profiles"]:
            if pp.get("actor_id") == aid:
                return pp
        return None

    def get_actor_relationships(self, actor_id: str) -> List[Dict[str, Any]]:
        actor = self.get_actor_by_id(actor_id)
        if not actor:
            return []
        code = actor["actor_code"]
        handle = actor["primary_handle"]
        
        # Collect edges where actor code or handle is source or target
        edges = []
        for r in self._memory_data["relationships"]:
            if r.get("source_id") in (code, handle, actor_id) or r.get("target_id") in (code, handle, actor_id):
                edges.append(r)
        return edges

    # -------------------------------------------------------------------------
    # 4. GLOBAL INFRASTRUCTURE
    # -------------------------------------------------------------------------
    def get_infrastructure(self, indicator_type: Optional[str] = None, search: Optional[str] = None) -> List[Dict[str, Any]]:
        infra = self._memory_data["infrastructure"]
        results = []
        for item in infra:
            if indicator_type and indicator_type != "all" and item.get("indicator_type") != indicator_type:
                continue
            if search:
                s = search.lower().strip()
                match = (
                    s in item.get("indicator_value", "").lower() or
                    s in item.get("indicator_type", "").lower() or
                    s in item.get("service_banner", "").lower() or
                    s in item.get("clearnet_association", "").lower() or
                    s in item.get("asn_organization", "").lower()
                )
                if not match:
                    continue
            results.append(item)
        return results

    # -------------------------------------------------------------------------
    # 5. PERSONA LINKS
    # -------------------------------------------------------------------------
    def get_persona_links(self, actor_id: Optional[str] = None) -> List[Dict[str, Any]]:
        links = self._memory_data["persona_links"]
        actors_dict = {a["id"]: a for a in self._memory_data["actors"]}
        
        enriched = []
        for pl in links:
            if actor_id:
                actor = self.get_actor_by_id(actor_id)
                if actor and pl.get("source_actor_id") != actor["id"] and pl.get("target_actor_id") != actor["id"]:
                    continue
            
            src = actors_dict.get(pl.get("source_actor_id"), {})
            tgt = actors_dict.get(pl.get("target_actor_id"), {})
            
            item = {
                **pl,
                "source_actor_code": src.get("actor_code", "UNKNOWN"),
                "source_primary_handle": src.get("primary_handle", "UNKNOWN"),
                "target_actor_code": tgt.get("actor_code", "UNKNOWN"),
                "target_primary_handle": tgt.get("primary_handle", "UNKNOWN")
            }
            enriched.append(item)
        return enriched

    # -------------------------------------------------------------------------
    # 6. TIMELINE & INTELLIGENCE EVENTS
    # -------------------------------------------------------------------------
    def get_intelligence_events(self, actor_id: Optional[str] = None, limit: Optional[int] = None) -> List[Dict[str, Any]]:
        events = self._memory_data["intelligence_events"]
        if actor_id:
            actor = self.get_actor_by_id(actor_id)
            if actor:
                events = [e for e in events if e.get("actor_id") == actor["id"]]
        
        # Sort chronologically reverse (newest first)
        sorted_events = sorted(events, key=lambda x: x.get("event_date", ""), reverse=True)
        if limit:
            return sorted_events[:limit]
        return sorted_events

    def get_timeline(self, actor_id: str) -> List[Dict[str, Any]]:
        return self.get_intelligence_events(actor_id=actor_id)

    # -------------------------------------------------------------------------
    # 7. SOURCES
    # -------------------------------------------------------------------------
    def get_sources(self) -> List[Dict[str, Any]]:
        return self._memory_data["sources"]

    # -------------------------------------------------------------------------
    # 8. RELATIONSHIPS & GRAPH DATA
    # -------------------------------------------------------------------------
    def get_full_graph_data(self) -> Dict[str, Any]:
        """Returns Cytoscape-formatted nodes and edges for the intelligence graph."""
        nodes = []
        edges = []
        node_ids = set()

        # Add Threat Actors
        for a in self._memory_data["actors"]:
            nid = a["actor_code"]
            if nid not in node_ids:
                node_ids.add(nid)
                nodes.append({
                    "data": {
                        "id": nid,
                        "label": a["primary_handle"],
                        "sublabel": a["actor_code"],
                        "type": "Threat Actor",
                        "category": a.get("category", ""),
                        "risk_score": float(a.get("risk_score", 50)),
                        "confidence": float(a.get("attribution_confidence", 70)),
                        "status": a.get("status", "Active")
                    }
                })

        # Add Handles
        for h in self._memory_data["handles"]:
            nid = h["handle"]
            if nid not in node_ids:
                node_ids.add(nid)
                nodes.append({
                    "data": {
                        "id": nid,
                        "label": h["handle"],
                        "sublabel": h["platform"],
                        "type": "Handle",
                        "role": h.get("observed_role", "Member"),
                        "confidence": float(h.get("confidence", 80))
                    }
                })

        # Add PGP Keys
        for p in self._memory_data["pgp_keys"]:
            nid = p["key_id"]
            if nid not in node_ids:
                node_ids.add(nid)
                nodes.append({
                    "data": {
                        "id": nid,
                        "label": p["key_id"],
                        "sublabel": p.get("key_fingerprint", "")[:19] + "...",
                        "type": "PGP Key",
                        "algorithm": p.get("key_algorithm", "RSA")
                    }
                })

        # Add Wallets
        for w in self._memory_data["wallets"]:
            addr = w["wallet_address"]
            nid = addr
            if nid not in node_ids:
                node_ids.add(nid)
                nodes.append({
                    "data": {
                        "id": nid,
                        "label": f"{w['currency']} {addr[:10]}...",
                        "sublabel": f"${w.get('total_received_usd', 0):,.0f} USD",
                        "type": "Wallet",
                        "currency": w["currency"],
                        "risk_level": w.get("risk_level", "High")
                    }
                })

        # Add Marketplaces
        for m in self._memory_data["marketplaces"]:
            nid = m["name"]
            if nid not in node_ids:
                node_ids.add(nid)
                nodes.append({
                    "data": {
                        "id": nid,
                        "label": m["name"],
                        "sublabel": m.get("market_type", "Forum"),
                        "type": "Marketplace",
                        "reputation": m.get("reputation_score", 80)
                    }
                })

        # Add Infrastructure
        for i in self._memory_data["infrastructure"]:
            nid = i["indicator_value"]
            if nid not in node_ids:
                node_ids.add(nid)
                nodes.append({
                    "data": {
                        "id": nid,
                        "label": i["indicator_value"][:25] + ("..." if len(i["indicator_value"]) > 25 else ""),
                        "sublabel": i["indicator_type"],
                        "type": "Infrastructure",
                        "confidence": float(i.get("confidence", 85))
                    }
                })

        # Add Edges
        for r in self._memory_data["relationships"]:
            # Ensure both source and target exist
            if r["source_id"] in node_ids and r["target_id"] in node_ids:
                edges.append({
                    "data": {
                        "id": r["id"],
                        "source": r["source_id"],
                        "target": r["target_id"],
                        "label": r["relationship_type"],
                        "relationship_type": r["relationship_type"],
                        "confidence": float(r.get("confidence_score", 85)),
                        "evidence": r.get("evidence_text", "Direct intelligence observation")
                    }
                })

        return {"nodes": nodes, "edges": edges}

# Singleton instance
db_service = DatabaseService()
