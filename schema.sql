-- =============================================================================
-- NTRO DARK WEB THREAT ACTOR DE-ANONYMIZATION & ATTRIBUTION PLATFORM (ID: 26151)
-- SUPABASE POSTGRESQL SCHEMA SPECIFICATION
-- DEFENSIVE CYBERSECURITY INTELLIGENCE SYSTEM
-- =============================================================================

-- Enable UUID extension
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";
CREATE EXTENSION IF NOT EXISTS "pgcrypto";

-- 1. USERS & ANALYSTS TABLE
CREATE TABLE IF NOT EXISTS users (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    username VARCHAR(100) UNIQUE NOT NULL,
    email VARCHAR(255) UNIQUE NOT NULL,
    full_name VARCHAR(150),
    role VARCHAR(50) DEFAULT 'threat_analyst', -- threat_analyst, lead_investigator, admin, auditor
    badge_number VARCHAR(50),
    created_at TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP,
    last_login TIMESTAMPTZ
);

-- 2. THREAT ACTORS CORE TABLE
CREATE TABLE IF NOT EXISTS threat_actors (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    actor_code VARCHAR(50) UNIQUE NOT NULL, -- e.g. TA-NIGHTFALCON-01
    primary_handle VARCHAR(100) NOT NULL,
    category VARCHAR(80) NOT NULL, -- Ransomware Affiliate, Initial Access Broker, Data Broker, Bulletproof Hosting, Carding Ring, Exploit Developer
    risk_score NUMERIC(5, 2) NOT NULL DEFAULT 50.00 CHECK (risk_score >= 0 AND risk_score <= 100),
    risk_level VARCHAR(20) GENERATED ALWAYS AS (
        CASE 
            WHEN risk_score >= 80 THEN 'Critical'
            WHEN risk_score >= 60 THEN 'High'
            WHEN risk_score >= 30 THEN 'Medium'
            ELSE 'Low'
        END
    ) STORED,
    attribution_confidence NUMERIC(5, 2) NOT NULL DEFAULT 65.00 CHECK (attribution_confidence >= 0 AND attribution_confidence <= 100),
    status VARCHAR(30) DEFAULT 'Active', -- Active, Dormant, Incarcerated, Monitored, Splintered
    operational_language VARCHAR(50) DEFAULT 'Russian/English',
    primary_timezone VARCHAR(50) DEFAULT 'UTC+3',
    threat_description TEXT,
    analyst_notes TEXT,
    first_seen TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP,
    last_seen TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP,
    created_at TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP
);

-- 3. ACTOR HANDLES / ALIASES
CREATE TABLE IF NOT EXISTS actor_handles (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    actor_id UUID NOT NULL REFERENCES threat_actors(id) ON DELETE CASCADE,
    handle VARCHAR(100) NOT NULL,
    platform VARCHAR(100) NOT NULL, -- Dread, Exploit.in, XSS.is, BreachForums, Telegram, Jabber, Matrix, TOX
    observed_role VARCHAR(100) DEFAULT 'Member', -- Admin, Escrow, Broker, Vendor, Member
    confidence NUMERIC(5, 2) DEFAULT 80.00,
    first_seen TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP,
    last_seen TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP,
    is_primary BOOLEAN DEFAULT FALSE,
    notes TEXT,
    created_at TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP
);

-- 4. PGP KEYS
CREATE TABLE IF NOT EXISTS pgp_keys (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    actor_id UUID REFERENCES threat_actors(id) ON DELETE SET NULL,
    key_fingerprint VARCHAR(100) UNIQUE NOT NULL,
    key_id VARCHAR(50) NOT NULL,
    key_size INTEGER DEFAULT 4096,
    key_algorithm VARCHAR(50) DEFAULT 'RSA',
    user_id_string TEXT,
    created_date TIMESTAMPTZ,
    expires_date TIMESTAMPTZ,
    revocation_status VARCHAR(30) DEFAULT 'Valid',
    raw_public_key TEXT,
    created_at TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP
);

-- 5. CRYPTOCURRENCY WALLETS
CREATE TABLE IF NOT EXISTS wallets (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    actor_id UUID REFERENCES threat_actors(id) ON DELETE SET NULL,
    currency VARCHAR(20) NOT NULL, -- BTC, XMR, ETH, USDT
    wallet_address VARCHAR(150) UNIQUE NOT NULL,
    cluster_label VARCHAR(150),
    total_received_usd NUMERIC(15, 2) DEFAULT 0.00,
    current_balance_usd NUMERIC(15, 2) DEFAULT 0.00,
    transaction_count INTEGER DEFAULT 0,
    first_activity TIMESTAMPTZ,
    last_activity TIMESTAMPTZ,
    risk_level VARCHAR(20) DEFAULT 'High',
    source_service VARCHAR(100) DEFAULT 'Mixer/Darknet Market',
    created_at TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP
);

