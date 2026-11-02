-- =============================================================================
-- NTRO DARK WEB THREAT ACTOR DE-ANONYMIZATION PLATFORM
-- SQL SEED SCRIPT (SYNTHETIC DEMO DATA) - 100% VALID RFC 4122 HEX UUIDS
-- =============================================================================

-- Clean existing demo data safely
TRUNCATE TABLE risk_assessments, intelligence_events, actor_relationships, 
persona_links, persona_profiles, infrastructure_indicators, actor_marketplaces, 
marketplaces, wallets, pgp_keys, actor_handles, threat_actors, sources, users CASCADE;

-- 1. USERS (Prefix: 01000000)
INSERT INTO users (id, username, email, full_name, role, badge_number) VALUES
('01000000-0000-0000-0000-000000000001', 'analyst_arjun', 'arjun.sharma@ntro.gov.in', 'Arjun Sharma', 'lead_investigator', 'NTRO-CYBER-8841'),
('01000000-0000-0000-0000-000000000002', 'analyst_priya', 'priya.nair@ntro.gov.in', 'Priya Nair', 'threat_analyst', 'NTRO-CYBER-9204');

-- 2. THREAT ACTORS (Prefix: a1000000)
INSERT INTO threat_actors (id, actor_code, primary_handle, category, risk_score, attribution_confidence, status, operational_language, primary_timezone, threat_description, analyst_notes, first_seen, last_seen) VALUES
('a1000000-0000-0000-0000-000000000001', 'TA-NIGHTFALCON-01', 'NightFalcon', 'Ransomware Affiliate', 88.50, 82.00, 'Active', 'Russian / English', 'UTC+3 (Eastern Europe)', 'High-tier initial access broker and ransomware affiliate specializing in corporate network penetration via zero-day VPN exploits.', 'Correlated across Dread and Exploit.in forums.', '2023-01-14 09:30:00+00', '2026-08-20 14:15:00+00'),
('a1000000-0000-0000-0000-000000000002', 'TA-SHADOWBYTE-02', 'ShadowByte', 'Initial Access Broker', 76.00, 74.50, 'Active', 'English / Russian', 'UTC+2', 'Specializes in illicit Citrix and RDP gateway compromise, selling authenticated domain administrator sessions.', 'Strong stylometric similarity to legacy cluster ByteReaper.', '2023-04-10 11:20:00+00', '2026-08-22 19:45:00+00'),
('a1000000-0000-0000-0000-000000000003', 'TA-DARKORBIT-03', 'DarkOrbit_Ops', 'Bulletproof Hosting Provider', 92.00, 89.00, 'Active', 'Russian / Mandarin', 'UTC+7 / UTC+8', 'Operates resilient fast-flux Tor proxy networks and bulletproof VPS nodes across rogue ASNs.', 'Tied to multiple TLS certificate reuse signatures.', '2022-11-05 08:00:00+00', '2026-08-24 22:10:00+00'),
('a1000000-0000-0000-0000-000000000004', 'TA-CRYPTONOVA-04', 'CryptoNova_Laundering', 'Illicit Finance & Mixing', 84.00, 78.00, 'Active', 'English / Spanish', 'UTC-4', 'Facilitates multi-hop peel-chain transactions, cross-chain atomic swaps, and darknet mixing services.', 'High transaction volume observed through Wasabi wallet clusters.', '2023-08-19 16:45:00+00', '2026-08-23 06:30:00+00'),
('a1000000-0000-0000-0000-000000000005', 'TA-VOIDWALKER-05', 'VoidWalker_Dev', 'Exploit Developer', 95.50, 91.00, 'Active', 'Russian / German', 'UTC+1', 'Develops weaponized 1-day/0-day kernel escalation exploits and rootkits.', 'Distinctive cryptographic coding style and PGP fingerprint.', '2022-06-12 14:10:00+00', '2026-08-25 01:15:00+00'),
('a1000000-0000-0000-0000-000000000006', 'TA-SPECTREGHOST-06', 'SpectreGhost', 'Data Broker & Exfiltration', 68.00, 70.00, 'Monitored', 'English', 'UTC-5', 'Monetizes exfiltrated enterprise databases and healthcare records on underground forums.', 'Maintains static PGP subkey and sample formatting.', '2023-09-01 12:00:00+00', '2026-08-18 17:50:00+00'),
('a1000000-0000-0000-0000-000000000007', 'TA-NEBULAVIPER-07', 'NebulaViper', 'Carding Ring Operator', 58.50, 64.00, 'Dormant', 'Portuguese / English', 'UTC-3', 'Coordinates automated POS malware skim dumps and stolen credit cards.', 'Activity dropped significantly following seizure of partner marketplace.', '2023-02-18 20:10:00+00', '2026-07-11 10:05:00+00'),
('a1000000-0000-0000-0000-000000000008', 'TA-IRONCICADA-08', 'IronCicada', 'Supply Chain Threat Actor', 91.00, 85.50, 'Active', 'Mandarin / English', 'UTC+8', 'Injects malicious dependencies into public open-source libraries and targets CI/CD deployment pipelines.', 'Infrastructure overlaps with passive DNS clusters in Singapore.', '2023-10-30 04:25:00+00', '2026-08-24 18:40:00+00'),
('a1000000-0000-0000-0000-000000000009', 'TA-ASTRALPHANTOM-09', 'AstralPhantom', 'Ransomware-as-a-Service Core', 96.00, 94.00, 'Active', 'Russian', 'UTC+3', 'Core administrator of multi-extortion ransomware portal managing victim negotiations.', 'Uses hardened multi-signature escrow vaults.', '2022-03-10 10:00:00+00', '2026-08-25 08:20:00+00'),
('a1000000-0000-0000-0000-000000000010', 'TA-SYNTHCORONA-10', 'SynthCorona', 'Credential Stuffing & Botnet', 62.00, 68.00, 'Active', 'Turkish / English', 'UTC+3', 'Controls distributed residential proxy botnet executing brute-force credential stuffing.', 'Operates high-throughput Telegram verification bot.', '2024-01-05 15:30:00+00', '2026-08-21 13:40:00+00'),
('a1000000-0000-0000-0000-000000000011', 'TA-ZEROKEEPER-11', 'ZeroKeeper', 'Data Broker & Exfiltration', 52.00, 61.00, 'Monitored', 'English / Hindi', 'UTC+5:30', 'Aggregates leaked telecom PII records and sells targeted lookup APIs.', 'Identified through Jabber OTR fingerprint.', '2024-03-22 08:15:00+00', '2026-08-19 11:00:00+00'),
('a1000000-0000-0000-0000-000000000012', 'TA-KRAKEN-SEC-12', 'KrakenSec', 'Initial Access Broker', 79.50, 76.00, 'Active', 'Russian / Ukrainian', 'UTC+2', 'Deploys spear-phishing lures with weaponized SVG/OneNote attachments.', 'Collaborates frequently with TA-NIGHTFALCON-01 on staging.', '2023-07-14 13:00:00+00', '2026-08-23 16:20:00+00');

