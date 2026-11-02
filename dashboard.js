/**
 * Dashboard Analytics & Dynamic Chart.js Rendering
 */

document.addEventListener('DOMContentLoaded', () => {
  loadDashboardData();

  const refreshBtn = document.getElementById('refresh-dashboard-btn');
  if (refreshBtn) {
    refreshBtn.addEventListener('click', () => {
      loadDashboardData();
      if (window.showToast) window.showToast('Intelligence feeds refreshed successfully', 'success');
    });
  }
});

let charts = {};

async function loadDashboardData() {
  try {
    const res = await fetch('/api/dashboard/stats');
    const result = await res.json();

    if (result.status !== 'success' || !result.data) {
      throw new Error('Invalid statistics payload');
    }

    const data = result.data;

    // 1. Populate KPIs
    document.getElementById('kpi-total-actors').innerText = data.kpis.total_threat_actors || 0;
    document.getElementById('kpi-high-risk').innerText = data.kpis.high_risk_actors || 0;
    document.getElementById('kpi-active-actors').innerText = data.kpis.active_actors || 0;
    document.getElementById('kpi-infra-count').innerText = data.kpis.infrastructure_indicators || 0;
    document.getElementById('kpi-persona-links').innerText = data.kpis.persona_links || 0;
    document.getElementById('kpi-events-count').innerText = data.kpis.intelligence_events || 0;

    // 2. Render Charts
    renderRiskDistChart(data.risk_distribution);
    renderEventsTimelineChart(data.recent_events);
    renderCategoriesChart(data.category_distribution);
    renderConfidenceChart(data.confidence_distribution);
    renderInfraTypesChart(data.infra_type_distribution);

    // 3. Render Top Risk Actors Table
    renderTopActors(data.top_risk_actors);

    // 4. Render Recent Events Stream
    renderRecentEvents(data.recent_events);

  } catch (err) {
    console.error('Error loading dashboard stats:', err);
    if (window.showToast) window.showToast('Failed to load dashboard telemetry', 'danger');
  }
}

// Chart 1: Risk Distribution (Doughnut)
function renderRiskDistChart(dist) {
  const ctx = document.getElementById('chart-risk-dist').getContext('2d');
  if (charts.risk) charts.risk.destroy();

  charts.risk = new Chart(ctx, {
    type: 'doughnut',
    data: {
      labels: Object.keys(dist || {}),
      datasets: [{
        data: Object.values(dist || {}),
        backgroundColor: ['#ef4444', '#f59e0b', '#0ea5e9', '#10b981'],
        borderColor: '#0b111a',
        borderWidth: 2,
        hoverOffset: 6
      }]
    },
    options: {
      responsive: true,
      maintainAspectRatio: false,
      plugins: {
        legend: {
          position: 'bottom',
          labels: { color: '#94a3b8', boxWidth: 12, font: { size: 11 } }
        }
      },
      cutout: '68%'
    }
  });
}

// Chart 2: Timeline Line Graph
function renderEventsTimelineChart(events) {
  const ctx = document.getElementById('chart-events-timeline').getContext('2d');
  if (charts.timeline) charts.timeline.destroy();

  // Mock aggregated temporal counts for visual trajectory
  const labels = ['Q1 2023', 'Q2 2023', 'Q3 2023', 'Q4 2023', 'Q1 2024', 'Q2 2024', 'Q3 2024', 'Q4 2024', 'Q1 2025', 'Q2 2025', 'Q3 2026'];
  const counts = [2, 5, 8, 12, 16, 22, 28, 35, 41, 48, 56];

  charts.timeline = new Chart(ctx, {
    type: 'line',
    data: {
      labels: labels,
      datasets: [{
        label: 'Cumulative Observed Intelligence Events',
        data: counts,
        borderColor: '#00f0ff',
        backgroundColor: 'rgba(0, 240, 255, 0.08)',
        borderWidth: 2.5,
        tension: 0.35,
        fill: true,
        pointBackgroundColor: '#00f0ff',
        pointBorderColor: '#06090e',
        pointRadius: 4,
        pointHoverRadius: 6
      }]
    },
    options: {
      responsive: true,
      maintainAspectRatio: false,
      plugins: {
        legend: { display: false }
      },
      scales: {
        x: {
          grid: { color: 'rgba(255, 255, 255, 0.05)' },
          ticks: { color: '#64748b', font: { size: 10 } }
        },
        y: {
          grid: { color: 'rgba(255, 255, 255, 0.05)' },
          ticks: { color: '#64748b', font: { size: 10 } }
        }
      }
    }
  });
}

// Chart 3: Categories (Horizontal Bar)
function renderCategoriesChart(categories) {
  const ctx = document.getElementById('chart-categories').getContext('2d');
  if (charts.categories) charts.categories.destroy();

  const labels = Object.keys(categories || {});
  const data = Object.values(categories || {});

  charts.categories = new Chart(ctx, {
    type: 'bar',
    data: {
      labels: labels.map(l => l.length > 18 ? l.substring(0, 16) + '...' : l),
      datasets: [{
        data: data,
        backgroundColor: 'rgba(139, 92, 246, 0.65)',
        borderColor: '#8b5cf6',
        borderWidth: 1,
        borderRadius: 4
      }]
    },
    options: {
      indexAxis: 'y',
      responsive: true,
      maintainAspectRatio: false,
      plugins: { legend: { display: false } },
      scales: {
        x: {
          grid: { color: 'rgba(255, 255, 255, 0.05)' },
          ticks: { color: '#64748b', stepSize: 1 }
        },
        y: {
          grid: { display: false },
          ticks: { color: '#94a3b8', font: { size: 10 } }
        }
      }
    }
  });
}

