/**
 * Actor Detail 11-Tab Controller & Asynchronous Intelligence Loader
 */

document.addEventListener('DOMContentLoaded', () => {
  const actorId = document.getElementById('current-actor-id')?.value;
  if (!actorId) return;

  // Initialize Tab Switchers
  const tabBtns = document.querySelectorAll('.actor-tab-btn');
  tabBtns.forEach(btn => {
    btn.addEventListener('click', () => {
      tabBtns.forEach(b => b.classList.remove('active'));
      document.querySelectorAll('.tab-pane').forEach(pane => pane.classList.remove('active'));

      btn.classList.add('active');
      const targetTab = btn.getAttribute('data-tab');
      const pane = document.getElementById(targetTab);
      if (pane) pane.classList.add('active');
    });
  });

  // Load all intelligence data for the actor
  loadAllActorIntelligence(actorId);
});

async function loadAllActorIntelligence(actorId) {
  try {
    // 1. Handles
    const handlesRes = await fetch(`/api/actors/${actorId}/handles`);
    const handlesData = (await handlesRes.json()).data || [];
    renderHandles(handlesData);
    document.getElementById('overview-count-handles').innerText = handlesData.length;

    // 2. PGP Keys
    const pgpRes = await fetch(`/api/actors/${actorId}/pgp`);
    const pgpData = (await pgpRes.json()).data || [];
    renderPGP(pgpData);
    document.getElementById('overview-count-pgp').innerText = pgpData.length;

    // 3. Wallets
    const walletsRes = await fetch(`/api/actors/${actorId}/wallets`);
    const walletsData = (await walletsRes.json()).data || [];
    renderWallets(walletsData);
    document.getElementById('overview-count-wallets').innerText = walletsData.length;

    // 4. Marketplaces
    const marketRes = await fetch(`/api/actors/${actorId}/marketplaces`);
    const marketData = (await marketRes.json()).data || [];
    renderMarketplaces(marketData);

    // 5. Infrastructure
    const infraRes = await fetch(`/api/actors/${actorId}/infrastructure`);
    const infraData = (await infraRes.json()).data || [];
    renderInfrastructure(infraData);
    document.getElementById('overview-count-infra').innerText = infraData.length;

    // 6. Relationships
    const relRes = await fetch(`/api/actors/${actorId}/relationships`);
    const relData = (await relRes.json()).data || [];
    renderRelationships(relData);
    document.getElementById('overview-count-relations').innerText = relData.length;

    // 7. Timeline
    const timeRes = await fetch(`/api/timeline/${actorId}`);
    const timeData = (await timeRes.json()).data || [];
    renderTimeline(timeData);

    // 8. Persona Profile & Evidence
    renderPersonaAndEvidence(actorId, handlesData, pgpData, walletsData, infraData);

    // 9. Sources
    renderSourcesTab();

  } catch (err) {
    console.error('Error loading actor intelligence dossier:', err);
    if (window.showToast) window.showToast('Failed to load complete actor dossier', 'danger');
  }
}

function renderHandles(handles) {
  const tbody = document.getElementById('handles-tbody');
  if (!tbody) return;
  if (handles.length === 0) {
    tbody.innerHTML = `<tr><td colspan="7" style="text-align:center; color: var(--text-muted); padding: 20px;">No secondary handles identified.</td></tr>`;
    return;
  }
  tbody.innerHTML = handles.map(h => `
    <tr>
      <td><strong style="color: #fff;">${h.handle}</strong></td>
      <td><span style="color: var(--cyber-cyan); font-size: 0.8rem;">${h.platform}</span></td>
      <td>${h.observed_role || 'Member'}</td>
      <td><span class="font-mono">${h.confidence}%</span></td>
      <td>${h.is_primary ? '<span class="status-badge status-active">Primary</span>' : '<span style="color: var(--text-muted); font-size: 0.75rem;">Alias</span>'}</td>
      <td class="font-mono" style="font-size: 0.75rem; color: var(--text-muted);">${h.first_seen ? h.first_seen.split('T')[0] : 'N/A'}</td>
      <td class="font-mono" style="font-size: 0.75rem; color: var(--text-secondary);">${h.last_seen ? h.last_seen.split('T')[0] : 'N/A'}</td>
    </tr>
  `).join('');
}