-- 6. DARKNET MARKETPLACES & FORUMS
CREATE TABLE IF NOT EXISTS marketplaces (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    name VARCHAR(100) UNIQUE NOT NULL,
    market_type VARCHAR(50) DEFAULT 'Marketplace & Forum', -- Forum, Automated Vending, Marketplace, Escrow Service
    onion_address_v3 VARCHAR(150),
    clearnet_mirror VARCHAR(255),
    status VARCHAR(30) DEFAULT 'Active', -- Active, Seized, Exit Scammed, Inactive
    primary_category VARCHAR(100),
    first_indexed TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP,
    last_seen TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP,
    reputation_score NUMERIC(5, 2) DEFAULT 75.00,
    created_at TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP
);

-- 7. ACTOR - MARKETPLACE ASSOCIATION
CREATE TABLE IF NOT EXISTS actor_marketplaces (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    actor_id UUID NOT NULL REFERENCES threat_actors(id) ON DELETE CASCADE,
    marketplace_id UUID NOT NULL REFERENCES marketplaces(id) ON DELETE CASCADE,
    handle_used VARCHAR(100),
    vendor_tier VARCHAR(50) DEFAULT 'Verified Vendor',
    positive_feedback_pct NUMERIC(5, 2) DEFAULT 98.50,
    total_sales_count INTEGER DEFAULT 140,
    escrow_volume_usd NUMERIC(12, 2) DEFAULT 45000.00,
    active_since TIMESTAMPTZ,
    last_active TIMESTAMPTZ,
    status VARCHAR(30) DEFAULT 'Active',
    created_at TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP,
    UNIQUE(actor_id, marketplace_id)
);

-- 8. PASSIVE INFRASTRUCTURE INDICATORS
CREATE TABLE IF NOT EXISTS infrastructure_indicators (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    actor_id UUID REFERENCES threat_actors(id) ON DELETE SET NULL,
    indicator_type VARCHAR(50) NOT NULL, -- IPv4, Domain, Onion v3, JA3 Hash, TLS Hash, Favicon Hash, SSH Banner, ASN
    indicator_value VARCHAR(255) NOT NULL,
    service_banner TEXT,
    certificate_subject TEXT,
    certificate_issuer TEXT,
    clearnet_association VARCHAR(255),
    descriptor_status VARCHAR(50) DEFAULT 'Active Consensus',
    exposed_status_page_indicator VARCHAR(255),
    asn_number VARCHAR(50),
    asn_organization VARCHAR(150),
    hosting_country VARCHAR(50),
    confidence NUMERIC(5, 2) DEFAULT 75.00,
    source VARCHAR(100) DEFAULT 'Passive DNS & TLS Telemetry',
    first_seen TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP,
    last_seen TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP,
    created_at TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP
);

-- 9. PERSONA PROFILES & STYLOMETRY
CREATE TABLE IF NOT EXISTS persona_profiles (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    actor_id UUID NOT NULL REFERENCES threat_actors(id) ON DELETE CASCADE,
    primary_language VARCHAR(50) DEFAULT 'Russian',
    secondary_language VARCHAR(50) DEFAULT 'English (Broken)',
    avg_sentence_length NUMERIC(6, 2) DEFAULT 14.20,
    type_token_ratio NUMERIC(5, 4) DEFAULT 0.6840,
    punctuation_entropy NUMERIC(5, 4) DEFAULT 0.4512,
    active_hours_utc VARCHAR(100) DEFAULT '08:00 - 18:00 UTC',
    posting_frequency_score NUMERIC(5, 2) DEFAULT 82.50,
    signature_phrases TEXT[], -- Array of typical phrases/slang
    technical_jargon_profile JSONB,
    sample_corpus TEXT,
    created_at TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP
);

-- 10. PERSONA LINKS (ANALYTICAL ATTRIBUTION INDICATOR)
CREATE TABLE IF NOT EXISTS persona_links (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    source_actor_id UUID NOT NULL REFERENCES threat_actors(id) ON DELETE CASCADE,
    target_actor_id UUID NOT NULL REFERENCES threat_actors(id) ON DELETE CASCADE,
    writing_style_similarity NUMERIC(5, 2) NOT NULL,
    vocabulary_similarity NUMERIC(5, 2) NOT NULL,
    behaviour_similarity NUMERIC(5, 2) NOT NULL,
    activity_pattern_similarity NUMERIC(5, 2) NOT NULL,
    posting_frequency_similarity NUMERIC(5, 2) NOT NULL,
    overall_similarity NUMERIC(5, 2) NOT NULL,
    confidence_level VARCHAR(20) DEFAULT 'Medium', -- Low, Medium, High, Very High
    shared_indicators_count INTEGER DEFAULT 3,
    evidence_summary TEXT NOT NULL,
    analytical_disclaimer VARCHAR(255) DEFAULT 'Potential analytical linkage — not confirmed identity.',
    analyst_verified BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP
);

