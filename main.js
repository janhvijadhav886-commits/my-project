/**
 * Global JavaScript utilities, toast notifications, sidebar toggling, and search
 */

document.addEventListener('DOMContentLoaded', () => {
  // 1. Sidebar toggle
  const toggleBtn = document.getElementById('sidebar-toggle');
  const sidebar = document.getElementById('sidebar');
  if (toggleBtn && sidebar) {
    toggleBtn.addEventListener('click', () => {
      sidebar.classList.toggle('open');
    });
  }

  // 2. Global Search Event Handler & Shortcut '/'
  const globalSearch = document.getElementById('global-search-input');
  if (globalSearch) {
    globalSearch.addEventListener('keypress', (e) => {
      if (e.key === 'Enter') {
        const query = globalSearch.value.trim();
        if (query) {
          window.location.href = `/actors?search=${encodeURIComponent(query)}`;
        }
      }
    });

    // Global shortcut: press '/' to focus search input
    document.addEventListener('keydown', (e) => {
      if (e.key === '/' && document.activeElement !== globalSearch && !['INPUT', 'TEXTAREA'].includes(document.activeElement.tagName)) {
        e.preventDefault();
        globalSearch.focus();
      } else if (e.key === 'Escape' && document.activeElement === globalSearch) {
        globalSearch.blur();
      }
    });
  }

  // 3. Live Military Zulu & Local Clock Updater
  const clockEl = document.getElementById('military-clock-time');
  if (clockEl) {
    function updateClock() {
      const now = new Date();
      const h = String(now.getUTCHours()).padStart(2, '0');
      const m = String(now.getUTCMinutes()).padStart(2, '0');
      const s = String(now.getUTCSeconds()).padStart(2, '0');
      clockEl.innerText = `${h}:${m}:${s} ZULU`;
    }
    updateClock();
    setInterval(updateClock, 1000);
  }
});

// Toast notification helper
window.showToast = function(message, type = 'info') {
  const container = document.getElementById('toast-container');
  if (!container) return;

  const toast = document.createElement('div');
  toast.className = 'toast';
  
  let icon = 'fa-circle-info';
  let color = 'var(--cyber-cyan)';
  if (type === 'success') {
    icon = 'fa-circle-check';
    color = 'var(--cyber-emerald)';
  } else if (type === 'danger' || type === 'error') {
    icon = 'fa-circle-exclamation';
    color = 'var(--cyber-crimson)';
  } else if (type === 'warning') {
    icon = 'fa-triangle-exclamation';
    color = 'var(--cyber-amber)';
  }

  toast.style.borderColor = color;
  toast.innerHTML = `
    <i class="fa-solid ${icon}" style="color: ${color}; font-size: 1.1rem;"></i>
    <div style="flex: 1;">${message}</div>
    <i class="fa-solid fa-xmark" style="cursor: pointer; color: var(--text-muted);" onclick="this.parentElement.remove()"></i>
  `;

  container.appendChild(toast);

  setTimeout(() => {
    toast.style.opacity = '0';
    toast.style.transform = 'translateX(100%)';
    toast.style.transition = 'all 0.3s ease';
    setTimeout(() => toast.remove(), 300);
  }, 4000);
};

// Formatter Helpers
window.formatCurrency = (num) => `$${Number(num || 0).toLocaleString(undefined, { minimumFractionDigits: 2, maximumFractionDigits: 2 })}`;
window.formatRiskBadge = (score) => {
  const s = parseFloat(score || 0);
  if (s >= 80) return `<span class="risk-pill risk-critical"><i class="fa-solid fa-skull"></i> Critical ${s.toFixed(1)}</span>`;
  if (s >= 60) return `<span class="risk-pill risk-high"><i class="fa-solid fa-triangle-exclamation"></i> High ${s.toFixed(1)}</span>`;
  if (s >= 30) return `<span class="risk-pill risk-medium"><i class="fa-solid fa-circle-exclamation"></i> Medium ${s.toFixed(1)}</span>`;
  return `<span class="risk-pill risk-low"><i class="fa-solid fa-shield-check"></i> Low ${s.toFixed(1)}</span>`;
};