function renderPGP(pgpKeys) {
  const container = document.getElementById('pgp-container');
  if (!container) return;
  if (pgpKeys.length === 0) {
    container.innerHTML = `<div style="text-align:center; color: var(--text-muted); padding: 20px;">No PGP public keys registered for this actor.</div>`;
    return;
  }
  container.innerHTML = pgpKeys.map(p => `
    <div style="background: rgba(0, 0, 0, 0.35); border: 1px solid var(--border-card); border-radius: 8px; padding: 18px;">
      <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 10px;">
        <div style="font-size: 0.95rem; font-weight: 700; color: var(--cyber-amber); font-family: var(--font-mono);">
          <i class="fa-solid fa-key" style="margin-right: 6px;"></i> Key ID: ${p.key_id}
        </div>
        <span class="status-badge status-active">${p.revocation_status || 'Valid'}</span>
      </div>
      <div style="margin-bottom: 8px; font-size: 0.85rem;">
        <span style="color: var(--text-muted);">User ID:</span> <strong style="color: #fff;">${p.user_id_string || 'Anonymous'}</strong>
      </div>
      <div style="margin-bottom: 12px; font-size: 0.8rem; font-family: var(--font-mono); color: var(--cyber-cyan); background: rgba(0, 240, 255, 0.05); padding: 6px 10px; border-radius: 4px;">
        Fingerprint: ${p.key_fingerprint}
      </div>
      <pre style="background: rgba(0, 0, 0, 0.6); padding: 12px; border-radius: 6px; font-size: 0.72rem; color: var(--text-secondary); overflow-x: auto; border: 1px solid rgba(255,255,255,0.05);">${p.raw_public_key || '-----BEGIN PGP PUBLIC KEY BLOCK-----\n[PUBLIC KEY]\n-----END PGP PUBLIC KEY BLOCK-----'}</pre>
    </div>
  `).join('');
}

function renderWallets(wallets) {
  const tbody = document.getElementById('wallets-tbody');
  if (!tbody) return;
  if (wallets.length === 0) {
    tbody.innerHTML = `<tr><td colspan="7" style="text-align:center; color: var(--text-muted); padding: 20px;">No cryptocurrency wallets observed.</td></tr>`;
    return;
  }
  tbody.innerHTML = wallets.map(w => `
    <tr>
      <td><span class="font-mono" style="font-weight: 700; color: var(--cyber-amber);">${w.currency}</span></td>
      <td><span class="font-mono" style="font-size: 0.78rem; color: var(--cyber-cyan);">${w.wallet_address}</span></td>
      <td style="font-size: 0.8rem;">${w.cluster_label || 'Unlabeled Cluster'}</td>
      <td class="font-mono" style="color: #fff;">${window.formatCurrency(w.total_received_usd)}</td>
      <td class="font-mono" style="color: var(--cyber-emerald);">${window.formatCurrency(w.current_balance_usd)}</td>
      <td>${window.formatRiskBadge(w.risk_level === 'Critical' ? 85 : 65)}</td>
      <td style="font-size: 0.75rem; color: var(--text-muted);">${w.source_service}</td>
    </tr>
  `).join('');
}

function renderMarketplaces(markets) {
  const tbody = document.getElementById('marketplaces-tbody');
  if (!tbody) return;
  if (markets.length === 0) {
    tbody.innerHTML = `<tr><td colspan="7" style="text-align:center; color: var(--text-muted); padding: 20px;">No marketplace vendor history.</td></tr>`;
    return;
  }
  tbody.innerHTML = markets.map(m => `
    <tr>
      <td><strong style="color: #fff;">${m.name || 'Underground Market'}</strong></td>
      <td style="font-size: 0.8rem; color: var(--text-secondary);">${m.market_type || 'Market'}</td>
      <td><span class="font-mono" style="color: var(--cyber-cyan); font-size: 0.8rem;">${m.handle_used || 'Same'}</span></td>
      <td><span style="font-size: 0.78rem; color: var(--cyber-purple);">${m.vendor_tier || 'Verified'}</span></td>
      <td class="font-mono" style="color: var(--cyber-emerald);">${m.positive_feedback_pct || 98}%</td>
      <td class="font-mono">${m.total_sales_count || 0}</td>
      <td class="font-mono" style="color: #fff;">${window.formatCurrency(m.escrow_volume_usd || 0)}</td>
    </tr>
  `).join('');
}

