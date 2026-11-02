/**
 * 4-Factor Risk Engine Simulator Controller
 */

document.addEventListener('DOMContentLoaded', () => {
  initRiskPage();

  const sliders = [
    'slider-infra-risk',
    'slider-behaviour-risk',
    'slider-network-risk',
    'slider-activity-risk'
  ];

  sliders.forEach(id => {
    const el = document.getElementById(id);
    if (el) {
      el.addEventListener('input', () => {
        // Update display text
        const key = id.replace('slider-', '');
        document.getElementById(`val-${key}`).innerText = parseFloat(el.value).toFixed(1);
        recalculateRisk();
      });
    }
  });
});

async function initRiskPage() {
  try {
    const res = await fetch('/api/actors');
    const actors = (await res.json()).data || [];
    const select = document.getElementById('risk-actor-select');

    if (select) {
      actors.forEach(a => {
        const opt = document.createElement('option');
        opt.value = a.id;
        opt.innerText = `${a.primary_handle} (${a.actor_code}) - Risk ${a.risk_score}`;
        select.appendChild(opt);
      });

      select.addEventListener('change', async () => {
        const actorId = select.value;
        if (!actorId) return;
        try {
          const rRes = await fetch(`/api/risk/${actorId}`);
          const rData = (await rRes.json()).data;
          if (rData && rData.breakdown) {
            setSliderValue('infra-risk', rData.breakdown.infrastructure_risk);
            setSliderValue('behaviour-risk', rData.breakdown.behavioural_risk);
            setSliderValue('network-risk', rData.breakdown.network_risk);
            setSliderValue('activity-risk', rData.breakdown.activity_risk);
            recalculateRisk();
          }
        } catch (e) {
          console.error(e);
        }
      });
    }

    recalculateRisk();

  } catch (err) {
    console.error('Error initializing risk page:', err);
  }
}

function setSliderValue(key, val) {
  const slider = document.getElementById(`slider-${key}`);
  const label = document.getElementById(`val-${key}`);
  if (slider && label) {
    slider.value = val;
    label.innerText = parseFloat(val).toFixed(1);
  }
}

async function recalculateRisk() {
  const infra = parseFloat(document.getElementById('slider-infra-risk')?.value || 50);
  const behaviour = parseFloat(document.getElementById('slider-behaviour-risk')?.value || 50);
  const network = parseFloat(document.getElementById('slider-network-risk')?.value || 50);
  const activity = parseFloat(document.getElementById('slider-activity-risk')?.value || 50);

  try {
    const res = await fetch('/api/risk/calculate', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        infrastructure_risk: infra,
        behavioural_risk: behaviour,
        network_risk: network,
        activity_risk: activity
      })
    });

    const result = await res.json();
    const data = result.data;
    if (!data) return;

    // Update Result Display
    const scoreElem = document.getElementById('result-risk-score');
    if (scoreElem) {
      scoreElem.innerText = data.total_risk_score.toFixed(2);
      if (data.total_risk_score >= 80) scoreElem.style.color = 'var(--cyber-crimson)';
      else if (data.total_risk_score >= 60) scoreElem.style.color = 'var(--cyber-amber)';
      else if (data.total_risk_score >= 30) scoreElem.style.color = 'var(--cyber-blue)';
      else scoreElem.style.color = 'var(--cyber-emerald)';
    }

    const badgeElem = document.getElementById('result-risk-tier-badge');
    if (badgeElem) {
      badgeElem.innerHTML = window.formatRiskBadge(data.total_risk_score);
    }

    const rationaleElem = document.getElementById('result-risk-rationale');
    if (rationaleElem) {
      rationaleElem.innerText = data.rationale;
    }

    // Recommended Mitigations
    const mitigationsContainer = document.getElementById('recommended-mitigations-list');
    if (mitigationsContainer) {
      const mitigations = data.recommended_mitigations || [];
      mitigationsContainer.innerHTML = mitigations.map(m => `
        <div style="background: rgba(0,0,0,0.3); border: 1px solid var(--border-card); border-left: 3px solid var(--cyber-cyan); padding: 10px 14px; border-radius: 0 6px 6px 0; color: var(--text-primary);">
          <i class="fa-solid fa-shield-halved" style="color: var(--cyber-cyan); margin-right: 6px;"></i> ${m}
        </div>
      `).join('');
    }

  } catch (err) {
    console.error('Risk recalculation error:', err);
  }
}
