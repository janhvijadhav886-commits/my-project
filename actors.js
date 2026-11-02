/**
 * Threat Actors Directory Search, Filtering, and Actions
 */

document.addEventListener('DOMContentLoaded', () => {
  // Check URL query parameters for initial search query
  const urlParams = new URLSearchParams(window.location.search);
  const initialSearch = urlParams.get('search');
  if (initialSearch) {
    const searchInput = document.getElementById('actor-filter-search');
    if (searchInput) searchInput.value = initialSearch;
  }

  fetchActors();

  // Attach filter listeners
  const searchInput = document.getElementById('actor-filter-search');
  const riskSelect = document.getElementById('actor-filter-risk');
  const categorySelect = document.getElementById('actor-filter-category');
  const statusSelect = document.getElementById('actor-filter-status');
  const resetBtn = document.getElementById('reset-actor-filters');

  if (searchInput) {
    searchInput.addEventListener('input', debounce(fetchActors, 300));
  }
  if (riskSelect) riskSelect.addEventListener('change', fetchActors);
  if (categorySelect) categorySelect.addEventListener('change', fetchActors);
  if (statusSelect) statusSelect.addEventListener('change', fetchActors);

  if (resetBtn) {
    resetBtn.addEventListener('click', () => {
      if (searchInput) searchInput.value = '';
      if (riskSelect) riskSelect.value = 'all';
      if (categorySelect) categorySelect.value = 'all';
      if (statusSelect) statusSelect.value = 'all';
      fetchActors();
    });
  }
});

function debounce(func, wait) {
  let timeout;
  return function(...args) {
    clearTimeout(timeout);
    timeout = setTimeout(() => func.apply(this, args), wait);
  };
}

async function fetchActors() {
  const search = document.getElementById('actor-filter-search')?.value.trim() || '';
  const risk = document.getElementById('actor-filter-risk')?.value || 'all';
  const category = document.getElementById('actor-filter-category')?.value || 'all';
  const status = document.getElementById('actor-filter-status')?.value || 'all';

  const tbody = document.getElementById('actors-table-body');
  const countLabel = document.getElementById('actor-count-label');

  try {
    const queryParams = new URLSearchParams();
    if (search) queryParams.append('search', search);
    if (risk !== 'all') queryParams.append('risk', risk);
    if (category !== 'all') queryParams.append('category', category);
    if (status !== 'all') queryParams.append('status', status);

    const res = await fetch(`/api/actors?${queryParams.toString()}`);
    const result = await res.json();

    if (result.status !== 'success' || !Array.isArray(result.data)) {
      throw new Error('Invalid actor list payload');
    }

    const actors = result.data;
    if (countLabel) countLabel.innerText = actors.length;

    if (actors.length === 0) {
      tbody.innerHTML = `
        <tr>
          <td colspan="9" style="text-align: center; color: var(--text-muted); padding: 36px;">
            <i class="fa-solid fa-filter-circle-xmark" style="font-size: 2rem; margin-bottom: 10px; display: block; color: var(--text-muted);"></i>
            No threat actors matched your filter parameters.
          </td>
        </tr>
      `;
      return;
    }

    tbody.innerHTML = actors.map(a => {
      const statusClass = a.status === 'Active' ? 'status-active' : (a.status === 'Monitored' ? 'status-monitored' : 'status-dormant');
      const firstSeen = a.first_seen ? a.first_seen.split('T')[0] : 'N/A';
      const lastSeen = a.last_seen ? a.last_seen.split('T')[0] : 'N/A';

      return `
        <tr>
          <td>
            <a href="/actors/${a.id}" style="color: var(--cyber-cyan); text-decoration: none; font-weight: 700; font-family: var(--font-mono);">
              ${a.actor_code}
            </a>
          </td>
          <td>
            <div class="actor-cell-flex">
              <div class="actor-table-avatar">
                <img src="/static/images/darkweb_actor_avatar.jpg" alt="${a.primary_handle}">
                <span class="actor-reticle-dot"></span>
              </div>
              <div>
                <a href="/actors/${a.id}" class="actor-handle-link">${a.primary_handle}</a>
                <div style="font-size: 0.72rem; color: var(--text-muted); font-family: var(--font-mono);">${a.operational_language || 'UNKNOWN_LANG'} • ${a.primary_timezone || 'UTC'}</div>
              </div>
            </div>
          </td>
          <td>
            <span style="font-size: 0.8rem; color: var(--text-secondary);">${a.category}</span>
          </td>
          <td>
            ${window.formatRiskBadge(a.risk_score)}
          </td>
          <td>
            <div style="display: flex; align-items: center; gap: 6px;">
              <div style="flex: 1; max-width: 60px; height: 6px; background: rgba(255,255,255,0.1); border-radius: 3px; overflow: hidden;">
                <div style="width: ${a.attribution_confidence}%; height: 100%; background: ${a.attribution_confidence >= 80 ? 'var(--cyber-emerald)' : 'var(--cyber-cyan)'};"></div>
              </div>
              <span style="font-size: 0.75rem; font-family: var(--font-mono);">${a.attribution_confidence}%</span>
            </div>
          </td>
          <td>
            <span class="status-badge ${statusClass}">${a.status}</span>
          </td>
          <td style="font-family: var(--font-mono); font-size: 0.75rem; color: var(--text-muted);">${firstSeen}</td>
          <td style="font-family: var(--font-mono); font-size: 0.75rem; color: var(--text-secondary);">${lastSeen}</td>
          <td style="text-align: right;">
            <div style="display: inline-flex; gap: 6px;">
              <a href="/actors/${a.id}" class="btn-cyber btn-sm" title="Open Deep Intelligence Dossier">
                <i class="fa-solid fa-folder-open"></i> Dossier
              </a>
              <a href="/persona?actor=${a.id}" class="btn-cyber-outline btn-sm" title="Run Persona Stylometry Match">
                <i class="fa-solid fa-fingerprint"></i>
              </a>
              <a href="/api/export/actor/${a.id}/json" class="btn-cyber-outline btn-sm" title="Export JSON Intelligence Package">
                <i class="fa-solid fa-download"></i>
              </a>
            </div>
          </td>
        </tr>
      `;
    }).join('');

  } catch (err) {
    console.error('Error fetching actors:', err);
    tbody.innerHTML = `<tr><td colspan="9" style="text-align: center; color: var(--cyber-crimson); padding: 20px;">Failed to retrieve threat actor records.</td></tr>`;
  }
}