function renderInfrastructure(infra) {
  const tbody = document.getElementById('infra-tbody');
  if (!tbody) return;
  if (infra.length === 0) {
    tbody.innerHTML = `<tr><td colspan="6" style="text-align:center; color: var(--text-muted); padding: 20px;">No passive infrastructure indicators linked.</td></tr>`;
    return;
  }
  tbody.innerHTML = infra.map(i => `
    <tr>
      <td><span class="font-mono" style="font-size: 0.78rem; color: var(--cyber-purple);">${i.indicator_type}</span></td>
      <td><span class="font-mono" style="color: var(--cyber-cyan); font-size: 0.8rem;">${i.indicator_value}</span></td>
      <td style="font-size: 0.75rem; color: var(--text-secondary); max-width: 250px;">${i.service_banner || 'Passive TLS Telemetry'}</td>
      <td class="font-mono" style="font-size: 0.75rem; color: var(--text-muted);">${i.clearnet_association || 'None'}</td>
      <td style="font-size: 0.78rem;">${i.asn_organization || 'Darknet'} (${i.hosting_country || 'Global'})</td>
      <td class="font-mono">${i.confidence || 85}%</td>
    </tr>
  `).join('');
}

function renderRelationships(relations) {
  const tbody = document.getElementById('relationships-tbody');
  if (!tbody) return;
  if (relations.length === 0) {
    tbody.innerHTML = `<tr><td colspan="5" style="text-align:center; color: var(--text-muted); padding: 20px;">No direct relationships recorded.</td></tr>`;
    return;
  }
  tbody.innerHTML = relations.map(r => `
    <tr>
      <td><span class="font-mono" style="color: var(--cyber-cyan);">${r.source_id}</span></td>
      <td><span class="font-mono" style="color: #fff;">${r.target_id}</span></td>
      <td><span class="status-badge status-active">${r.relationship_type}</span></td>
      <td class="font-mono">${r.confidence_score}%</td>
      <td style="font-size: 0.78rem; color: var(--text-secondary);">${r.evidence_text}</td>
    </tr>
  `).join('');
}

function renderTimeline(events) {
  const container = document.getElementById('timeline-container');
  if (!container) return;
  if (events.length === 0) {
    container.innerHTML = `<div style="text-align:center; color: var(--text-muted); padding: 20px;">No chronological timeline events.</div>`;
    return;
  }
  container.innerHTML = events.map(e => `
    <div style="display: flex; gap: 16px; align-items: flex-start; background: rgba(0,0,0,0.3); border: 1px solid var(--border-card); border-radius: 6px; padding: 14px 18px;">
      <div style="min-width: 100px; font-family: var(--font-mono); font-size: 0.8rem; color: var(--cyber-cyan);">${e.event_date ? e.event_date.split('T')[0] : ''}</div>
      <div style="flex: 1;">
        <div style="font-size: 0.9rem; font-weight: 600; color: #fff; margin-bottom: 4px;">${e.event_title}</div>
        <div style="font-size: 0.82rem; color: var(--text-secondary); line-height: 1.4;">${e.event_description}</div>
      </div>
      <div>
        <span class="status-badge ${e.severity === 'Critical' ? 'status-seized' : 'status-active'}">${e.severity}</span>
      </div>
    </div>
  `).join('');
}

