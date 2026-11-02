"""
=============================================================================
NTRO DARK WEB THREAT ACTOR DE-ANONYMIZATION & ATTRIBUTION PLATFORM
SYNTHETIC DEMONSTRATION DATASET
=============================================================================
DISCLAIMER:
All entities, handles, wallet addresses, PGP keys, infrastructure indicators,
and timeline events in this file are completely FICTITIOUS and SYNTHETIC.
Designed strictly for defensive cybersecurity hackathon demonstration and testing.
"""

from datetime import datetime, timezone, timedelta

# Standard mock UUIDs for referential integrity
ACTORS_RAW = [
    {
        "id": "a1000000-0000-0000-0000-000000000001",
        "actor_code": "TA-NIGHTFALCON-01",
        "primary_handle": "NightFalcon",
        "category": "Ransomware Affiliate",
        "risk_score": 88.50,
        "attribution_confidence": 82.00,
        "status": "Active",
        "operational_language": "Russian / English",
        "primary_timezone": "UTC+3 (Eastern Europe)",
        "threat_description": "High-tier initial access broker and ransomware affiliate specializing in corporate network penetration via zero-day VPN exploits and enterprise credential harvesting.",
        "analyst_notes": "Correlated across Dread and Exploit.in forums. Uses distinct custom obfuscator header in malware payloads.",
        "first_seen": "2023-01-14T09:30:00Z",
        "last_seen": "2026-08-20T14:15:00Z"
    },
    {
        "id": "a1000000-0000-0000-0000-000000000002",
        "actor_code": "TA-SHADOWBYTE-02",
        "primary_handle": "ShadowByte",
        "category": "Initial Access Broker",
        "risk_score": 76.00,
        "attribution_confidence": 74.50,
        "status": "Active",
        "operational_language": "English / Russian",
        "primary_timezone": "UTC+2",
        "threat_description": "Specializes in illicit Citrix and RDP gateway compromise, selling authenticated domain administrator sessions on darknet escrow auctions.",
        "analyst_notes": "Strong stylometric similarity to legacy threat cluster 'ByteReaper'. Monitored on XSS.is.",
        "first_seen": "2023-04-10T11:20:00Z",
        "last_seen": "2026-08-22T19:45:00Z"
    },
    {
        "id": "a1000000-0000-0000-0000-000000000003",
        "actor_code": "TA-DARKORBIT-03",
        "primary_handle": "DarkOrbit_Ops",
        "category": "Bulletproof Hosting Provider",
        "risk_score": 92.00,
        "attribution_confidence": 89.00,
        "status": "Active",
        "operational_language": "Russian / Mandarin",
        "primary_timezone": "UTC+7 / UTC+8",
        "threat_description": "Operates resilient fast-flux Tor proxy networks, bulletproof VPS nodes, and automated cryptolocker C2 infrastructure across rogue ASNs.",
        "analyst_notes": "Tied to multiple TLS certificate reuse signatures and persistent JA3 fingerprints across 14 dark web mirrors.",
        "first_seen": "2022-11-05T08:00:00Z",
        "last_seen": "2026-08-24T22:10:00Z"
    },
    {
        "id": "a1000000-0000-0000-0000-000000000004",
        "actor_code": "TA-CRYPTONOVA-04",
        "primary_handle": "CryptoNova_Laundering",
        "category": "Illicit Finance & Mixing",
        "risk_score": 84.00,
        "attribution_confidence": 78.00,
        "status": "Active",
        "operational_language": "English / Spanish",
        "primary_timezone": "UTC-4",
        "threat_description": "Facilitates multi-hop peel-chain transactions, cross-chain atomic swaps (BTC -> XMR), and automated darknet mixing services for extortion proceeds.",
        "analyst_notes": "High transaction volume observed through Wasabi wallet clusters and decentralized cross-chain bridges.",
        "first_seen": "2023-08-19T16:45:00Z",
        "last_seen": "2026-08-23T06:30:00Z"
    },
    {
        "id": "a1000000-0000-0000-0000-000000000005",
        "actor_code": "TA-VOIDWALKER-05",
        "primary_handle": "VoidWalker_Dev",
        "category": "Exploit Developer",
        "risk_score": 95.50,
        "attribution_confidence": 91.00,
        "status": "Active",
        "operational_language": "Russian / German",
        "primary_timezone": "UTC+1",
        "threat_description": "Develops weaponized 1-day/0-day kernel escalation exploits, UEFI rootkits, and bespoke crypters bypassing modern EDR heuristic engines.",
        "analyst_notes": "Distinctive cryptographic coding style, PGP fingerprint embedded in early PoC leak on underground repository.",
        "first_seen": "2022-06-12T14:10:00Z",
        "last_seen": "2026-08-25T01:15:00Z"
    },
    {
        "id": "a1000000-0000-0000-0000-000000000006",
        "actor_code": "TA-SPECTREGHOST-06",
        "primary_handle": "SpectreGhost",
        "category": "Data Broker & Exfiltration",
        "risk_score": 68.00,
        "attribution_confidence": 70.00,
        "status": "Monitored",
        "operational_language": "English",
        "primary_timezone": "UTC-5",
        "threat_description": "Monetizes exfiltrated enterprise databases, healthcare records, and SQL injection dumps on BreachForums and Telegram escrow channels.",
        "analyst_notes": "Frequently changes Telegram handles but maintains static PGP subkey and identical sample file formatting.",
        "first_seen": "2023-09-01T12:00:00Z",
        "last_seen": "2026-08-18T17:50:00Z"
    },
    {
        "id": "a1000000-0000-0000-0000-000000000007",
        "actor_code": "TA-NEBULAVIPER-07",
        "primary_handle": "NebulaViper",
        "category": "Carding Ring Operator",
        "risk_score": 58.50,
        "attribution_confidence": 64.00,
        "status": "Dormant",
        "operational_language": "Portuguese / English",
        "primary_timezone": "UTC-3",
        "threat_description": "Coordinates automated POS malware skim dumps and stolen credit card credential validation bots on underground vending portals.",
        "analyst_notes": "Activity dropped significantly following seizure of partner marketplace in Q1 2026.",
        "first_seen": "2023-02-18T20:10:00Z",
        "last_seen": "2026-07-11T10:05:00Z"
    },
    {
        "id": "a1000000-0000-0000-0000-000000000008",
        "actor_code": "TA-IRONCICADA-08",
        "primary_handle": "IronCicada",
        "category": "Supply Chain Threat Actor",
        "risk_score": 91.00,
        "attribution_confidence": 85.50,
        "status": "Active",
        "operational_language": "Mandarin / English",
        "primary_timezone": "UTC+8",
        "threat_description": "Injects malicious dependencies into public NPM/PyPI open-source libraries and targets CI/CD deployment pipelines of cloud software vendors.",
        "analyst_notes": "Infrastructure overlaps with known passive DNS clusters in Singapore and Hong Kong VPS hosts.",
        "first_seen": "2023-10-30T04:25:00Z",
        "last_seen": "2026-08-24T18:40:00Z"
    },
    {
        "id": "a1000000-0000-0000-0000-000000000009",
        "actor_code": "TA-ASTRALPHANTOM-09",
        "primary_handle": "AstralPhantom",
        "category": "Ransomware-as-a-Service Core",
        "risk_score": 96.00,
        "attribution_confidence": 94.00,
        "status": "Active",
        "operational_language": "Russian",
        "primary_timezone": "UTC+3",
        "threat_description": "Core administrator of multi-extortion ransomware portal. Manages victim negotiation chats, decryptor key releases, and affiliate revenue splits.",
        "analyst_notes": "Primary target of multinational defensive tracking. Uses hardened multi-signature escrow wallets.",
        "first_seen": "2022-03-10T10:00:00Z",
        "last_seen": "2026-08-25T08:20:00Z"
    },
    {
        "id": "a1000000-0000-0000-0000-000000000010",
        "actor_code": "TA-SYNTHCORONA-10",
        "primary_handle": "SynthCorona",
        "category": "Credential Stuffing & Botnet",
        "risk_score": 62.00,
        "attribution_confidence": 68.00,
        "status": "Active",
        "operational_language": "Turkish / English",
        "primary_timezone": "UTC+3",
        "threat_description": "Controls distributed residential proxy botnet executing high-frequency brute-force credential stuffing against financial institutions.",
        "analyst_notes": "Operates high-throughput Telegram verification bot linked to synthetic USDT payout addresses.",
        "first_seen": "2024-01-05T15:30:00Z",
        "last_seen": "2026-08-21T13:40:00Z"
    },
    {
        "id": "a1000000-0000-0000-0000-000000000011",
        "actor_code": "TA-ZEROKEEPER-11",
        "primary_handle": "ZeroKeeper",
        "category": "Data Broker & Exfiltration",
        "risk_score": 52.00,
        "attribution_confidence": 61.00,
        "status": "Monitored",
        "operational_language": "English / Hindi",
        "primary_timezone": "UTC+5:30",
        "threat_description": "Aggregates leaked telecom PII records and sells targeted lookup APIs to underground identity fraud operators.",
        "analyst_notes": "Identified through recurring Jabber OTR fingerprint and stylistic phrasing on public breach channels.",
        "first_seen": "2024-03-22T08:15:00Z",
        "last_seen": "2026-08-19T11:00:00Z"
    },
    {
        "id": "a1000000-0000-0000-0000-000000000012",
        "actor_code": "TA-KRAKEN-SEC-12",
        "primary_handle": "KrakenSec",
        "category": "Initial Access Broker",
        "risk_score": 79.50,
        "attribution_confidence": 76.00,
        "status": "Active",
        "operational_language": "Russian / Ukrainian",
        "primary_timezone": "UTC+2",
        "threat_description": "Deploys spear-phishing lures with weaponized SVG/OneNote attachments to harvest corporate SSO and Azure AD sessions.",
        "analyst_notes": "Collaborates frequently with TA-NIGHTFALCON-01 on initial network access staging.",
        "first_seen": "2023-07-14T13:00:00Z",
        "last_seen": "2026-08-23T16:20:00Z"
    }
]