-- 3. SOURCES (Prefix: 05000000)
INSERT INTO sources (id, source_name, source_type, reliability_score, source_url, ingestion_method, description) VALUES
('05000000-0000-0000-0000-000000000001', 'Darknet Forum Metadata Feed', 'Forum Metadata', 92.00, 'https://intel.soc-hub.local/feeds/forum-metadata', 'Automated Passive Ingestion', 'Parses public discussion headers, PGP signatures, and handle timestamp activity.'),
('05000000-0000-0000-0000-000000000002', 'Passive DNS & TLS Certificate Stream', 'Infrastructure Intelligence', 96.00, 'https://crt.sh / Passive DNS Sensor Network', 'Real-time Telemetry Stream', 'Ingests newly issued TLS certificates and JA3 fingerprints.'),
('05000000-0000-0000-0000-000000000003', 'On-Chain Blockchain Ledger & Peel Tracer', 'Blockchain Intelligence', 98.00, 'https://blockstream.info / Monero Node', 'Automated Transaction Clustering', 'Monitors UTXO clusters and cross-chain bridge contracts.'),
('05000000-0000-0000-0000-000000000004', 'Tor Hidden Service Descriptor Archive', 'Infrastructure Intelligence', 90.00, 'https://metrics.torproject.org', 'Consensus Polling', 'Tracks publication of Onion v3 descriptors and uptime statistics.'),
('05000000-0000-0000-0000-000000000005', 'Public Threat Intel Advisories', 'Public Report', 85.00, 'https://cisa.gov / Mandiant / CrowdStrike', 'Structured STIX/TAXII Ingestion', 'Normalized threat actor profiles and IOC reports.');