-- 11. ACTOR RELATIONSHIPS (GRAPH TOPOLOGY)
CREATE TABLE IF NOT EXISTS actor_relationships (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    source_id VARCHAR(100) NOT NULL,
    target_id VARCHAR(100) NOT NULL,
    source_type VARCHAR(50) NOT NULL, -- Threat Actor, Handle, PGP Key, Wallet, Marketplace, Infrastructure
    target_type VARCHAR(50) NOT NULL,
    relationship_type VARCHAR(80) NOT NULL, -- Uses Handle, Owns PGP Key, Associated Wallet, Active On Marketplace, Related Infrastructure, Potential Persona Link, Trust Relationship
    confidence_score NUMERIC(5, 2) DEFAULT 85.00,
    weight NUMERIC(5, 2) DEFAULT 1.0,
    evidence_text TEXT,
    first_observed TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP,
    last_observed TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP,
    created_at TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP
);

-- 12. INTELLIGENCE SOURCES (PROVENANCE & RELIABILITY)
CREATE TABLE IF NOT EXISTS sources (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    source_name VARCHAR(150) UNIQUE NOT NULL,
    source_type VARCHAR(80) NOT NULL, -- Public Report, Forum Metadata, Marketplace Metadata, Blockchain Intelligence, Infrastructure Intelligence, Research Dataset, Synthetic Demo Data
    reliability_score NUMERIC(5, 2) DEFAULT 88.00, -- 0 - 100
    source_url VARCHAR(255),
    ingestion_method VARCHAR(100) DEFAULT 'Automated Passive Ingestion',
    description TEXT,
    last_scanned TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP,
    created_at TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP
);

-- 13. INTELLIGENCE EVENTS (TIMELINE)
CREATE TABLE IF NOT EXISTS intelligence_events (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    actor_id UUID REFERENCES threat_actors(id) ON DELETE SET NULL,
    event_type VARCHAR(80) NOT NULL, -- First Seen, Handle changes, Marketplace activity, Wallet association, PGP key association, Infrastructure observations, Persona linkage, Exploit Release, Ransom Demand
    event_title VARCHAR(200) NOT NULL,
    event_description TEXT NOT NULL,
    severity VARCHAR(20) DEFAULT 'Medium', -- Low, Medium, High, Critical
    confidence NUMERIC(5, 2) DEFAULT 85.00,
    event_date TIMESTAMPTZ NOT NULL,
    source_id UUID REFERENCES sources(id) ON DELETE SET NULL,
    metadata JSONB,
    created_at TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP
);

-- 14. RISK ASSESSMENTS
CREATE TABLE IF NOT EXISTS risk_assessments (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    actor_id UUID NOT NULL REFERENCES threat_actors(id) ON DELETE CASCADE,
    infrastructure_risk NUMERIC(5, 2) NOT NULL,
    behavioural_risk NUMERIC(5, 2) NOT NULL,
    network_risk NUMERIC(5, 2) NOT NULL,
    activity_risk NUMERIC(5, 2) NOT NULL,
    total_risk_score NUMERIC(5, 2) NOT NULL,
    risk_level VARCHAR(20) NOT NULL DEFAULT 'High', -- Low, Medium, High, Critical
    assessed_by VARCHAR(100) DEFAULT 'Automated Risk Engine v2.4',
    rationale TEXT,
    assessment_date TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP
);

-- =============================================================================
-- PERFORMANCE INDEXES (REQUIRED)
-- =============================================================================
CREATE INDEX IF NOT EXISTS idx_threat_actors_actor_code ON threat_actors(actor_code);
CREATE INDEX IF NOT EXISTS idx_threat_actors_primary_handle ON threat_actors(primary_handle);
CREATE INDEX IF NOT EXISTS idx_threat_actors_risk_score ON threat_actors(risk_score);
CREATE INDEX IF NOT EXISTS idx_threat_actors_last_seen ON threat_actors(last_seen);
CREATE INDEX IF NOT EXISTS idx_wallets_wallet_address ON wallets(wallet_address);
CREATE INDEX IF NOT EXISTS idx_pgp_keys_key_fingerprint ON pgp_keys(key_fingerprint);
CREATE INDEX IF NOT EXISTS idx_actor_handles_handle ON actor_handles(handle);
CREATE INDEX IF NOT EXISTS idx_infra_indicator_value ON infrastructure_indicators(indicator_value);
CREATE INDEX IF NOT EXISTS idx_intelligence_events_date ON intelligence_events(event_date);
CREATE INDEX IF NOT EXISTS idx_relationships_source_target ON actor_relationships(source_id, target_id);