HANDLES_RAW = [
    # NightFalcon
    {"id": "h01", "actor_id": "a1000000-0000-0000-0000-000000000001", "handle": "NightFalcon", "platform": "Dread Forum", "observed_role": "VIP Vendor", "confidence": 95.0, "is_primary": True, "first_seen": "2023-01-14T09:30:00Z", "last_seen": "2026-08-20T14:15:00Z"},
    {"id": "h02", "actor_id": "a1000000-0000-0000-0000-000000000001", "handle": "NF_Access_Broker", "platform": "Exploit.in", "observed_role": "Verified Seller", "confidence": 90.0, "is_primary": False, "first_seen": "2023-03-20T11:00:00Z", "last_seen": "2026-08-15T18:00:00Z"},
    {"id": "h03", "actor_id": "a1000000-0000-0000-0000-000000000001", "handle": "falcon_ops_qtox", "platform": "TOX Messenger", "observed_role": "Direct Contact", "confidence": 85.0, "is_primary": False, "first_seen": "2023-06-01T10:00:00Z", "last_seen": "2026-08-19T20:00:00Z"},
    
    # ShadowByte
    {"id": "h04", "actor_id": "a1000000-0000-0000-0000-000000000002", "handle": "ShadowByte", "platform": "XSS.is", "observed_role": "IAB Specialist", "confidence": 92.0, "is_primary": True, "first_seen": "2023-04-10T11:20:00Z", "last_seen": "2026-08-22T19:45:00Z"},
    {"id": "h05", "actor_id": "a1000000-0000-0000-0000-000000000002", "handle": "sh4d0w_rdp", "platform": "Telegram", "observed_role": "Channel Admin", "confidence": 88.0, "is_primary": False, "first_seen": "2023-07-15T09:00:00Z", "last_seen": "2026-08-21T15:30:00Z"},
    {"id": "h06", "actor_id": "a1000000-0000-0000-0000-000000000002", "handle": "byte_reaper_v2", "platform": "BreachForums", "observed_role": "Member", "confidence": 72.0, "is_primary": False, "first_seen": "2023-11-01T14:00:00Z", "last_seen": "2026-05-10T12:00:00Z"},

    # DarkOrbit
    {"id": "h07", "actor_id": "a1000000-0000-0000-0000-000000000003", "handle": "DarkOrbit_Ops", "platform": "Dread Forum", "observed_role": "Bulletproof Host Admin", "confidence": 98.0, "is_primary": True, "first_seen": "2022-11-05T08:00:00Z", "last_seen": "2026-08-24T22:10:00Z"},
    {"id": "h08", "actor_id": "a1000000-0000-0000-0000-000000000003", "handle": "orbit_bulletproof_bot", "platform": "Telegram", "observed_role": "Automated Dispenser", "confidence": 91.0, "is_primary": False, "first_seen": "2023-01-20T16:00:00Z", "last_seen": "2026-08-24T21:00:00Z"},
    {"id": "h09", "actor_id": "a1000000-0000-0000-0000-000000000003", "handle": "orbit_c2_support", "platform": "Jabber / OTR", "observed_role": "Support Rep", "confidence": 84.0, "is_primary": False, "first_seen": "2023-05-12T13:00:00Z", "last_seen": "2026-08-23T11:00:00Z"},

    # CryptoNova
    {"id": "h10", "actor_id": "a1000000-0000-0000-0000-000000000004", "handle": "CryptoNova_Laundering", "platform": "Dread Forum", "observed_role": "Escrow / Mixer", "confidence": 94.0, "is_primary": True, "first_seen": "2023-08-19T16:45:00Z", "last_seen": "2026-08-23T06:30:00Z"},
    {"id": "h11", "actor_id": "a1000000-0000-0000-0000-000000000004", "handle": "nova_peel_service", "platform": "Telegram", "observed_role": "Bot Operator", "confidence": 89.0, "is_primary": False, "first_seen": "2023-10-02T19:00:00Z", "last_seen": "2026-08-20T22:00:00Z"},

    # VoidWalker
    {"id": "h12", "actor_id": "a1000000-0000-0000-0000-000000000005", "handle": "VoidWalker_Dev", "platform": "Exploit.in", "observed_role": "Senior Reverser", "confidence": 96.0, "is_primary": True, "first_seen": "2022-06-12T14:10:00Z", "last_seen": "2026-08-25T01:15:00Z"},
    {"id": "h13", "actor_id": "a1000000-0000-0000-0000-000000000005", "handle": "null_ptr_0x00", "platform": "XSS.is", "observed_role": "Kernel Coder", "confidence": 92.0, "is_primary": False, "first_seen": "2022-09-18T10:00:00Z", "last_seen": "2026-08-22T04:00:00Z"},
    {"id": "h14", "actor_id": "a1000000-0000-0000-0000-000000000005", "handle": "void_root_matrix", "platform": "Matrix", "observed_role": "Direct Contact", "confidence": 86.0, "is_primary": False, "first_seen": "2023-02-14T11:00:00Z", "last_seen": "2026-08-24T17:00:00Z"},

    # SpectreGhost
    {"id": "h15", "actor_id": "a1000000-0000-0000-0000-000000000006", "handle": "SpectreGhost", "platform": "BreachForums", "observed_role": "Data Broker", "confidence": 91.0, "is_primary": True, "first_seen": "2023-09-01T12:00:00Z", "last_seen": "2026-08-18T17:50:00Z"},
    {"id": "h16", "actor_id": "a1000000-0000-0000-0000-000000000006", "handle": "spectre_leaks_tg", "platform": "Telegram", "observed_role": "Channel Owner", "confidence": 87.0, "is_primary": False, "first_seen": "2023-11-20T08:00:00Z", "last_seen": "2026-08-17T14:00:00Z"},

    # NebulaViper
    {"id": "h17", "actor_id": "a1000000-0000-0000-0000-000000000007", "handle": "NebulaViper", "platform": "Nemesis Market", "observed_role": "CVV Vendor", "confidence": 88.0, "is_primary": True, "first_seen": "2023-02-18T20:10:00Z", "last_seen": "2026-07-11T10:05:00Z"},
    {"id": "h18", "actor_id": "a1000000-0000-0000-0000-000000000007", "handle": "viper_dumps_hub", "platform": "Telegram", "observed_role": "Vendor", "confidence": 79.0, "is_primary": False, "first_seen": "2023-05-01T18:00:00Z", "last_seen": "2026-06-30T16:00:00Z"},

    # IronCicada
    {"id": "h19", "actor_id": "a1000000-0000-0000-0000-000000000008", "handle": "IronCicada", "platform": "Darknet Trust Hub", "observed_role": "Supply Chain Op", "confidence": 93.0, "is_primary": True, "first_seen": "2023-10-30T04:25:00Z", "last_seen": "2026-08-24T18:40:00Z"},
    {"id": "h20", "actor_id": "a1000000-0000-0000-0000-000000000008", "handle": "cicada_npm_maintainer", "platform": "Public Git/Mirror", "observed_role": "Lurker/Dev", "confidence": 84.0, "is_primary": False, "first_seen": "2024-01-10T02:00:00Z", "last_seen": "2026-08-23T12:00:00Z"},

    # AstralPhantom
    {"id": "h21", "actor_id": "a1000000-0000-0000-0000-000000000009", "handle": "AstralPhantom", "platform": "Dread Forum", "observed_role": "RaaS Operator", "confidence": 99.0, "is_primary": True, "first_seen": "2022-03-10T10:00:00Z", "last_seen": "2026-08-25T08:20:00Z"},
    {"id": "h22", "actor_id": "a1000000-0000-0000-0000-000000000009", "handle": "astral_negotiation_desk", "platform": "TOX Messenger", "observed_role": "Ransom Negotiator", "confidence": 95.0, "is_primary": False, "first_seen": "2022-05-15T14:00:00Z", "last_seen": "2026-08-25T07:00:00Z"},

    # SynthCorona
    {"id": "h23", "actor_id": "a1000000-0000-0000-0000-000000000010", "handle": "SynthCorona", "platform": "Telegram", "observed_role": "Botnet Operator", "confidence": 89.0, "is_primary": True, "first_seen": "2024-01-05T15:30:00Z", "last_seen": "2026-08-21T13:40:00Z"},
    {"id": "h24", "actor_id": "a1000000-0000-0000-0000-000000000010", "handle": "corona_brute_api", "platform": "Exploit.in", "observed_role": "Service Seller", "confidence": 85.0, "is_primary": False, "first_seen": "2024-02-12T16:00:00Z", "last_seen": "2026-08-19T21:00:00Z"},

    # ZeroKeeper
    {"id": "h25", "actor_id": "a1000000-0000-0000-0000-000000000011", "handle": "ZeroKeeper", "platform": "BreachForums", "observed_role": "PII Reseller", "confidence": 82.0, "is_primary": True, "first_seen": "2024-03-22T08:15:00Z", "last_seen": "2026-08-19T11:00:00Z"},

    # KrakenSec
    {"id": "h26", "actor_id": "a1000000-0000-0000-0000-000000000012", "handle": "KrakenSec", "platform": "Exploit.in", "observed_role": "Phishing Specialist", "confidence": 91.0, "is_primary": True, "first_seen": "2023-07-14T13:00:00Z", "last_seen": "2026-08-23T16:20:00Z"},
    {"id": "h27", "actor_id": "a1000000-0000-0000-0000-000000000012", "handle": "kraken_session_shop", "platform": "XSS.is", "observed_role": "IAB Vendor", "confidence": 87.0, "is_primary": False, "first_seen": "2023-09-05T15:00:00Z", "last_seen": "2026-08-20T10:00:00Z"}
]