-- 4. PGP KEYS (Prefix: 0b000000)
INSERT INTO pgp_keys (id, actor_id, key_fingerprint, key_id, key_size, key_algorithm, user_id_string, created_date, expires_date, revocation_status, raw_public_key) VALUES
('0b000000-0000-0000-0000-000000000001', 'a1000000-0000-0000-0000-000000000001', '7C3E A219 9F5D 47B1 8E6A  C0D4 55BF E790 3B21 99A1', '0x55BFE7903B2199A1', 4096, 'RSA', 'NightFalcon <nightfalcon@secmail.pro>', '2023-01-10 12:00:00+00', '2027-01-10 12:00:00+00', 'Valid', '-----BEGIN PGP PUBLIC KEY BLOCK-----\n[SYNTHETIC RSA 4096 BIT PGP KEY FOR NIGHTFALCON]\n-----END PGP PUBLIC KEY BLOCK-----'),
('0b000000-0000-0000-0000-000000000002', 'a1000000-0000-0000-0000-000000000002', '8F12 B574 D4A9 110C 3EE8  71AB 90C4 28EA 14DC FF88', '0x90C428EA14DCFF88', 4096, 'RSA', 'ShadowByte <sh4d0w@elude.in>', '2023-04-05 09:30:00+00', '2026-12-31 23:59:59+00', 'Valid', '-----BEGIN PGP PUBLIC KEY BLOCK-----\n[SYNTHETIC PGP KEY FOR SHADOWBYTE]\n-----END PGP PUBLIC KEY BLOCK-----'),
('0b000000-0000-0000-0000-000000000003', 'a1000000-0000-0000-0000-000000000003', '3D4C 9E81 7A25 6401 BF42  AA19 72E3 80DA 9912 C054', '0x72E380DA9912C054', 4096, 'ED25519', 'DarkOrbit Root Authority <darkorbit@cock.li>', '2022-11-01 15:00:00+00', '2028-11-01 15:00:00+00', 'Valid', '-----BEGIN PGP PUBLIC KEY BLOCK-----\n[SYNTHETIC ED25519 KEY FOR DARKORBIT]\n-----END PGP PUBLIC KEY BLOCK-----'),
('0b000000-0000-0000-0000-000000000009', 'a1000000-0000-0000-0000-000000000009', 'FA90 4118 7752 90BA D551  8821 9903 A45B 1102 CE99', '0x9903A45B1102CE99', 4096, 'RSA', 'Astral Master Lock <astral@ransomportal.biz>', '2022-03-01 10:00:00+00', '2027-03-01 10:00:00+00', 'Valid', '-----BEGIN PGP PUBLIC KEY BLOCK-----\n[SYNTHETIC PGP KEY FOR ASTRALPHANTOM]\n-----END PGP PUBLIC KEY BLOCK-----');