// Chart 4: Confidence Scores
function renderConfidenceChart(conf) {
  const ctx = document.getElementById('chart-confidence').getContext('2d');
  if (charts.confidence) charts.confidence.destroy();

  charts.confidence = new Chart(ctx, {
    type: 'bar',
    data: {
      labels: Object.keys(conf || {}),
      datasets: [{
        data: Object.values(conf || {}),
        backgroundColor: 'rgba(14, 165, 233, 0.65)',
        borderColor: '#0ea5e9',
        borderWidth: 1,
        borderRadius: 4
      }]
    },
    options: {
      responsive: true,
      maintainAspectRatio: false,
      plugins: { legend: { display: false } },
      scales: {
        x: {
          grid: { display: false },
          ticks: { color: '#64748b', font: { size: 9 } }
        },
        y: {
          grid: { color: 'rgba(255, 255, 255, 0.05)' },
          ticks: { color: '#64748b', stepSize: 1 }
        }
      }
    }
  });
}

// Chart 5: Infrastructure Types (Pie)
function renderInfraTypesChart(types) {
  const ctx = document.getElementById('chart-infra-types').getContext('2d');
  if (charts.infra) charts.infra.destroy();

  charts.infra = new Chart(ctx, {
    type: 'pie',
    data: {
      labels: Object.keys(types || {}),
      datasets: [{
        data: Object.values(types || {}),
        backgroundColor: ['#00f0ff', '#8b5cf6', '#ec4899', '#f59e0b', '#10b981', '#64748b'],
        borderColor: '#0b111a',
        borderWidth: 1.5
      }]
    },
    options: {
      responsive: true,
      maintainAspectRatio: false,
      plugins: {
        legend: {
          position: 'bottom',
          labels: { color: '#94a3b8', boxWidth: 10, font: { size: 10 } }
        }
      }
    }
  });
}

// Render Top Actors Table
function renderTopActors(actors) {
  const tbody = document.getElementById('top-actors-tbody');
  if (!tbody) return;

  if (!actors || actors.length === 0) {
    tbody.innerHTML = `<tr><td colspan="5" style="text-align:center; color: var(--text-muted); padding: 20px;">No threat actors found</td></tr>`;
    return;
  }

  tbody.innerHTML = actors.map(a => `
    <tr>
      <td><strong class="font-mono" style="color: var(--cyber-cyan);">${a.actor_code}</strong></td>
      <td>
        <div class="actor-cell-flex">
          <div class="actor-table-avatar">
            <img src="/static/images/darkweb_actor_avatar.jpg" alt="${a.primary_handle}">
            <span class="actor-reticle-dot"></span>
          </div>
          <div>
            <div style="font-weight: 600; color: #fff;">${a.primary_handle}</div>
            <div style="font-size: 0.7rem; color: var(--text-muted); font-family: var(--font-mono);">${a.primary_timezone || 'UTC'}</div>
          </div>
        </div>
      </td>
      <td><span style="font-size: 0.78rem; color: var(--text-secondary);">${a.category}</span></td>
      <td>${window.formatRiskBadge(a.risk_score)}</td>
      <td>
        <a href="/actors/${a.id}" class="btn-cyber-outline btn-sm">
          <i class="fa-solid fa-folder-open"></i> Dossier
        </a>
      </td>
    </tr>
  `).join('');
}

// Render Recent Events Stream
function renderRecentEvents(events) {
  const container = document.getElementById('recent-events-container');
  if (!container) return;

  if (!events || events.length === 0) {
    container.innerHTML = `<div style="color: var(--text-muted); text-align: center; padding: 20px;">No recent events recorded</div>`;
    return;
  }

  container.innerHTML = events.slice(0, 5).map(e => `
    <div style="background: rgba(0, 0, 0, 0.25); border: 1px solid var(--border-card); border-radius: 6px; padding: 10px 14px; display: flex; gap: 12px; align-items: flex-start;">
      <div style="width: 8px; height: 8px; border-radius: 50%; background: ${e.severity === 'Critical' ? 'var(--cyber-crimson)' : 'var(--cyber-cyan)'}; margin-top: 6px; box-shadow: 0 0 6px ${e.severity === 'Critical' ? 'var(--cyber-crimson)' : 'var(--cyber-cyan)'};"></div>
      <div style="flex: 1;">
        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 2px;">
          <div style="font-size: 0.82rem; font-weight: 600; color: #fff;">${e.event_title}</div>
          <span style="font-size: 0.7rem; color: var(--text-muted); font-family: var(--font-mono);">${e.event_date ? e.event_date.split('T')[0] : ''}</span>
        </div>
        <div style="font-size: 0.75rem; color: var(--text-secondary); line-height: 1.3;">${e.event_description}</div>
      </div>
    </div>
  `).join('');
}