PGP_KEYS_RAW = [
    {
        "id": "p01",
        "actor_id": "a1000000-0000-0000-0000-000000000001",
        "key_fingerprint": "7C3E A219 9F5D 47B1 8E6A  C0D4 55BF E790 3B21 99A1",
        "key_id": "0x55BFE7903B2199A1",
        "key_size": 4096,
        "key_algorithm": "RSA (Encrypt/Sign)",
        "user_id_string": "NightFalcon <nightfalcon@secmail.pro>",
        "created_date": "2023-01-10T12:00:00Z",
        "expires_date": "2027-01-10T12:00:00Z",
        "revocation_status": "Valid",
        "raw_public_key": "-----BEGIN PGP PUBLIC KEY BLOCK-----\nVersion: Synthetic Demonstration Key v4.2\nComment: NTRO SIH-26151 Mock Security Indicator\nmQINBGO0A4kBEADK...[SYNTHETIC RSA 4096 BIT PGP KEY FOR NIGHTFALCON]...=\n-----END PGP PUBLIC KEY BLOCK-----"
    },
    {
        "id": "p02",
        "actor_id": "a1000000-0000-0000-0000-000000000002",
        "key_fingerprint": "8F12 B574 D4A9 110C 3EE8  71AB 90C4 28EA 14DC FF88",
        "key_id": "0x90C428EA14DCFF88",
        "key_size": 4096,
        "key_algorithm": "RSA",
        "user_id_string": "ShadowByte <sh4d0w@elude.in>",
        "created_date": "2023-04-05T09:30:00Z",
        "expires_date": "2026-12-31T23:59:59Z",
        "revocation_status": "Valid",
        "raw_public_key": "-----BEGIN PGP PUBLIC KEY BLOCK-----\nVersion: Synthetic Key Block\nComment: Demonstration Only\nmQINBGO7B5...[SYNTHETIC PGP KEY FOR SHADOWBYTE]...=\n-----END PGP PUBLIC KEY BLOCK-----"
    },
    {
        "id": "p03",
        "actor_id": "a1000000-0000-0000-0000-000000000003",
        "key_fingerprint": "3D4C 9E81 7A25 6401 BF42  AA19 72E3 80DA 9912 C054",
        "key_id": "0x72E380DA9912C054",
        "key_size": 4096,
        "key_algorithm": "ED25519 / Curve25519",
        "user_id_string": "DarkOrbit Root Authority <darkorbit@cock.li>",
        "created_date": "2022-11-01T15:00:00Z",
        "expires_date": "2028-11-01T15:00:00Z",
        "revocation_status": "Valid",
        "raw_public_key": "-----BEGIN PGP PUBLIC KEY BLOCK-----\n[SYNTHETIC ED25519 KEY FOR DARKORBIT]\n-----END PGP PUBLIC KEY BLOCK-----"
    },
    {
        "id": "p04",
        "actor_id": "a1000000-0000-0000-0000-000000000004",
        "key_fingerprint": "11E9 548A 2B01 9FF3 C852  00DA 471B 65DE 8891 22C4",
        "key_id": "0x471B65DE889122C4",
        "key_size": 4096,
        "key_algorithm": "RSA",
        "user_id_string": "CryptoNova Escrow <cryptonova@mail2tor.com>",
        "created_date": "2023-08-15T18:00:00Z",
        "expires_date": "2027-08-15T18:00:00Z",
        "revocation_status": "Valid",
        "raw_public_key": "-----BEGIN PGP PUBLIC KEY BLOCK-----\n[SYNTHETIC PGP KEY FOR CRYPTONOVA]\n-----END PGP PUBLIC KEY BLOCK-----"
    },
    {
        "id": "p05",
        "actor_id": "a1000000-0000-0000-0000-000000000005",
        "key_fingerprint": "A567 33D9 8B12 45EE 9180  CD55 18F2 90BC 44AA EF19",
        "key_id": "0x18F290BC44AAEF19",
        "key_size": 4096,
        "key_algorithm": "RSA",
        "user_id_string": "VoidWalker Coder <voidwalker@onionmail.org>",
        "created_date": "2022-06-01T08:00:00Z",
        "expires_date": "2026-06-01T08:00:00Z",
        "revocation_status": "Valid",
        "raw_public_key": "-----BEGIN PGP PUBLIC KEY BLOCK-----\n[SYNTHETIC PGP KEY FOR VOIDWALKER]\n-----END PGP PUBLIC KEY BLOCK-----"
    },
    {
        "id": "p06",
        "actor_id": "a1000000-0000-0000-0000-000000000006",
        "key_fingerprint": "59B1 CC82 0451 77E9 D4A2  8391 E801 7734 BC22 01FA",
        "key_id": "0xE8017734BC2201FA",
        "key_size": 4096,
        "key_algorithm": "RSA",
        "user_id_string": "SpectreGhost <spectre@dread.onion>",
        "created_date": "2023-08-28T14:30:00Z",
        "expires_date": "2027-08-28T14:30:00Z",
        "revocation_status": "Valid",
        "raw_public_key": "-----BEGIN PGP PUBLIC KEY BLOCK-----\n[SYNTHETIC PGP KEY FOR SPECTREGHOST]\n-----END PGP PUBLIC KEY BLOCK-----"
    },
    {
        "id": "p07",
        "actor_id": "a1000000-0000-0000-0000-000000000007",
        "key_fingerprint": "EE34 1902 4478 A901 B562  9812 3341 5567 AAAA 8821",
        "key_id": "0x33415567AAAA8821",
        "key_size": 2048,
        "key_algorithm": "RSA (Legacy)",
        "user_id_string": "NebulaViper <viper@autoshop.cc>",
        "created_date": "2023-02-10T11:00:00Z",
        "expires_date": "2025-02-10T11:00:00Z",
        "revocation_status": "Expired",
        "raw_public_key": "-----BEGIN PGP PUBLIC KEY BLOCK-----\n[SYNTHETIC PGP KEY FOR NEBULAVIPER]\n-----END PGP PUBLIC KEY BLOCK-----"
    },
    {
        "id": "p08",
        "actor_id": "a1000000-0000-0000-0000-000000000008",
        "key_fingerprint": "6612 FF89 1234 A554 9901  BC12 4490 1289 CCD1 5532",
        "key_id": "0x44901289CCD15532",
        "key_size": 4096,
        "key_algorithm": "RSA",
        "user_id_string": "IronCicada Team <cicada_core@secmail.pro>",
        "created_date": "2023-10-25T16:00:00Z",
        "expires_date": "2028-10-25T16:00:00Z",
        "revocation_status": "Valid",
        "raw_public_key": "-----BEGIN PGP PUBLIC KEY BLOCK-----\n[SYNTHETIC PGP KEY FOR IRONCICADA]\n-----END PGP PUBLIC KEY BLOCK-----"
    },
    {
        "id": "p09",
        "actor_id": "a1000000-0000-0000-0000-000000000009",
        "key_fingerprint": "FA90 4118 7752 90BA D551  8821 9903 A45B 1102 CE99",
        "key_id": "0x9903A45B1102CE99",
        "key_size": 4096,
        "key_algorithm": "RSA",
        "user_id_string": "Astral Master Lock <astral@ransomportal.biz>",
        "created_date": "2022-03-01T10:00:00Z",
        "expires_date": "2027-03-01T10:00:00Z",
        "revocation_status": "Valid",
        "raw_public_key": "-----BEGIN PGP PUBLIC KEY BLOCK-----\n[SYNTHETIC PGP KEY FOR ASTRALPHANTOM]\n-----END PGP PUBLIC KEY BLOCK-----"
    },
    {
        "id": "p10",
        "actor_id": "a1000000-0000-0000-0000-000000000012",
        "key_fingerprint": "2245 9981 BB34 1109 7753  ECA1 5591 0021 8847 DE01",
        "key_id": "0x559100218847DE01",
        "key_size": 4096,
        "key_algorithm": "RSA",
        "user_id_string": "KrakenSec <kraken@secure-vault.onion>",
        "created_date": "2023-07-10T12:00:00Z",
        "expires_date": "2026-12-31T23:59:59Z",
        "revocation_status": "Valid",
        "raw_public_key": "-----BEGIN PGP PUBLIC KEY BLOCK-----\n[SYNTHETIC PGP KEY FOR KRAKEN SEC]\n-----END PGP PUBLIC KEY BLOCK-----"
    }
]