-- 5. WALLETS (Prefix: 0c000000)
INSERT INTO wallets (id, actor_id, currency, wallet_address, cluster_label, total_received_usd, current_balance_usd, transaction_count, risk_level, source_service, first_activity, last_activity) VALUES
('0c000000-0000-0000-0000-000000000001', 'a1000000-0000-0000-0000-000000000001', 'BTC', 'bc1qxy2kgdygjrsqtzq2n0yrf2493p83kkfjhx0wlh', 'NightFalcon Ransom Proceeds Cluster', 1425000.00, 384000.00, 86, 'Critical', 'Wasabi Mixer & Darknet Escrow', '2023-02-01 10:00:00+00', '2026-08-18 16:20:00+00'),
('0c000000-0000-0000-0000-000000000002', 'a1000000-0000-0000-0000-000000000001', 'XMR', '888tNkZrPN6JsEgekjMnABU4TBzc2Dt29EPAvkFxbTNsFoBkEhyGZndU23E99n79E5vKzZzR46X9X5yV6Jp8nK4A3bM9SYN', 'NightFalcon Direct Payout Monero', 850000.00, 620000.00, 142, 'Critical', 'Private Monero Node', '2023-03-15 12:00:00+00', '2026-08-20 14:00:00+00'),
('0c000000-0000-0000-0000-000000000003', 'a1000000-0000-0000-0000-000000000002', 'BTC', 'bc1q9v8h2km784z4qwhz0g4qjue7g68k9v28e578fa', 'ShadowByte Access Auction Payouts', 510000.00, 94000.00, 49, 'High', 'XSS Market Escrow', '2023-04-18 14:30:00+00', '2026-08-15 19:10:00+00'),
('0c000000-0000-0000-0000-000000000004', 'a1000000-0000-0000-0000-000000000004', 'BTC', 'bc1q5v49g8u52t3r22w788q68903v842r3h46s8912', 'CryptoNova Peel Chain Distributor', 12500000.00, 2400000.00, 1840, 'Critical', 'Cross-Chain Atomic Bridge', '2023-08-22 11:00:00+00', '2026-08-25 03:30:00+00'),
('0c000000-0000-0000-0000-000000000009', 'a1000000-0000-0000-0000-000000000009', 'BTC', 'bc1qar0srrr7xfkvy5l643lydnw9re59gtzzwf5mdq-astral', 'Astral Ransom Vault (Multi-sig 3-of-5)', 28400000.00, 6900000.00, 312, 'Critical', 'Deep Cold Storage', '2022-04-01 10:00:00+00', '2026-08-25 06:00:00+00');

-- 6. MARKETPLACES (Prefix: 0d000000)
INSERT INTO marketplaces (id, name, market_type, onion_address_v3, status, primary_category, reputation_score) VALUES
('0d000000-0000-0000-0000-000000000001', 'Dread Underground Forum', 'Forum & Intelligence Hub', 'dreadsub4x7k72pynq9fhl5z8m1a2b3c4d5e6f7g8h9i0j1k2l3m4n5o.onion', 'Active', 'Discussions, Escrow, Vulnerability Disclosure', 96.00),
('0d000000-0000-0000-0000-000000000002', 'Exploit.in Syndicate', 'Vulnerability & Access Brokerage', 'exploitv3node77a98bcdef1234567890abcdef1234567890abcdef.onion', 'Active', '0-Day/1-Day Exploits, Corporate Access', 94.00),
('0d000000-0000-0000-0000-000000000003', 'XSS.is Cyber Security Forum', 'Technical Forum & Access Escrow', 'xssforumv3a7b8c9d0e1f2g3h4i5j6k7l8m9n0p1q2r3s4t5u6v7w8.onion', 'Active', 'Malware Analysis, Access Brokers', 92.00),
('0d000000-0000-0000-0000-000000000004', 'BreachForums Reborn', 'Data Leak & PII Repository', 'breach2v3xyz987654321fedcba0987654321fedcba0987654321.onion', 'Active', 'SQL Dumps, Corporate Leaks', 88.00);

