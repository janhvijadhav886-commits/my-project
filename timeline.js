/**
 * Timeline Feed Controller & Event Filtering
 */

document.addEventListener('DOMContentLoaded', () => {
  initTimeline();

  const actorFilter = document.getElementById('timeline-actor-filter');
  const typeFilter = document.getElementById('timeline-type-filter');
  const sevFilter = document.getElementById('timeline-severity-filter');
  const refreshBtn = document.getElementById('btn-timeline-refresh');

  if (actorFilter) actorFilter.addEventListener('change', fetchTimelineEvents);
  if (typeFilter) typeFilter.addEventListener('change', fetchTimelineEvents);
  if (sevFilter) sevFilter.addEventListener('change', fetchTimelineEvents);
  if (refreshBtn) refreshBtn.addEventListener('click', fetchTimelineEvents);
});

async function initTimeline() {
  try {
    const res = await fetch('/api/actors');
    const actors = (await res.json()).data || [];
    const select = document.getElementById('timeline-actor-filter');

    if (select) {
      actors.forEach(a => {
        const opt = document.createElement('option');
        opt.value = a.id;
        opt.innerText = `${a.primary_handle} (${a.actor_code})`;
        select.appendChild(opt);
      });
    }

    fetchTimelineEvents();
  } catch (err) {
    console.error('Error initializing timeline:', err);
  }
}

async function fetchTimelineEvents() {
  const actorId = document.getElementById('timeline-actor-filter')?.value || 'all';
  const typeFilter = document.getElementById('timeline-type-filter')?.value || 'all';
  const sevFilter = document.getElementById('timeline-severity-filter')?.value || 'all';
  const feedList = document.getElementById('timeline-feed-list');
  const countBadge = document.getElementById('timeline-count-badge');

  try {
    const url = (actorId && actorId !== 'all') ? `/api/intelligence-events?actor_id=${actorId}` : '/api/intelligence-events';
    const res = await fetch(url);
    const result = await res.json();
    let events = result.data || [];

    // Filter by type & severity
    if (typeFilter !== 'all') {
      events = events.filter(e => e.event_type === typeFilter);
    }
    if (sevFilter !== 'all') {
      events = events.filter(e => e.severity === sevFilter);
    }

    if (countBadge) countBadge.innerText = events.length;

    if (events.length === 0) {
      feedList.innerHTML = `
        <div style="text-align: center; color: var(--text-muted); padding: 40px;">
          <i class="fa-solid fa-calendar-xmark" style="font-size: 2rem; margin-bottom: 12px; display: block;"></i>
          No timeline events match the selected criteria.
        </div>
      `;
      return;
    }

    feedList.innerHTML = events.map(e => {
      let icon = 'fa-circle-info';
      let iconColor = 'var(--cyber-cyan)';

      if (e.event_type === 'First Seen') { icon = 'fa-eye'; iconColor = 'var(--cyber-blue)'; }
      else if (e.event_type === 'Wallet association') { icon = 'fa-wallet'; iconColor = 'var(--cyber-emerald)'; }
      else if (e.event_type === 'Infrastructure observations') { icon = 'fa-server'; iconColor = 'var(--cyber-purple)'; }
      else if (e.event_type === 'Persona linkage') { icon = 'fa-fingerprint'; iconColor = 'var(--cyber-magenta)'; }
      else if (e.event_type === 'Exploit Release') { icon = 'fa-bug'; iconColor = 'var(--cyber-crimson)'; }
      else if (e.event_type === 'Ransom Demand') { icon = 'fa-skull'; iconColor = 'var(--cyber-crimson)'; }

      const sevClass = e.severity === 'Critical' ? 'status-seized' : (e.severity === 'High' ? 'status-monitored' : 'status-active');
      const dateStr = e.event_date ? e.event_date.split('T')[0] : 'N/A';

      return `
        <div style="display: flex; gap: 20px; align-items: flex-start; background: rgba(0,0,0,0.3); border: 1px solid var(--border-card); border-radius: 8px; padding: 18px; position: relative;">
          
          <!-- Event Icon Bubble -->
          <div style="width: 42px; height: 42px; border-radius: 8px; background: rgba(255,255,255,0.03); border: 1px solid ${iconColor}; display: flex; align-items: center; justify-content: center; font-size: 1.1rem; color: ${iconColor}; flex-shrink: 0;">
            <i class="fa-solid ${icon}"></i>
          </div>

          <!-- Event Content -->
          <div style="flex: 1;">
            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 6px;">
              <div>
                <span class="font-mono" style="font-size: 0.72rem; color: var(--cyber-cyan); text-transform: uppercase; background: rgba(0,240,255,0.08); padding: 2px 6px; border-radius: 3px; margin-right: 8px;">
                  ${e.event_type}
                </span>
                <strong style="font-size: 0.95rem; color: #fff;">${e.event_title}</strong>
              </div>
              <span class="font-mono" style="font-size: 0.8rem; color: var(--text-muted);">${dateStr}</span>
            </div>

            <div style="font-size: 0.82rem; color: var(--text-secondary); line-height: 1.45; margin-bottom: 8px;">
              ${e.event_description}
            </div>

            <div style="display: flex; gap: 16px; font-size: 0.75rem; color: var(--text-muted);">
              <span>Confidence: <strong class="font-mono" style="color: var(--cyber-emerald);">${e.confidence || 85}%</strong></span>
              <span>Severity: <span class="status-badge ${sevClass}">${e.severity}</span></span>
            </div>
          </div>

        </div>
      `;
    }).join('');

  } catch (err) {
    console.error('Error loading events:', err);
    feedList.innerHTML = `<div style="color: var(--cyber-crimson); text-align: center; padding: 20px;">Failed to load events.</div>`;
  }
}