WALLETS_RAW = [
    # NightFalcon
    {"id": "w01", "actor_id": "a1000000-0000-0000-0000-000000000001", "currency": "BTC", "wallet_address": "bc1qxy2kgdygjrsqtzq2n0yrf2493p83kkfjhx0wlh", "cluster_label": "NightFalcon Ransom Proceeds Cluster", "total_received_usd": 1425000.0, "current_balance_usd": 384000.0, "transaction_count": 86, "risk_level": "Critical", "source_service": "Wasabi Mixer & Darknet Escrow", "first_activity": "2023-02-01T10:00:00Z", "last_activity": "2026-08-18T16:20:00Z"},
    {"id": "w02", "actor_id": "a1000000-0000-0000-0000-000000000001", "currency": "XMR", "wallet_address": "888tNkZrPN6JsEgekjMnABU4TBzc2Dt29EPAvkFxbTNsFoBkEhyGZndU23E99n79E5vKzZzR46X9X5yV6Jp8nK4A3bM9SYN", "cluster_label": "NightFalcon Direct Payout Monero", "total_received_usd": 850000.0, "current_balance_usd": 620000.0, "transaction_count": 142, "risk_level": "Critical", "source_service": "Private Monero Node", "first_activity": "2023-03-15T12:00:00Z", "last_activity": "2026-08-20T14:00:00Z"},

    # ShadowByte
    {"id": "w03", "actor_id": "a1000000-0000-0000-0000-000000000002", "currency": "BTC", "wallet_address": "bc1q9v8h2km784z4qwhz0g4qjue7g68k9v28e578fa", "cluster_label": "ShadowByte Access Auction Payouts", "total_received_usd": 510000.0, "current_balance_usd": 94000.0, "transaction_count": 49, "risk_level": "High", "source_service": "XSS Market Escrow", "first_activity": "2023-04-18T14:30:00Z", "last_activity": "2026-08-15T19:10:00Z"},
    {"id": "w04", "actor_id": "a1000000-0000-0000-0000-000000000002", "currency": "USDT", "wallet_address": "0x71C8395982845c4C835492473919b6279E4571A1", "cluster_label": "Tether ERC-20 Staging", "total_received_usd": 220000.0, "current_balance_usd": 45000.0, "transaction_count": 31, "risk_level": "High", "source_service": "DEX Liquidity Pool", "first_activity": "2023-08-20T08:00:00Z", "last_activity": "2026-07-28T11:45:00Z"},

    # DarkOrbit
    {"id": "w05", "actor_id": "a1000000-0000-0000-0000-000000000003", "currency": "BTC", "wallet_address": "1A1zP1eP5QGefi2DMPTfTL5SLmv7DivfNa-mock-orbit", "cluster_label": "DarkOrbit Infrastructure Subscriptions", "total_received_usd": 3800000.0, "current_balance_usd": 1150000.0, "transaction_count": 420, "risk_level": "Critical", "source_service": "Automated Bulletproof Billing", "first_activity": "2022-11-10T18:00:00Z", "last_activity": "2026-08-24T20:15:00Z"},
    {"id": "w06", "actor_id": "a1000000-0000-0000-0000-000000000003", "currency": "XMR", "wallet_address": "44AFFq5kSiGBoZ4NMDwYtN18obc8AemS33DBLWs3H7otXft3XjrpDtQGZX7Mr4x9ORUJuCHELbGJZj8m515p9SYNTHORBIT", "cluster_label": "DarkOrbit Stealth Hosting Pool", "total_received_usd": 2100000.0, "current_balance_usd": 980000.0, "transaction_count": 310, "risk_level": "Critical", "source_service": "Monero Stealth Address", "first_activity": "2023-01-05T09:00:00Z", "last_activity": "2026-08-24T18:00:00Z"},

    # CryptoNova
    {"id": "w07", "actor_id": "a1000000-0000-0000-0000-000000000004", "currency": "BTC", "wallet_address": "bc1q5v49g8u52t3r22w788q68903v842r3h46s8912", "cluster_label": "CryptoNova Peel Chain Distributor", "total_received_usd": 12500000.0, "current_balance_usd": 2400000.0, "transaction_count": 1840, "risk_level": "Critical", "source_service": "Cross-Chain Atomic Bridge", "first_activity": "2023-08-22T11:00:00Z", "last_activity": "2026-08-25T03:30:00Z"},
    {"id": "w08", "actor_id": "a1000000-0000-0000-0000-000000000004", "currency": "ETH", "wallet_address": "0x4B0897b0513fdC7C541B6d9D7E929C4e5364D2dB", "cluster_label": "Tornado Mixer Relay Contract", "total_received_usd": 4800000.0, "current_balance_usd": 720000.0, "transaction_count": 520, "risk_level": "Critical", "source_service": "Smart Contract Relayer", "first_activity": "2023-09-10T14:00:00Z", "last_activity": "2026-08-23T05:00:00Z"},

    # VoidWalker
    {"id": "w09", "actor_id": "a1000000-0000-0000-0000-000000000005", "currency": "XMR", "wallet_address": "84nvT9uA2eKHg9E88N3t9S2kF8a7H9q2L5k8M9P4R7t3V2w1X6z4B8c2D5e7G9j1L3n5P7r9T1v3W5y7Z9SYNTHVOIDDEV", "cluster_label": "Zero-Day Exploit Bounty Address", "total_received_usd": 3200000.0, "current_balance_usd": 2800000.0, "transaction_count": 34, "risk_level": "Critical", "source_service": "Private Monero Wallet", "first_activity": "2022-07-01T10:00:00Z", "last_activity": "2026-08-24T23:00:00Z"},

    # SpectreGhost
    {"id": "w10", "actor_id": "a1000000-0000-0000-0000-000000000006", "currency": "BTC", "wallet_address": "3J98t1WpEZ73CNmQviecrnyiWrnqRhWNLy-synth-spec", "cluster_label": "Breach Dump Sales Escrow", "total_received_usd": 430000.0, "current_balance_usd": 68000.0, "transaction_count": 82, "risk_level": "Medium", "source_service": "Multi-sig P2SH Escrow", "first_activity": "2023-09-15T16:00:00Z", "last_activity": "2026-08-16T12:00:00Z"},

    # NebulaViper
    {"id": "w11", "actor_id": "a1000000-0000-0000-0000-000000000007", "currency": "USDT", "wallet_address": "TXj8F9k2L4n6P8r1T3v5W7y9Z2b4D6f8H0-mock-trc20", "cluster_label": "TRC-20 Automated Carding Payout", "total_received_usd": 290000.0, "current_balance_usd": 12000.0, "transaction_count": 190, "risk_level": "Medium", "source_service": "Tron Smart Contract", "first_activity": "2023-03-01T12:00:00Z", "last_activity": "2026-06-25T14:00:00Z"},

    # IronCicada
    {"id": "w12", "actor_id": "a1000000-0000-0000-0000-000000000008", "currency": "BTC", "wallet_address": "bc1qrp33g0q5c5txsp9dysnj4t594n6j852vl0g829", "cluster_label": "State-Sponsored Contract Retainer", "total_received_usd": 1800000.0, "current_balance_usd": 940000.0, "transaction_count": 18, "risk_level": "High", "source_service": "Overseas OTC Desk", "first_activity": "2023-11-12T08:00:00Z", "last_activity": "2026-08-22T09:00:00Z"},

    # AstralPhantom
    {"id": "w13", "actor_id": "a1000000-0000-0000-0000-000000000009", "currency": "BTC", "wallet_address": "bc1qar0srrr7xfkvy5l643lydnw9re59gtzzwf5mdq-astral", "cluster_label": "Astral Ransom Vault (Multi-sig 3-of-5)", "total_received_usd": 28400000.0, "current_balance_usd": 6900000.0, "transaction_count": 312, "risk_level": "Critical", "source_service": "Deep Cold Storage", "first_activity": "2022-04-01T10:00:00Z", "last_activity": "2026-08-25T06:00:00Z"},
    {"id": "w14", "actor_id": "a1000000-0000-0000-0000-000000000009", "currency": "XMR", "wallet_address": "82V7nKpR9bT3dE6gH8jM2wP4r7s9U1x3Z5y7B9D2F4H6J8L0N2P4R6T8V0X2Z4SYNTHASTRALMONERO", "cluster_label": "Astral Monero Ransom Settlement", "total_received_usd": 14200000.0, "current_balance_usd": 5100000.0, "transaction_count": 218, "risk_level": "Critical", "source_service": "High-Assurance Monero Node", "first_activity": "2022-06-15T14:00:00Z", "last_activity": "2026-08-25T07:30:00Z"},

    # SynthCorona & KrakenSec
    {"id": "w15", "actor_id": "a1000000-0000-0000-0000-000000000010", "currency": "USDT", "wallet_address": "0x3f5CE5FBFe3E9af3971dD833D26bA9b5C936f0bE", "cluster_label": "Botnet Subscription Gateway", "total_received_usd": 380000.0, "current_balance_usd": 42000.0, "transaction_count": 480, "risk_level": "Medium", "source_service": "Ethereum TRC Gateway", "first_activity": "2024-01-10T12:00:00Z", "last_activity": "2026-08-20T19:00:00Z"},
    {"id": "w16", "actor_id": "a1000000-0000-0000-0000-000000000012", "currency": "BTC", "wallet_address": "bc1q7y7r8x8u9w0v1z2a3b4c5d6e7f8g9h0i1j2k3l", "cluster_label": "Kraken Phishing Kit Sales", "total_received_usd": 680000.0, "current_balance_usd": 145000.0, "transaction_count": 75, "risk_level": "High", "source_service": "Samourai Whirlpool", "first_activity": "2023-08-01T15:00:00Z", "last_activity": "2026-08-22T17:00:00Z"}
]

MARKETPLACES_RAW = [
    {
        "id": "m01",
        "name": "Dread Underground Forum",
        "market_type": "Forum & Intelligence Hub",
        "onion_address_v3": "dreadsub4x7k72pynq9fhl5z8m1a2b3c4d5e6f7g8h9i0j1k2l3m4n5o.onion",
        "clearnet_mirror": "https://dread-archive-mirror.defensive-intel.local",
        "status": "Active",
        "primary_category": "Discussions, Escrow, Vulnerability Disclosure",
        "reputation_score": 96.0,
        "first_indexed": "2021-01-01T00:00:00Z",
        "last_seen": "2026-08-25T15:00:00Z"
    },
    {
        "id": "m02",
        "name": "Exploit.in Syndicate",
        "market_type": "Vulnerability & Access Brokerage",
        "onion_address_v3": "exploitv3node77a98bcdef1234567890abcdef1234567890abcdef.onion",
        "clearnet_mirror": "https://exploit-research.local",
        "status": "Active",
        "primary_category": "0-Day/1-Day Exploits, Corporate Access",
        "reputation_score": 94.0,
        "first_indexed": "2020-05-12T00:00:00Z",
        "last_seen": "2026-08-25T14:30:00Z"
    },
    {
        "id": "m03",
        "name": "XSS.is Cyber Security Forum",
        "market_type": "Technical Forum & Access Escrow",
        "onion_address_v3": "xssforumv3a7b8c9d0e1f2g3h4i5j6k7l8m9n0p1q2r3s4t5u6v7w8.onion",
        "clearnet_mirror": "https://xss-defensive-archive.local",
        "status": "Active",
        "primary_category": "Malware Analysis, Access Brokers, Stealer Logs",
        "reputation_score": 92.0,
        "first_indexed": "2020-08-10T00:00:00Z",
        "last_seen": "2026-08-25T13:45:00Z"
    },
    {
        "id": "m04",
        "name": "BreachForums Reborn",
        "market_type": "Data Leak & PII Repository",
        "onion_address_v3": "breach2v3xyz987654321fedcba0987654321fedcba0987654321.onion",
        "clearnet_mirror": "https://breachforums-intel-mirror.local",
        "status": "Active",
        "primary_category": "SQL Dumps, Corporate Leaks, Stolen Databases",
        "reputation_score": 88.0,
        "first_indexed": "2022-04-15T00:00:00Z",
        "last_seen": "2026-08-24T20:00:00Z"
    },
    {
        "id": "m05",
        "name": "Bohemia Reloaded Market",
        "market_type": "Commercial Darknet Marketplace",
        "onion_address_v3": "bohemia4v3node987123abc554433221100998877665544332211.onion",
        "clearnet_mirror": None,
        "status": "Active",
        "primary_category": "Digital Goods, Software, Escrow Services",
        "reputation_score": 85.0,
        "first_indexed": "2022-09-01T00:00:00Z",
        "last_seen": "2026-08-25T11:00:00Z"
    },
    {
        "id": "m06",
        "name": "Nemesis Autonomous Marketplace",
        "market_type": "Automated Vending Portal",
        "onion_address_v3": "nemesis5v3market7766554433221100aabbccddeeff0011223344.onion",
        "clearnet_mirror": None,
        "status": "Seized",
        "primary_category": "Carding Dumps, Counterfeit Credentials",
        "reputation_score": 45.0,
        "first_indexed": "2022-11-20T00:00:00Z",
        "last_seen": "2026-06-15T00:00:00Z"
    },
    {
        "id": "m07",
        "name": "Darknet Trust Hub",
        "market_type": "Decentralized Escrow & Reputation",
        "onion_address_v3": "trusthubv3escrow00112233445566778899aabbccddeeff001122.onion",
        "clearnet_mirror": "https://trusthub-metrics.local",
        "status": "Active",
        "primary_category": "Multi-sig Escrow, Vendor Verification",
        "reputation_score": 90.0,
        "first_indexed": "2023-01-10T00:00:00Z",
        "last_seen": "2026-08-25T16:00:00Z"
    },
    {
        "id": "m08",
        "name": "Genesis Reborn Portal",
        "market_type": "Bot Fingerprints & Session Marketplace",
        "onion_address_v3": "genesisv3bots00998877665544332211aabbccddeeff00112233.onion",
        "clearnet_mirror": None,
        "status": "Active",
        "primary_category": "Browser Fingerprints, Antidetect Profiles",
        "reputation_score": 89.0,
        "first_indexed": "2023-06-05T00:00:00Z",
        "last_seen": "2026-08-25T12:30:00Z"
    }
]