-- 7. ACTOR HANDLES (Prefix: 0e000000)
INSERT INTO actor_handles (id, actor_id, handle, platform, observed_role, confidence, is_primary) VALUES
('0e000000-0000-0000-0000-000000000001', 'a1000000-0000-0000-0000-000000000001', 'NightFalcon', 'Dread Forum', 'VIP Vendor', 95.00, TRUE),
('0e000000-0000-0000-0000-000000000002', 'a1000000-0000-0000-0000-000000000001', 'NF_Access_Broker', 'Exploit.in', 'Verified Seller', 90.00, FALSE),
('0e000000-0000-0000-0000-000000000004', 'a1000000-0000-0000-0000-000000000002', 'ShadowByte', 'XSS.is', 'IAB Specialist', 92.00, TRUE);

-- 8. INFRASTRUCTURE INDICATORS (Prefix: 0f000000)
INSERT INTO infrastructure_indicators (id, actor_id, indicator_type, indicator_value, service_banner, certificate_subject, clearnet_association, descriptor_status, exposed_status_page_indicator, asn_number, asn_organization, hosting_country, confidence, source) VALUES
('0f000000-0000-0000-0000-000000000001', 'a1000000-0000-0000-0000-000000000003', 'IPv4 Address', '185.220.101.45', 'SSH-2.0-OpenSSH_8.9p1 | nginx/1.24.0 (Fast-Flux Tor Relay)', 'CN=darkorbit-relay-node04.internal', 'relay04.orbit-secure-hosting.su', 'Active Tor Consensus Relay', 'HTTP/1.1 200 OK - /api/v1/healthz', 'AS49981', 'WorldStream B.V. Bulletproof Allocation', 'Netherlands', 92.00, 'Passive TLS Telemetry'),
('0f000000-0000-0000-0000-000000000002', 'a1000000-0000-0000-0000-000000000001', 'JA3 TLS Fingerprint', 'a0e9f5d64349fb13191bc781f81f42e1', 'TLS Client Hello: Cipher Suites Custom Go Handler', 'CN=vpn-gateway.falcon-net.org', 'vpn-gateway.falcon-net.org', 'Active C2 Listener', 'HTTP 404 Custom Go Handler', 'AS51167', 'Contabo GmbH Bulletproof Lease', 'Germany', 88.00, 'Passive Network Flow Feed');

-- 9. INTELLIGENCE EVENTS (Prefix: ee000000)
INSERT INTO intelligence_events (id, actor_id, event_type, event_title, event_description, severity, confidence, event_date) VALUES
('ee000000-0000-0000-0000-000000000001', 'a1000000-0000-0000-0000-000000000001', 'First Seen', 'NightFalcon First Registered on Dread Forum', 'Initial account registration detected under handle NightFalcon with RSA-4096 PGP key.', 'Low', 95.00, '2023-01-14 09:30:00+00'),
('ee000000-0000-0000-0000-000000000002', 'a1000000-0000-0000-0000-000000000001', 'Exploit Release', 'Zero-Day VPN Initial Access Listing', 'Published darknet auction for enterprise initial access.', 'Critical', 94.00, '2026-08-19 20:30:00+00');

-- 10. RISK ASSESSMENTS (Prefix: ff000000)
INSERT INTO risk_assessments (id, actor_id, infrastructure_risk, behavioural_risk, network_risk, activity_risk, total_risk_score, risk_level, assessed_by, rationale) VALUES
('ff000000-0000-0000-0000-000000000001', 'a1000000-0000-0000-0000-000000000001', 88.00, 92.00, 85.00, 89.00, 88.50, 'Critical', 'Automated Risk Engine v2.4', 'High volume corporate initial access brokering coupled with weaponized zero-day VPN exploit distribution.'),
('ff000000-0000-0000-0000-000000000002', 'a1000000-0000-0000-0000-000000000002', 74.00, 78.00, 72.00, 80.00, 76.00, 'High', 'Automated Risk Engine v2.4', 'Frequent RDP/Citrix gateway credential auctions on underground forums.'),
('ff000000-0000-0000-0000-000000000009', 'a1000000-0000-0000-0000-000000000009', 98.00, 96.00, 95.00, 95.00, 96.00, 'Critical', 'Automated Risk Engine v2.4', 'Core RaaS operator coordinating multi-million dollar corporate extortions.');
