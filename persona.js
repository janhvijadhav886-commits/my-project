/**
 * Persona Analysis Engine Controller with Dynamic Radar Chart
 */

let radarChart = null;
let actorList = [];

document.addEventListener('DOMContentLoaded', () => {
  initPersonaPage();

  const runBtn = document.getElementById('btn-run-persona-analysis');
  if (runBtn) {
    runBtn.addEventListener('click', executePersonaAnalysis);
  }
});

async function initPersonaPage() {
  try {
    const res = await fetch('/api/actors');
    const result = await res.json();
    actorList = result.data || [];

    const selectA = document.getElementById('persona-actor-a');
    const selectB = document.getElementById('persona-actor-b');

    if (!selectA || !selectB) return;

    actorList.forEach(a => {
      const optA = document.createElement('option');
      optA.value = a.id;
      optA.innerText = `${a.primary_handle} (${a.actor_code})`;
      selectA.appendChild(optA);

      const optB = document.createElement('option');
      optB.value = a.id;
      optB.innerText = `${a.primary_handle} (${a.actor_code})`;
      selectB.appendChild(optB);
    });

    // Check URL parameters for preset selection
    const urlParams = new URLSearchParams(window.location.search);
    const presetActor = urlParams.get('actor');
    if (presetActor) {
      selectA.value = presetActor;
      loadActorCorpus(presetActor, 'A');
      // Pick second actor automatically for demo
      if (actorList.length > 1) {
        const other = actorList.find(x => x.id !== presetActor);
        if (other) {
          selectB.value = other.id;
          loadActorCorpus(other.id, 'B');
        }
      }
    } else {
      // Default initial selection for instant hackathon demonstration
      if (actorList.length >= 2) {
        selectA.value = actorList[0].id;
        loadActorCorpus(actorList[0].id, 'A');

        selectB.value = actorList[1].id;
        loadActorCorpus(actorList[1].id, 'B');
      }
    }

    // Attach change listeners to update textareas
    selectA.addEventListener('change', () => loadActorCorpus(selectA.value, 'A'));
    selectB.addEventListener('change', () => loadActorCorpus(selectB.value, 'B'));

    // Automatically trigger initial comparison
    setTimeout(executePersonaAnalysis, 400);

  } catch (err) {
    console.error('Error initializing persona comparison:', err);
  }
}

function loadActorCorpus(actorId, target) {
  const actor = actorList.find(a => a.id === actorId);
  const textarea = document.getElementById(`persona-text-${target.toLowerCase()}`);
  if (!actor || !textarea) return;

  textarea.value = actor.threat_description || '';
}

async function executePersonaAnalysis() {
  const actorAId = document.getElementById('persona-actor-a')?.value;
  const actorBId = document.getElementById('persona-actor-b')?.value;
  const textA = document.getElementById('persona-text-a')?.value.trim();
  const textB = document.getElementById('persona-text-b')?.value.trim();

  if (!textA && !actorAId) {
    if (window.showToast) window.showToast('Please provide text or select Subject A', 'warning');
    return;
  }
  if (!textB && !actorBId) {
    if (window.showToast) window.showToast('Please provide text or select Subject B', 'warning');
    return;
  }

  try {
    const payload = {
      actor_a_id: actorAId || null,
      actor_b_id: actorBId || null,
      custom_text_a: textA || null,
      custom_text_b: textB || null
    };

    const res = await fetch('/api/persona/analyze', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(payload)
    });

    const result = await res.json();
    if (result.status !== 'success' || !result.data) {
      throw new Error('Analysis response error');
    }

    const data = result.data;
    renderPersonaResults(data);

  } catch (err) {
    console.error('Persona analysis failed:', err);
    if (window.showToast) window.showToast('Failed to execute persona engine analysis', 'danger');
  }
}

function renderPersonaResults(data) {
  const container = document.getElementById('persona-results-container');
  if (!container) return;

  container.style.display = 'block';

  // Overall Score
  document.getElementById('result-overall-sim').innerText = `${data.overall_similarity}%`;
  document.getElementById('result-confidence-badge').innerText = `Confidence: ${data.confidence} (${data.overall_similarity >= 80 ? 'High Stylistic Linkage' : 'Moderate Overlap'})`;
  document.getElementById('result-evidence-text').innerText = data.evidence;

  // Breakdown Bars
  updateBar('writing-style', data.writing_style_similarity);
  updateBar('vocabulary', data.vocabulary_similarity);
  updateBar('behavior', data.behaviour_similarity);
  updateBar('activity', data.activity_pattern_similarity);

  // Shared Markers Chips
  const markersContainer = document.getElementById('shared-markers-container');
  if (markersContainer) {
    const vocab = data.shared_indicators?.shared_vocabulary || [];
    const phrases = data.shared_indicators?.shared_phrases || [];
    const all = [...vocab, ...phrases];

    if (all.length === 0) {
      markersContainer.innerHTML = `<span style="font-size: 0.75rem; color: var(--text-muted);">No direct semantic tokens overlapped.</span>`;
    } else {
      markersContainer.innerHTML = all.map(m => `
        <span style="background: rgba(0, 240, 255, 0.1); border: 1px solid rgba(0, 240, 255, 0.3); color: #bae6fd; font-size: 0.72rem; padding: 2px 8px; border-radius: 4px; font-family: var(--font-mono);">
          ${m}
        </span>
      `).join('');
    }
  }

  // Render Radar Chart
  renderRadarChart(data);

  // Smooth scroll down to results
  container.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
}

function updateBar(key, value) {
  const label = document.getElementById(`score-${key}`);
  const bar = document.getElementById(`bar-${key}`);
  if (label) label.innerText = `${value}%`;
  if (bar) bar.style.width = `${value}%`;
}

function renderRadarChart(data) {
  const ctx = document.getElementById('chart-persona-radar').getContext('2d');
  if (radarChart) radarChart.destroy();

  radarChart = new Chart(ctx, {
    type: 'radar',
    data: {
      labels: [
        'Writing Style',
        'Vocabulary (TF-IDF)',
        'Behavioral Alignment',
        'Activity / Timezone',
        'Posting Cadence'
      ],
      datasets: [
        {
          label: 'Probabilistic Stylometric Correlation',
          data: [
            data.writing_style_similarity,
            data.vocabulary_similarity,
            data.behaviour_similarity,
            data.activity_pattern_similarity,
            data.posting_frequency_similarity
          ],
          backgroundColor: 'rgba(0, 240, 255, 0.2)',
          borderColor: '#00f0ff',
          borderWidth: 2,
          pointBackgroundColor: '#00f0ff',
          pointBorderColor: '#0b111a',
          pointRadius: 4
        }
      ]
    },
    options: {
      responsive: true,
      maintainAspectRatio: false,
      scales: {
        r: {
          min: 0,
          max: 100,
          ticks: { stepSize: 20, color: '#64748b', backdropColor: 'transparent' },
          grid: { color: 'rgba(255, 255, 255, 0.08)' },
          angleLines: { color: 'rgba(255, 255, 255, 0.08)' },
          pointLabels: { color: '#94a3b8', font: { size: 10.5, family: 'Inter' } }
        }
      },
      plugins: {
        legend: {
          position: 'bottom',
          labels: { color: '#f1f5f9', font: { size: 11 } }
        }
      }
    }
  });
}