ACTOR_MARKETPLACES_RAW = [
    {"actor_id": "a1000000-0000-0000-0000-000000000001", "marketplace_id": "m01", "handle_used": "NightFalcon", "vendor_tier": "VIP Level 4", "positive_feedback_pct": 99.2, "total_sales_count": 215, "escrow_volume_usd": 680000.0, "status": "Active"},
    {"actor_id": "a1000000-0000-0000-0000-000000000001", "marketplace_id": "m02", "handle_used": "NF_Access_Broker", "vendor_tier": "Verified Seller", "positive_feedback_pct": 98.5, "total_sales_count": 84, "escrow_volume_usd": 420000.0, "status": "Active"},
    {"actor_id": "a1000000-0000-0000-0000-000000000002", "marketplace_id": "m02", "handle_used": "ShadowByte", "vendor_tier": "IAB Specialist", "positive_feedback_pct": 97.8, "total_sales_count": 62, "escrow_volume_usd": 310000.0, "status": "Active"},
    {"actor_id": "a1000000-0000-0000-0000-000000000002", "marketplace_id": "m03", "handle_used": "ShadowByte", "vendor_tier": "Senior Member", "positive_feedback_pct": 99.0, "total_sales_count": 48, "escrow_volume_usd": 190000.0, "status": "Active"},
    {"actor_id": "a1000000-0000-0000-0000-000000000003", "marketplace_id": "m01", "handle_used": "DarkOrbit_Ops", "vendor_tier": "Core Infrastructure Host", "positive_feedback_pct": 99.8, "total_sales_count": 520, "escrow_volume_usd": 2400000.0, "status": "Active"},
    {"actor_id": "a1000000-0000-0000-0000-000000000004", "marketplace_id": "m01", "handle_used": "CryptoNova_Laundering", "vendor_tier": "Certified Mixer", "positive_feedback_pct": 99.5, "total_sales_count": 940, "escrow_volume_usd": 8500000.0, "status": "Active"},
    {"actor_id": "a1000000-0000-0000-0000-000000000005", "marketplace_id": "m02", "handle_used": "VoidWalker_Dev", "vendor_tier": "Elite Exploit Author", "positive_feedback_pct": 100.0, "total_sales_count": 28, "escrow_volume_usd": 2900000.0, "status": "Active"},
    {"actor_id": "a1000000-0000-0000-0000-000000000006", "marketplace_id": "m04", "handle_used": "SpectreGhost", "vendor_tier": "Verified Data Broker", "positive_feedback_pct": 96.4, "total_sales_count": 130, "escrow_volume_usd": 380000.0, "status": "Active"},
    {"actor_id": "a1000000-0000-0000-0000-000000000007", "marketplace_id": "m06", "handle_used": "NebulaViper", "vendor_tier": "Auto-Shop Vendor", "positive_feedback_pct": 88.0, "total_sales_count": 310, "escrow_volume_usd": 240000.0, "status": "Seized"},
    {"actor_id": "a1000000-0000-0000-0000-000000000008", "marketplace_id": "m07", "handle_used": "IronCicada", "vendor_tier": "Enterprise Syndicate", "positive_feedback_pct": 98.9, "total_sales_count": 35, "escrow_volume_usd": 1500000.0, "status": "Active"},
    {"actor_id": "a1000000-0000-0000-0000-000000000009", "marketplace_id": "m01", "handle_used": "AstralPhantom", "vendor_tier": "RaaS Operator", "positive_feedback_pct": 99.9, "total_sales_count": 110, "escrow_volume_usd": 18000000.0, "status": "Active"},
    {"actor_id": "a1000000-0000-0000-0000-000000000010", "marketplace_id": "m08", "handle_used": "SynthCorona", "vendor_tier": "Botnet Supplier", "positive_feedback_pct": 94.2, "total_sales_count": 280, "escrow_volume_usd": 320000.0, "status": "Active"},
    {"actor_id": "a1000000-0000-0000-0000-000000000012", "marketplace_id": "m02", "handle_used": "KrakenSec", "vendor_tier": "IAB Tier 2", "positive_feedback_pct": 97.1, "total_sales_count": 68, "escrow_volume_usd": 480000.0, "status": "Active"}
]

INFRASTRUCTURE_RAW = [
    {
        "id": "i01",
        "actor_id": "a1000000-0000-0000-0000-000000000003",
        "indicator_type": "IPv4 Address",
        "indicator_value": "185.220.101.45",
        "service_banner": "SSH-2.0-OpenSSH_8.9p1 Ubuntu-3ubuntu0.4 | nginx/1.24.0 (Fast-Flux Tor Exit/Relay)",
        "certificate_subject": "CN=darkorbit-relay-node04.internal, O=Darknet Security Lab",
        "certificate_issuer": "Let's Encrypt Authority X3 / Synthetic Self-Signed",
        "clearnet_association": "relay04.orbit-secure-hosting.su",
        "descriptor_status": "Active Tor Consensus Relay",
        "exposed_status_page_indicator": "HTTP/1.1 200 OK - /api/v1/healthz (C2 Node Health)",
        "asn_number": "AS49981",
        "asn_organization": "WorldStream B.V. Bulletproof Allocation",
        "hosting_country": "Netherlands",
        "confidence": 92.0,
        "source": "Passive TLS Telemetry & Tor Descriptor Parser",
        "first_seen": "2023-02-14T08:00:00Z",
        "last_seen": "2026-08-24T22:15:00Z"
    },
    {
        "id": "i02",
        "actor_id": "a1000000-0000-0000-0000-000000000003",
        "indicator_type": "Onion v3 Address",
        "indicator_value": "orbitc2ctrl77a8b9c0d1e2f3g4h5i6j7k8l9m0n1p2q3r4s5t6u7v8w9x0.onion",
        "service_banner": "HTTP/1.1 401 Unauthorized - WWW-Authenticate: Basic realm=\"Orbit Management Gateway\"",
        "certificate_subject": "CN=orbit-gateway.onion",
        "certificate_issuer": "Self-Signed Onion TLS",
        "clearnet_association": "None (Darknet Hidden Service)",
        "descriptor_status": "Published Descriptor (Tor HSDir consensus)",
        "exposed_status_page_indicator": "Authenticated Login Portal for RaaS Operators",
        "asn_number": "N/A",
        "asn_organization": "Tor Hidden Service Protocol v3",
        "hosting_country": "Decentralized Onion Network",
        "confidence": 95.0,
        "source": "Passive Onion Indexer & Descriptor Archive",
        "first_seen": "2023-01-20T10:00:00Z",
        "last_seen": "2026-08-25T01:00:00Z"
    },
    {
        "id": "i03",
        "actor_id": "a1000000-0000-0000-0000-000000000001",
        "indicator_type": "JA3 TLS Fingerprint",
        "indicator_value": "a0e9f5d64349fb13191bc781f81f42e1",
        "service_banner": "TLS Client Hello: Cipher Suites [0x1301, 0x1302, 0x1303, 0xc02b, 0xc02f] (Go-http-client custom)",
        "certificate_subject": "CN=vpn-gateway.falcon-net.org",
        "certificate_issuer": "ZeroSSL RSA Domain Secure CA",
        "clearnet_association": "vpn-gateway.falcon-net.org",
        "descriptor_status": "Active C2 Listener",
        "exposed_status_page_indicator": "HTTP 404 Custom Go Handler",
        "asn_number": "AS51167",
        "asn_organization": "Contabo GmbH Bulletproof Lease",
        "hosting_country": "Germany",
        "confidence": 88.0,
        "source": "Passive Network Flow & JA3 Sensor Feed",
        "first_seen": "2023-05-18T14:30:00Z",
        "last_seen": "2026-08-20T16:00:00Z"
    },
    {
        "id": "i04",
        "actor_id": "a1000000-0000-0000-0000-000000000001",
        "indicator_type": "IPv4 Address",
        "indicator_value": "194.38.21.112",
        "service_banner": "SSH-2.0-OpenSSH_8.4p1 Debian-5+deb11u1 | Apache/2.4.56",
        "certificate_subject": "CN=staging-exfil-sinkhole.internal",
        "certificate_issuer": "Self-Signed",
        "clearnet_association": "data-collector.local-vpn.cc",
        "descriptor_status": "Stealth Staging Server",
        "exposed_status_page_indicator": "Directory Listing Disabled / 403 Forbidden",
        "asn_number": "AS200019",
        "asn_organization": "Alexhost SRL Bulletproof Colocation",
        "hosting_country": "Moldova",
        "confidence": 84.0,
        "source": "Passive DNS History & ASN BGP Monitor",
        "first_seen": "2023-09-10T12:00:00Z",
        "last_seen": "2026-08-19T18:40:00Z"
    },
    {
        "id": "i05",
        "actor_id": "a1000000-0000-0000-0000-000000000002",
        "indicator_type": "Favicon Hash (Murmur3)",
        "indicator_value": "-1254890123",
        "service_banner": "Guacamole Client Portal / RDP Tunnel Gateway (Apache Guacamole 1.5.2)",
        "certificate_subject": "CN=remote-access-portal.net",
        "certificate_issuer": "Let's Encrypt Authority",
        "clearnet_association": "rdp.secure-session-broker.is",
        "descriptor_status": "Active RDP Proxy",
        "exposed_status_page_indicator": "Guacamole Authentication Screen with Custom Dark CSS",
        "asn_number": "AS44592",
        "asn_organization": "Hostkey B.V.",
        "hosting_country": "Iceland",
        "confidence": 89.0,
        "source": "Passive Web Crawler & Favicon DB",
        "first_seen": "2023-06-25T11:00:00Z",
        "last_seen": "2026-08-22T21:00:00Z"
    },
    {
        "id": "i06",
        "actor_id": "a1000000-0000-0000-0000-000000000005",
        "indicator_type": "SSH Host Key Fingerprint",
        "indicator_value": "SHA256:uW3n7kP9v2mX1z5t8r4b0y6c8e0a2d4f6h8j0l2n4p6",
        "service_banner": "SSH-2.0-OpenSSH_9.2p1-hpn14v16 FreeBSD (Hardened Reverse Lab)",
        "certificate_subject": "N/A (SSH Key Authentication)",
        "certificate_issuer": "N/A",
        "clearnet_association": "dev-build-node.void-exploit.su",
        "descriptor_status": "High-Security Private Lab",
        "exposed_status_page_indicator": "Port 2222 Open, Public Key Only Auth",
        "asn_number": "AS197019",
        "asn_organization": "FlokiNET VPS Host",
        "hosting_country": "Romania",
        "confidence": 93.0,
        "source": "Passive SSH Banner Telemetry",
        "first_seen": "2022-08-14T06:00:00Z",
        "last_seen": "2026-08-24T23:50:00Z"
    },
    {
        "id": "i07",
        "actor_id": "a1000000-0000-0000-0000-000000000009",
        "indicator_type": "Onion v3 Address",
        "indicator_value": "astralleaks77node8899aabbccddeeff00112233445566778899aabb.onion",
        "service_banner": "HTTP/1.1 200 OK - Content-Type: text/html (Astral Ransom Public Shaming Blog)",
        "certificate_subject": "CN=astral-ransom-blog.onion",
        "certificate_issuer": "Self-Signed",
        "clearnet_association": "astral-leaks-mirror.cc",
        "descriptor_status": "Active Tor Consensus",
        "exposed_status_page_indicator": "Public Victim Countdown Clock & Torrent Download Links",
        "asn_number": "N/A",
        "asn_organization": "Tor Hidden Service",
        "hosting_country": "Decentralized Onion",
        "confidence": 98.0,
        "source": "Defensive Dark Web Threat Intel Feed",
        "first_seen": "2022-04-10T12:00:00Z",
        "last_seen": "2026-08-25T08:00:00Z"
    },
    {
        "id": "i08",
        "actor_id": "a1000000-0000-0000-0000-000000000008",
        "indicator_type": "Domain Name",
        "indicator_value": "cdn-package-resolver.cloud",
        "service_banner": "HTTP/2 200 OK - cloudflare-nginx / Custom Node.js Proxy",
        "certificate_subject": "CN=cdn-package-resolver.cloud",
        "certificate_issuer": "Cloudflare Inc ECC CA-3",
        "clearnet_association": "cdn-package-resolver.cloud -> 104.21.55.90",
        "descriptor_status": "Malicious Dependency Mirror",
        "exposed_status_page_indicator": "Mock NPM registry mirror returning backdoored tarballs",
        "asn_number": "AS13335",
        "asn_organization": "Cloudflare Anycast Proxy",
        "hosting_country": "United States / Global",
        "confidence": 91.0,
        "source": "Passive DNS & Certificate Transparency Logs",
        "first_seen": "2024-02-11T09:00:00Z",
        "last_seen": "2026-08-24T17:00:00Z"
    },
    {
        "id": "i09",
        "actor_id": "a1000000-0000-0000-0000-000000000010",
        "indicator_type": "IPv4 Address",
        "indicator_value": "45.154.255.89",
        "service_banner": "HTTP/1.1 200 OK - MikroTik RouterOS HTTP Proxy Bot Controller",
        "certificate_subject": "CN=router-os-proxy-node.net",
        "certificate_issuer": "Let's Encrypt",
        "clearnet_association": "bot-ctrl-01.synthnet.pw",
        "descriptor_status": "Botnet C2 Aggregator",
        "exposed_status_page_indicator": "REST API endpoint /api/v2/jobs for credential payloads",
        "asn_number": "AS48693",
        "asn_organization": "PQ Hosting S.R.L.",
        "hosting_country": "Moldova",
        "confidence": 86.0,
        "source": "Passive Shodan / Censys Telemetry Feed",
        "first_seen": "2024-03-01T10:00:00Z",
        "last_seen": "2026-08-21T18:00:00Z"
    },
    {
        "id": "i10",
        "actor_id": "a1000000-0000-0000-0000-000000000012",
        "indicator_type": "TLS Certificate SHA256",
        "indicator_value": "9a8b7c6d5e4f3a2b1c0d9e8f7a6b5c4d3e2f1a0b9c8d7e6f5a4b3c2d1e0f9a8b",
        "service_banner": "nginx/1.22.1 - Reverse Proxy for Evilginx3 Phishing Framework",
        "certificate_subject": "CN=login.microsoftonline.portal-sso-verify.com",
        "certificate_issuer": "Let's Encrypt Authority X3",
        "clearnet_association": "login.microsoftonline.portal-sso-verify.com",
        "descriptor_status": "Active Adversary-in-the-Middle (AiTM) Proxy",
        "exposed_status_page_indicator": "Replicates Microsoft 365 OAuth Login Interface",
        "asn_number": "AS206981",
        "asn_organization": "Kamatera Global Cloud",
        "hosting_country": "Netherlands",
        "confidence": 94.0,
        "source": "Passive Certificate Transparency & AiTM Telemetry",
        "first_seen": "2023-11-15T14:00:00Z",
        "last_seen": "2026-08-23T15:30:00Z"
    },
    {
        "id": "i11",
        "actor_id": "a1000000-0000-0000-0000-000000000004",
        "indicator_type": "Onion v3 Address",
        "indicator_value": "novamixer44node5566778899aabbccddeeff00112233445566778899.onion",
        "service_banner": "HTTP/1.1 200 OK - CryptoNova Automated Clean Coin Dispenser",
        "certificate_subject": "CN=novamixer.onion",
        "certificate_issuer": "Self-Signed",
        "clearnet_association": "novamixer-clearnet-status.net",
        "descriptor_status": "Active Tor Consensus",
        "exposed_status_page_indicator": "Deposit Address Generator & Fee Calculator",
        "asn_number": "N/A",
        "asn_organization": "Tor Hidden Service",
        "hosting_country": "Decentralized Onion",
        "confidence": 90.0,
        "source": "Passive Dark Web Spider",
        "first_seen": "2023-09-01T08:00:00Z",
        "last_seen": "2026-08-23T04:00:00Z"
    },
    {
        "id": "i12",
        "actor_id": "a1000000-0000-0000-0000-000000000006",
        "indicator_type": "IPv4 Address",
        "indicator_value": "193.106.191.24",
        "service_banner": "nginx/1.18.0 - Gofeed File Repository & Public Torrent Seeder",
        "certificate_subject": "CN=leaks-cdn-repo.biz",
        "certificate_issuer": "cPanel, Inc. Certification Authority",
        "clearnet_association": "leaks-cdn-repo.biz",
        "descriptor_status": "Public Exfiltration Mirror",
        "exposed_status_page_indicator": "HTTP 200 - File Storage Index for SQL dumps",
        "asn_number": "AS58061",
        "asn_organization": "Scalaxy LLC",
        "hosting_country": "Russian Federation",
        "confidence": 85.0,
        "source": "Passive DNS Records & WHOIS Logs",
        "first_seen": "2023-10-04T16:00:00Z",
        "last_seen": "2026-08-17T11:00:00Z"
    }
]