function renderPersonaAndEvidence(actorId, handles, pgp, wallets, infra) {
  // Persona Tab Content
  const personaContainer = document.getElementById('persona-profile-content');
  if (personaContainer) {
    personaContainer.innerHTML = `
      <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 20px;">
        <div style="background: rgba(0,0,0,0.3); padding: 16px; border-radius: 8px; border: 1px solid var(--border-card);">
          <h4 style="font-size: 0.88rem; color: var(--cyber-cyan); margin-bottom: 12px;"><i class="fa-solid fa-brain"></i> Stylometric Profile</h4>
          <div style="display: flex; flex-direction: column; gap: 8px; font-size: 0.82rem;">
            <div><span style="color: var(--text-muted);">Primary Language:</span> Russian / English</div>
            <div><span style="color: var(--text-muted);">Avg Sentence Length:</span> 13.8 words</div>
            <div><span style="color: var(--text-muted);">Type-Token Ratio (TTR):</span> 0.712 (Rich)</div>
            <div><span style="color: var(--text-muted);">Punctuation Entropy:</span> 0.485</div>
            <div><span style="color: var(--text-muted);">Peak Activity UTC:</span> 09:00 - 19:00 UTC</div>
          </div>
        </div>
        <div style="background: rgba(0,0,0,0.3); padding: 16px; border-radius: 8px; border: 1px solid var(--border-card);">
          <h4 style="font-size: 0.88rem; color: var(--cyber-purple); margin-bottom: 12px;"><i class="fa-solid fa-quote-left"></i> Typical Signature Phrases</h4>
          <ul style="padding-left: 18px; font-size: 0.82rem; color: var(--text-secondary); line-height: 1.6;">
            <li>"work through escrow only"</li>
            <li>"guaranteed clean domain admin"</li>
            <li>"ping jabber otr for private session"</li>
            <li>"check signature with pgp"</li>
          </ul>
          <div style="margin-top: 14px;">
            <a href="/persona?actor=${actorId}" class="btn-cyber btn-sm"><i class="fa-solid fa-fingerprint"></i> Compare with Another Actor</a>
          </div>
        </div>
      </div>
    `;
  }

  // Evidence Tab Content
  const evidenceContainer = document.getElementById('evidence-container');
  if (evidenceContainer) {
    evidenceContainer.innerHTML = `
      <div style="background: rgba(0,0,0,0.3); border: 1px solid var(--border-card); border-radius: 8px; padding: 20px;">
        <h3 style="font-size: 1rem; color: #fff; margin-bottom: 12px;"><i class="fa-solid fa-shield-halved" style="color: var(--cyber-cyan);"></i> Defensive Attribution Confidence Package</h3>
        <p style="font-size: 0.85rem; color: var(--text-secondary); line-height: 1.5; margin-bottom: 16px;">
          Attribution assessment is based on ${handles.length} observed handle correlations, ${pgp.length} cryptographic key fingerprints, 
          ${wallets.length} cryptocurrency wallet clusters, and ${infra.length} passive infrastructure indicators.
        </p>
        <div style="background: rgba(0, 240, 255, 0.05); border: 1px solid var(--border-subtle); padding: 14px; border-radius: 6px; font-size: 0.8rem; color: #bae6fd;">
          <strong>DEFENSIVE DISCLAIMER:</strong> All conclusions are mathematical and probabilistic attribution indicators derived from passive observation telemetry. This system does NOT assert confirmed real-world legal identities.
        </div>
      </div>
    `;
  }
}

async function renderSourcesTab() {
  const container = document.getElementById('sources-container');
  if (!container) return;
  try {
    const res = await fetch('/api/sources');
    const sources = (await res.json()).data || [];
    container.innerHTML = `
      <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 16px;">
        ${sources.map(s => `
          <div style="background: rgba(0,0,0,0.3); border: 1px solid var(--border-card); border-radius: 6px; padding: 16px;">
            <div style="font-weight: 700; color: #fff; font-size: 0.88rem; margin-bottom: 4px;">${s.source_name}</div>
            <div style="font-size: 0.72rem; color: var(--cyber-cyan); margin-bottom: 8px;">${s.source_type} • ${s.reliability_score}% Reliability</div>
            <div style="font-size: 0.78rem; color: var(--text-secondary);">${s.description}</div>
          </div>
        `).join('')}
      </div>
    `;
  } catch (e) {
    container.innerHTML = `<div style="color: var(--text-muted);">Failed to load sources.</div>`;
  }
}
