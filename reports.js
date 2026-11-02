/**
 * Report Generator and Dynamic Dossier Preview Controller
 */

let actorsList = [];

document.addEventListener('DOMContentLoaded', async () => {
  try {
    const res = await fetch('/api/actors');
    actorsList = (await res.json()).data || [];

    const select = document.getElementById('report-actor-select');
    if (select) {
      actorsList.forEach(a => {
        const opt = document.createElement('option');
        opt.value = a.id;
        opt.innerText = `${a.primary_handle} (${a.actor_code}) - Risk ${a.risk_score}`;
        select.appendChild(opt);
      });

      select.addEventListener('change', () => {
        updateReportPreview(select.value);
      });

      if (actorsList.length > 0) {
        select.value = actorsList[0].id;
        updateReportPreview(actorsList[0].id);
      }
    }
  } catch (err) {
    console.error('Error loading actors for report:', err);
  }
});

function updateReportPreview(actorId) {
  const actor = actorsList.find(a => a.id === actorId);
  const preview = document.getElementById('report-preview-container');
  const btnHtml = document.getElementById('btn-export-html');
  const btnJson = document.getElementById('btn-export-json');
  const btnCsv = document.getElementById('btn-export-csv');

  if (!actor || !preview) return;

  // Update export links
  if (btnHtml) btnHtml.href = `/api/report/actor/${actor.id}`;
  if (btnJson) btnJson.href = `/api/export/actor/${actor.id}/json`;
  if (btnCsv) btnCsv.href = `/api/export/actor/${actor.id}/csv`;

  preview.innerHTML = `
    <div style="background: rgba(0,0,0,0.3); border: 1px solid var(--border-card); border-radius: 8px; padding: 20px; margin-bottom: 16px;">
      <div style="display: flex; justify-content: space-between; align-items: flex-start; margin-bottom: 12px; border-bottom: 1px solid var(--border-subtle); padding-bottom: 12px;">
        <div>
          <div style="font-size: 1.2rem; font-weight: 700; color: #fff;">${actor.primary_handle}</div>
          <div class="font-mono" style="font-size: 0.8rem; color: var(--cyber-cyan);">${actor.actor_code} • ${actor.category}</div>
        </div>
        <div style="text-align: right;">
          ${window.formatRiskBadge(actor.risk_score)}
          <div style="font-size: 0.72rem; color: var(--text-muted); margin-top: 4px;">Attribution Confidence: ${actor.attribution_confidence}%</div>
        </div>
      </div>

      <div style="margin-bottom: 14px;">
        <strong style="color: #fff; font-size: 0.85rem;">Threat Narrative:</strong>
        <p style="font-size: 0.82rem; color: var(--text-secondary); margin-top: 4px;">${actor.threat_description}</p>
      </div>

      <div style="margin-bottom: 14px;">
        <strong style="color: #fff; font-size: 0.85rem;">Analyst Assessment Notes:</strong>
        <p style="font-size: 0.82rem; color: var(--cyber-amber); margin-top: 4px;">${actor.analyst_notes}</p>
      </div>

      <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 12px; font-size: 0.78rem; border-top: 1px solid var(--border-card); padding-top: 12px;">
        <div><span style="color: var(--text-muted);">Language:</span> ${actor.operational_language}</div>
        <div><span style="color: var(--text-muted);">Active Timezone:</span> ${actor.primary_timezone}</div>
        <div><span style="color: var(--text-muted);">First Seen:</span> ${actor.first_seen ? actor.first_seen.split('T')[0] : 'N/A'}</div>
        <div><span style="color: var(--text-muted);">Last Seen:</span> ${actor.last_seen ? actor.last_seen.split('T')[0] : 'N/A'}</div>
      </div>
    </div>

    <div style="background: rgba(0, 240, 255, 0.04); border: 1px solid var(--border-subtle); padding: 12px; border-radius: 6px; font-size: 0.75rem; color: #bae6fd;">
      <i class="fa-solid fa-circle-info" style="color: var(--cyber-cyan); margin-right: 4px;"></i>
      Click <strong>"Generate Printable Dossier (PDF)"</strong> to open the full unredacted brief ready for immediate hardcopy or PDF export (Ctrl+P).
    </div>
  `;
}