PERSONA_PROFILES_RAW = [
    {
        "id": "pp01",
        "actor_id": "a1000000-0000-0000-0000-000000000001",
        "primary_language": "Russian",
        "secondary_language": "English (Technical/Broken)",
        "avg_sentence_length": 12.8,
        "type_token_ratio": 0.694,
        "punctuation_entropy": 0.482,
        "active_hours_utc": "09:00 - 19:00 UTC",
        "posting_frequency_score": 88.0,
        "signature_phrases": ["work through escrow only", "guaranteed clean domain admin", "no logs retained", "ping jabber otr", "check signature with pgp"],
        "sample_corpus": "Selling verified VPN domain admin access for Tier-1 manufacturing conglomerate. Network mapped, EDR disabled via custom loader. Escrow only through Dread or Exploit admin. Ping via OTR on jabber or send encrypted PGP message."
    },
    {
        "id": "pp02",
        "actor_id": "a1000000-0000-0000-0000-000000000002",
        "primary_language": "Russian",
        "secondary_language": "English (Technical/Broken)",
        "avg_sentence_length": 13.4,
        "type_token_ratio": 0.681,
        "punctuation_entropy": 0.465,
        "active_hours_utc": "10:00 - 20:00 UTC",
        "posting_frequency_score": 82.0,
        "signature_phrases": ["escrow accepted", "domain admin verified", "no waste time", "check pgp key", "work with serious teams only"],
        "sample_corpus": "Offering fresh corporate access with domain admin credentials. Dual-homed domain controller reached. Strict escrow terms on XSS or Dread. Fast deal for serious ransomware teams."
    },
    {
        "id": "pp03",
        "actor_id": "a1000000-0000-0000-0000-000000000003",
        "primary_language": "Russian / English",
        "secondary_language": "Mandarin",
        "avg_sentence_length": 16.2,
        "type_token_ratio": 0.742,
        "punctuation_entropy": 0.510,
        "active_hours_utc": "06:00 - 22:00 UTC (Distributed Ops)",
        "posting_frequency_score": 94.0,
        "signature_phrases": ["bulletproof hosting 99.9% uptime", "no dmca ignore all abuse", "fast-flux dynamic tor", "api integration available", "pay via btc xmr"],
        "sample_corpus": "High reliability bulletproof infrastructure for high-traffic operations. Tor onion mirrors, fast-flux proxy relays, automated DDOS mitigation. 24/7 technical support over Jabber and Telegram."
    },
    {
        "id": "pp05",
        "actor_id": "a1000000-0000-0000-0000-000000000005",
        "primary_language": "English / Russian",
        "secondary_language": "German",
        "avg_sentence_length": 18.6,
        "type_token_ratio": 0.795,
        "punctuation_entropy": 0.580,
        "active_hours_utc": "14:00 - 02:00 UTC",
        "posting_frequency_score": 75.0,
        "signature_phrases": ["kernel privilege escalation", "edr unhooking technique", "zero-day payload assembly", "verified on latest patch", "strictly private sale"],
        "sample_corpus": "Releasing custom ring-0 kernel driver bypass targeting major enterprise EDR products. Clean compilation, zero heuristics triggered in automated sandbox testing. Serious inquiries only via Matrix."
    }
]

PERSONA_LINKS_RAW = [
    {
        "id": "pl01",
        "source_actor_id": "a1000000-0000-0000-0000-000000000001", # NightFalcon
        "target_actor_id": "a1000000-0000-0000-0000-000000000002", # ShadowByte
        "writing_style_similarity": 87.4,
        "vocabulary_similarity": 89.2,
        "behaviour_similarity": 84.0,
        "activity_pattern_similarity": 91.5,
        "posting_frequency_similarity": 86.0,
        "overall_similarity": 87.6,
        "confidence_level": "High",
        "shared_indicators_count": 5,
        "evidence_summary": "Identical phrasing in access broker listing templates ('guaranteed clean domain admin', 'work through escrow only'), matched UTC+3 activity windows, and shared PGP subkey generation parameters.",
        "analytical_disclaimer": "Potential analytical linkage — synthetic defensive attribution indicator. Not a confirmed real-world identity."
    },
    {
        "id": "pl02",
        "source_actor_id": "a1000000-0000-0000-0000-000000000001", # NightFalcon
        "target_actor_id": "a1000000-0000-0000-0000-000000000012", # KrakenSec
        "writing_style_similarity": 82.1,
        "vocabulary_similarity": 84.5,
        "behaviour_similarity": 80.0,
        "activity_pattern_similarity": 88.0,
        "posting_frequency_similarity": 81.5,
        "overall_similarity": 83.2,
        "confidence_level": "Medium",
        "shared_indicators_count": 4,
        "evidence_summary": "High correlation in initial access staging procedures and joint forum escrow deposits on Exploit.in.",
        "analytical_disclaimer": "Potential analytical linkage — synthetic defensive attribution indicator."
    },
    {
        "id": "pl03",
        "source_actor_id": "a1000000-0000-0000-0000-000000000001", # NightFalcon
        "target_actor_id": "a1000000-0000-0000-0000-000000000009", # AstralPhantom
        "writing_style_similarity": 74.0,
        "vocabulary_similarity": 76.5,
        "behaviour_similarity": 88.0,
        "activity_pattern_similarity": 85.0,
        "posting_frequency_similarity": 79.0,
        "overall_similarity": 80.5,
        "confidence_level": "High",
        "shared_indicators_count": 6,
        "evidence_summary": "Direct ransomware affiliate relationship; NightFalcon access tokens observed in Astral ransomware compromise deployments.",
        "analytical_disclaimer": "Potential analytical linkage — synthetic defensive attribution indicator."
    },
    {
        "id": "pl04",
        "source_actor_id": "a1000000-0000-0000-0000-000000000003", # DarkOrbit
        "target_actor_id": "a1000000-0000-0000-0000-000000000009", # AstralPhantom
        "writing_style_similarity": 71.0,
        "vocabulary_similarity": 73.0,
        "behaviour_similarity": 95.0,
        "activity_pattern_similarity": 92.0,
        "posting_frequency_similarity": 90.0,
        "overall_similarity": 84.2,
        "confidence_level": "Very High",
        "shared_indicators_count": 8,
        "evidence_summary": "DarkOrbit hosts AstralPhantom's victim leak portal and Tor onion negotiation gateways on shared AS49981 IP subnet.",
        "analytical_disclaimer": "Potential analytical linkage — synthetic defensive attribution indicator."
    },
    {
        "id": "pl05",
        "source_actor_id": "a1000000-0000-0000-0000-000000000004", # CryptoNova
        "target_actor_id": "a1000000-0000-0000-0000-000000000009", # AstralPhantom
        "writing_style_similarity": 68.0,
        "vocabulary_similarity": 70.2,
        "behaviour_similarity": 92.0,
        "activity_pattern_similarity": 89.0,
        "posting_frequency_similarity": 88.0,
        "overall_similarity": 81.4,
        "confidence_level": "High",
        "shared_indicators_count": 7,
        "evidence_summary": "Automated peel-chain transactions trace 75% of Astral extortion payouts through CryptoNova mixing relay contracts.",
        "analytical_disclaimer": "Potential analytical linkage — synthetic defensive attribution indicator."
    },
    {
        "id": "pl06",
        "source_actor_id": "a1000000-0000-0000-0000-000000000005", # VoidWalker
        "target_actor_id": "a1000000-0000-0000-0000-000000000001", # NightFalcon
        "writing_style_similarity": 79.5,
        "vocabulary_similarity": 82.0,
        "behaviour_similarity": 86.0,
        "activity_pattern_similarity": 78.0,
        "posting_frequency_similarity": 76.0,
        "overall_similarity": 80.3,
        "confidence_level": "Medium",
        "shared_indicators_count": 4,
        "evidence_summary": "VoidWalker crypter signatures uniquely utilized in NightFalcon access compromise packages.",
        "analytical_disclaimer": "Potential analytical linkage — synthetic defensive attribution indicator."
    }
]

RELATIONSHIPS_RAW = [
    # NightFalcon edges
    {"id": "r01", "source_id": "TA-NIGHTFALCON-01", "target_id": "NightFalcon", "source_type": "Threat Actor", "target_type": "Handle", "relationship_type": "Uses Handle", "confidence_score": 98.0, "evidence_text": "Primary persona verified across Dread forums and PGP signature keys."},
    {"id": "r02", "source_id": "TA-NIGHTFALCON-01", "target_id": "NF_Access_Broker", "source_type": "Threat Actor", "target_type": "Handle", "relationship_type": "Uses Handle", "confidence_score": 92.0, "evidence_text": "Secondary alias on Exploit.in forum with linked Jabber ID."},
    {"id": "r03", "source_id": "TA-NIGHTFALCON-01", "target_id": "0x55BFE7903B2199A1", "source_type": "Threat Actor", "target_type": "PGP Key", "relationship_type": "Owns PGP Key", "confidence_score": 99.0, "evidence_text": "Key fingerprint published on Dread user profile banner."},
    {"id": "r04", "source_id": "TA-NIGHTFALCON-01", "target_id": "bc1qxy2kgdygjrsqtzq2n0yrf2493p83kkfjhx0wlh", "source_type": "Threat Actor", "target_type": "Wallet", "relationship_type": "Associated Wallet", "confidence_score": 95.0, "evidence_text": "Deposit address provided in 4 verified escrow transactions."},
    {"id": "r05", "source_id": "TA-NIGHTFALCON-01", "target_id": "Dread Underground Forum", "source_type": "Threat Actor", "target_type": "Marketplace", "relationship_type": "Active On Marketplace", "confidence_score": 99.0, "evidence_text": "VIP Level 4 vendor with 215 verified sales."},
    {"id": "r06", "source_id": "TA-NIGHTFALCON-01", "target_id": "a0e9f5d64349fb13191bc781f81f42e1", "source_type": "Threat Actor", "target_type": "Infrastructure", "relationship_type": "Related Infrastructure", "confidence_score": 88.0, "evidence_text": "JA3 hash matches custom Go C2 loader deployed in recent campaigns."},
    {"id": "r07", "source_id": "TA-NIGHTFALCON-01", "target_id": "TA-SHADOWBYTE-02", "source_type": "Threat Actor", "target_type": "Threat Actor", "relationship_type": "Potential Persona Link", "confidence_score": 87.6, "evidence_text": "87.6% stylometric similarity, overlapping active timezone and shared access brokerage listings."},
    {"id": "r08", "source_id": "TA-NIGHTFALCON-01", "target_id": "TA-ASTRALPHANTOM-09", "source_type": "Threat Actor", "target_type": "Threat Actor", "relationship_type": "Trust Relationship", "confidence_score": 94.0, "evidence_text": "Verified affiliate in Astral Ransomware syndicate with shared revenue payouts."},

    # ShadowByte edges
    {"id": "r09", "source_id": "TA-SHADOWBYTE-02", "target_id": "ShadowByte", "source_type": "Threat Actor", "target_type": "Handle", "relationship_type": "Uses Handle", "confidence_score": 96.0, "evidence_text": "Primary handle on XSS.is and BreachForums."},
    {"id": "r10", "source_id": "TA-SHADOWBYTE-02", "target_id": "0x90C428EA14DCFF88", "source_type": "Threat Actor", "target_type": "PGP Key", "relationship_type": "Owns PGP Key", "confidence_score": 95.0, "evidence_text": "PGP signature verified on XSS.is verification thread."},
    {"id": "r11", "source_id": "TA-SHADOWBYTE-02", "target_id": "bc1q9v8h2km784z4qwhz0g4qjue7g68k9v28e578fa", "source_type": "Threat Actor", "target_type": "Wallet", "relationship_type": "Associated Wallet", "confidence_score": 91.0, "evidence_text": "Payout address on 49 access auctions."},
    {"id": "r12", "source_id": "TA-SHADOWBYTE-02", "target_id": "-1254890123", "source_type": "Threat Actor", "target_type": "Infrastructure", "relationship_type": "Related Infrastructure", "confidence_score": 89.0, "evidence_text": "Favicon Murmur3 hash matched Guacamole RDP staging gateway."},

    # DarkOrbit edges
    {"id": "r13", "source_id": "TA-DARKORBIT-03", "target_id": "DarkOrbit_Ops", "source_type": "Threat Actor", "target_type": "Handle", "relationship_type": "Uses Handle", "confidence_score": 99.0, "evidence_text": "Admin handle on Dread and Telegram support channels."},
    {"id": "r14", "source_id": "TA-DARKORBIT-03", "target_id": "185.220.101.45", "source_type": "Threat Actor", "target_type": "Infrastructure", "relationship_type": "Related Infrastructure", "confidence_score": 96.0, "evidence_text": "Core bulletproof relay IP registered to DarkOrbit operations."},
    {"id": "r15", "source_id": "TA-DARKORBIT-03", "target_id": "TA-ASTRALPHANTOM-09", "source_type": "Threat Actor", "target_type": "Threat Actor", "relationship_type": "Trust Relationship", "confidence_score": 95.0, "evidence_text": "Hosts Astral victim leak blogs and negotiation portals."},

    # CryptoNova edges
    {"id": "r16", "source_id": "TA-CRYPTONOVA-04", "target_id": "CryptoNova_Laundering", "source_type": "Threat Actor", "target_type": "Handle", "relationship_type": "Uses Handle", "confidence_score": 97.0, "evidence_text": "Official escrow handle on Dread Forum."},
    {"id": "r17", "source_id": "TA-CRYPTONOVA-04", "target_id": "bc1q5v49g8u52t3r22w788q68903v842r3h46s8912", "source_type": "Threat Actor", "target_type": "Wallet", "relationship_type": "Associated Wallet", "confidence_score": 98.0, "evidence_text": "Primary mixing cluster processing over $12.5M in illicit funds."},
    {"id": "r18", "source_id": "TA-CRYPTONOVA-04", "target_id": "TA-ASTRALPHANTOM-09", "source_type": "Threat Actor", "target_type": "Threat Actor", "relationship_type": "Trust Relationship", "confidence_score": 92.0, "evidence_text": "Processes extortion ransoms into privacy coins via automated peel chains."},

    # VoidWalker edges
    {"id": "r19", "source_id": "TA-VOIDWALKER-05", "target_id": "VoidWalker_Dev", "source_type": "Threat Actor", "target_type": "Handle", "relationship_type": "Uses Handle", "confidence_score": 98.0, "evidence_text": "Senior reverser profile on Exploit.in."},
    {"id": "r20", "source_id": "TA-VOIDWALKER-05", "target_id": "SHA256:uW3n7kP9v2mX1z5t8r4b0y6c8e0a2d4f6h8j0l2n4p6", "source_type": "Threat Actor", "target_type": "Infrastructure", "relationship_type": "Related Infrastructure", "confidence_score": 93.0, "evidence_text": "SSH host key on private exploit build server."},
    {"id": "r21", "source_id": "TA-VOIDWALKER-05", "target_id": "TA-NIGHTFALCON-01", "source_type": "Threat Actor", "target_type": "Threat Actor", "relationship_type": "Trust Relationship", "confidence_score": 86.0, "evidence_text": "Supplies customized EDR bypass loaders for initial access operations."},

    # AstralPhantom edges
    {"id": "r22", "source_id": "TA-ASTRALPHANTOM-09", "target_id": "AstralPhantom", "source_type": "Threat Actor", "target_type": "Handle", "relationship_type": "Uses Handle", "confidence_score": 99.0, "evidence_text": "Master RaaS brand administrator."},
    {"id": "r23", "source_id": "TA-ASTRALPHANTOM-09", "target_id": "0x9903A45B1102CE99", "source_type": "Threat Actor", "target_type": "PGP Key", "relationship_type": "Owns PGP Key", "confidence_score": 99.0, "evidence_text": "Master PGP key signing all victim ransom notes and decryptors."},
    {"id": "r24", "source_id": "TA-ASTRALPHANTOM-09", "target_id": "astralleaks77node8899aabbccddeeff00112233445566778899aabb.onion", "source_type": "Threat Actor", "target_type": "Infrastructure", "relationship_type": "Related Infrastructure", "confidence_score": 98.0, "evidence_text": "Official victim public extortion blog."},
    {"id": "r25", "source_id": "TA-ASTRALPHANTOM-09", "target_id": "bc1qar0srrr7xfkvy5l643lydnw9re59gtzzwf5mdq-astral", "source_type": "Threat Actor", "target_type": "Wallet", "relationship_type": "Associated Wallet", "confidence_score": 97.0, "evidence_text": "Cold storage vault containing $28.4M in ransom payments."},

    # Additional Graph Connections
    {"id": "r26", "source_id": "TA-IRONCICADA-08", "target_id": "cdn-package-resolver.cloud", "source_type": "Threat Actor", "target_type": "Infrastructure", "relationship_type": "Related Infrastructure", "confidence_score": 91.0, "evidence_text": "C2 mirror used for poisoned open-source package distribution."},
    {"id": "r27", "source_id": "TA-KRAKEN-SEC-12", "target_id": "9a8b7c6d5e4f3a2b1c0d9e8f7a6b5c4d3e2f1a0b9c8d7e6f5a4b3c2d1e0f9a8b", "source_type": "Threat Actor", "target_type": "Infrastructure", "relationship_type": "Related Infrastructure", "confidence_score": 94.0, "evidence_text": "TLS certificate fingerprint on active AiTM phishing proxy."},
    {"id": "r28", "source_id": "TA-SPECTREGHOST-06", "target_id": "BreachForums Reborn", "source_type": "Threat Actor", "target_type": "Marketplace", "relationship_type": "Active On Marketplace", "confidence_score": 93.0, "evidence_text": "Verified database vendor with 130 published data breaches."}
]

SOURCES_RAW = [
    {
        "id": "s01",
        "source_name": "Darknet Forum Metadata Feed (Dread & Exploit)",
        "source_type": "Forum Metadata",
        "reliability_score": 92.0,
        "source_url": "https://intel.soc-hub.local/feeds/forum-metadata",
        "ingestion_method": "Automated Passive Ingestion",
        "description": "Parses public discussion headers, PGP signatures, and handle timestamp activity from monitored underground forums."
    },
    {
        "id": "s02",
        "source_name": "Passive DNS & TLS Certificate Transparency Stream",
        "source_type": "Infrastructure Intelligence",
        "reliability_score": 96.0,
        "source_url": "https://crt.sh / Passive DNS Sensor Network",
        "ingestion_method": "Real-time Telemetry Stream",
        "description": "Ingests newly issued TLS certificates, JA3 fingerprints, and DNS resolution changes correlated with rogue ASNs."
    },
    {
        "id": "s03",
        "source_name": "On-Chain Blockchain Ledger & Peel-Chain Tracer",
        "source_type": "Blockchain Intelligence",
        "reliability_score": 98.0,
        "source_url": "https://blockstream.info / Monero Node Telemetry",
        "ingestion_method": "Automated Transaction Graph Clustering",
        "description": "Monitors UTXO clusters, Wasabi mixing coinjoins, and cross-chain bridge contracts linked to extortion addresses."
    },
    {
        "id": "s04",
        "source_name": "Tor Hidden Service Descriptor Archive",
        "source_type": "Infrastructure Intelligence",
        "reliability_score": 90.0,
        "source_url": "https://metrics.torproject.org / Synthetic Darknet Indexer",
        "ingestion_method": "Consensus Polling",
        "description": "Tracks publication of Onion v3 descriptors, uptime statistics, and introduction point changes across darknet markets."
    },
    {
        "id": "s05",
        "source_name": "Public Cybersecurity Threat Intel Reports",
        "source_type": "Public Report",
        "reliability_score": 85.0,
        "source_url": "https://cisa.gov / Mandiant / CrowdStrike Intelligence Advisories",
        "ingestion_method": "Structured STIX/TAXII Ingestion",
        "description": "Normalized threat actor profiles and IOC reports from global defensive research organizations."
    },
    {
        "id": "s06",
        "source_name": "Synthetic SOC Demonstration Dataset",
        "source_type": "Synthetic Demo Data",
        "reliability_score": 100.0,
        "source_url": "https://ntro.gov.in/sih-26151/demo-feed",
        "ingestion_method": "Internal Synthetic Seed",
        "description": "High-fidelity synthetic cybersecurity intelligence dataset generated strictly for SIH-26151 demonstration purposes."
    }
]

INTELLIGENCE_EVENTS_RAW = [
    {
        "id": "e01",
        "actor_id": "a1000000-0000-0000-0000-000000000001",
        "event_type": "First Seen",
        "event_title": "NightFalcon First Registered on Dread Forum",
        "event_description": "Initial account registration detected under handle 'NightFalcon' with RSA-4096 PGP key publication.",
        "severity": "Low",
        "confidence": 95.0,
        "event_date": "2023-01-14T09:30:00Z"
    },
    {
        "id": "e02",
        "actor_id": "a1000000-0000-0000-0000-000000000001",
        "event_type": "Handle changes",
        "event_title": "Expansion to Exploit.in as 'NF_Access_Broker'",
        "event_description": "Observed cross-posting corporate access auctions using identical PGP key fingerprint and OTR jabber contact.",
        "severity": "Medium",
        "confidence": 92.0,
        "event_date": "2023-03-20T11:00:00Z"
    },
    {
        "id": "e03",
        "actor_id": "a1000000-0000-0000-0000-000000000001",
        "event_type": "Wallet association",
        "event_title": "First Observed BTC Escrow Deposit",
        "event_description": "Wallet bc1qxy2kgdygjrsqtzq2n0yrf2493p83kkfjhx0wlh received 2.5 BTC deposit for enterprise VPN access sale.",
        "severity": "High",
        "confidence": 96.0,
        "event_date": "2023-04-18T14:00:00Z"
    },
    {
        "id": "e04",
        "actor_id": "a1000000-0000-0000-0000-000000000001",
        "event_type": "Infrastructure observations",
        "event_title": "JA3 Signature Match on Staging Server",
        "event_description": "JA3 hash a0e9f5d64349fb13191bc781f81f42e1 identified on IP 194.38.21.112 hosting Go-based exfiltration sinkhole.",
        "severity": "High",
        "confidence": 88.0,
        "event_date": "2023-09-10T12:00:00Z"
    },
    {
        "id": "e05",
        "actor_id": "a1000000-0000-0000-0000-000000000001",
        "event_type": "Persona linkage",
        "event_title": "Probabilistic Stylometric Correlation with ShadowByte",
        "event_description": "Persona engine identified 87.6% stylometric and behavioral similarity between NightFalcon and ShadowByte listing templates.",
        "severity": "Medium",
        "confidence": 87.6,
        "event_date": "2024-02-05T16:30:00Z"
    },
    {
        "id": "e06",
        "actor_id": "a1000000-0000-0000-0000-000000000001",
        "event_type": "Marketplace activity",
        "event_title": "Milestone: 200+ Verified Escrow Deals Reached",
        "event_description": "NightFalcon achieved VIP Level 4 status on Dread Forum with over $680K in cumulative trading volume.",
        "severity": "High",
        "confidence": 99.0,
        "event_date": "2025-06-15T18:00:00Z"
    },
    {
        "id": "e07",
        "actor_id": "a1000000-0000-0000-0000-000000000001",
        "event_type": "Exploit Release",
        "event_title": "Zero-Day VPN Initial Access Brokerage Listing",
        "event_description": "Published auction for unauthenticated RCE access targeting critical infrastructure enterprise network.",
        "severity": "Critical",
        "confidence": 94.0,
        "event_date": "2026-08-19T20:30:00Z"
    },

    # Additional chronological events across actors
    {
        "id": "e08",
        "actor_id": "a1000000-0000-0000-0000-000000000003",
        "event_type": "Infrastructure observations",
        "event_title": "DarkOrbit Fast-Flux Cluster Deployed on AS49981",
        "event_description": "Automated bulletproof proxy infrastructure expanded with 12 new Tor consensus exit nodes.",
        "severity": "Critical",
        "confidence": 96.0,
        "event_date": "2023-02-14T08:00:00Z"
    },
    {
        "id": "e09",
        "actor_id": "a1000000-0000-0000-0000-000000000004",
        "event_type": "Wallet association",
        "event_title": "CryptoNova Cross-Chain Mixing Pool Surpasses $10M Volume",
        "event_description": "On-chain transaction clustering detected massive peel-chain laundering throughput across BTC and XMR addresses.",
        "severity": "Critical",
        "confidence": 98.0,
        "event_date": "2024-05-20T11:00:00Z"
    },
    {
        "id": "e10",
        "actor_id": "a1000000-0000-0000-0000-000000000005",
        "event_type": "Exploit Release",
        "event_title": "VoidWalker Publishes Weaponized Kernel Driver PoC",
        "event_description": "Ring-0 kernel privilege escalation module bypassing crowd-scale EDR heuristics offered for $250K XMR.",
        "severity": "Critical",
        "confidence": 96.0,
        "event_date": "2024-11-12T17:00:00Z"
    },
    {
        "id": "e11",
        "actor_id": "a1000000-0000-0000-0000-000000000009",
        "event_type": "Ransom Demand",
        "event_title": "Astral RaaS Extorts Multinational Logistics Provider",
        "event_description": "Victim exfiltration data published on darknet leak site after 15 BTC ransom deadline lapsed.",
        "severity": "Critical",
        "confidence": 99.0,
        "event_date": "2025-09-04T08:00:00Z"
    },
    {
        "id": "e12",
        "actor_id": "a1000000-0000-0000-0000-000000000008",
        "event_type": "Infrastructure observations",
        "event_title": "IronCicada Malicious NPM Mirror Detected",
        "event_description": "Domain cdn-package-resolver.cloud identified delivering backdoored dependency tarballs to CI/CD pipelines.",
        "severity": "High",
        "confidence": 91.0,
        "event_date": "2026-02-11T09:00:00Z"
    },
    {
        "id": "e13",
        "actor_id": "a1000000-0000-0000-0000-000000000012",
        "event_type": "Infrastructure observations",
        "event_title": "KrakenSec AiTM Phishing Campaign Against Azure AD",
        "event_description": "Adversary-in-the-Middle reverse proxy certificate 9a8b7c... observed intercepting session cookies.",
        "severity": "High",
        "confidence": 94.0,
        "event_date": "2026-08-23T15:30:00Z"
    },
    {
        "id": "e14",
        "actor_id": "a1000000-0000-0000-0000-000000000006",
        "event_type": "Marketplace activity",
        "event_title": "SpectreGhost Leaks Healthcare Database on BreachForums",
        "event_description": "1.2 million patient PII records offered for immediate purchase via Telegram escrow.",
        "severity": "High",
        "confidence": 91.0,
        "event_date": "2026-08-16T12:00:00Z"
    },
    {
        "id": "e15",
        "actor_id": "a1000000-0000-0000-0000-000000000010",
        "event_type": "Infrastructure observations",
        "event_title": "SynthCorona Botnet Spike: 50,000 Credential Probes/Hr",
        "event_description": "Distributed residential proxy swarm detected spraying credentials against banking portals.",
        "severity": "Medium",
        "confidence": 86.0,
        "event_date": "2026-08-21T18:00:00Z"
    }
]

# Quick helper to get complete in-memory data
def get_synthetic_dataset():
    return {
        "actors": list(ACTORS_RAW),
        "handles": list(HANDLES_RAW),
        "pgp_keys": list(PGP_KEYS_RAW),
        "wallets": list(WALLETS_RAW),
        "marketplaces": list(MARKETPLACES_RAW),
        "actor_marketplaces": list(ACTOR_MARKETPLACES_RAW),
        "infrastructure": list(INFRASTRUCTURE_RAW),
        "persona_profiles": list(PERSONA_PROFILES_RAW),
        "persona_links": list(PERSONA_LINKS_RAW),
        "relationships": list(RELATIONSHIPS_RAW),
        "sources": list(SOURCES_RAW),
        "intelligence_events": list(INTELLIGENCE_EVENTS_RAW)
    }
