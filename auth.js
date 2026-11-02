(() => {
  const forms = document.querySelectorAll('[data-auth-form]');

  const showToast = (message, type = 'info') => {
    const container = document.getElementById('toast-container');
    if (!container) return;
    const toast = document.createElement('div');
    toast.className = `toast toast-${type}`;
    toast.innerHTML = `<i class="fa-solid ${type === 'error' ? 'fa-circle-exclamation' : 'fa-circle-check'}"></i><span>${message}</span>`;
    container.appendChild(toast);
    setTimeout(() => toast.remove(), 5000);
  };

  document.querySelectorAll('.password-toggle').forEach((button) => {
    button.addEventListener('click', () => {
      const input = button.parentElement.querySelector('input');
      const visible = input.type === 'text';
      input.type = visible ? 'password' : 'text';
      button.setAttribute('aria-label', visible ? 'Show password' : 'Hide password');
      button.innerHTML = `<i class="fa-regular ${visible ? 'fa-eye' : 'fa-eye-slash'}"></i>`;
    });
  });

  const password = document.querySelector('#register-password');
  const meter = document.querySelector('.password-meter');
  if (password && meter) {
    password.addEventListener('input', () => {
      let strength = 0;
      if (password.value.length >= 8) strength += 1;
      if (/[A-Z]/.test(password.value) && /[a-z]/.test(password.value)) strength += 1;
      if (/\d/.test(password.value)) strength += 1;
      if (/[^A-Za-z0-9]/.test(password.value)) strength += 1;
      meter.dataset.strength = strength;
    });
  }

  forms.forEach((form) => {
    form.addEventListener('submit', async (event) => {
      event.preventDefault();
      if (!form.reportValidity()) return;
      const button = form.querySelector('.auth-submit');
      const original = button.innerHTML;
      button.disabled = true;
      button.innerHTML = '<span>Verifying channel...</span><i class="fa-solid fa-spinner fa-spin"></i>';
      const payload = Object.fromEntries(new FormData(form).entries());
      const type = form.dataset.authForm;
      if (type === 'login') payload.remember = form.elements.remember.checked;

      try {
        const response = await fetch(`/api/auth/${type}`, { method: 'POST', headers: { 'Content-Type': 'application/json' }, body: JSON.stringify(payload) });
        const data = await response.json();
        if (!response.ok) throw new Error(data.message || 'Request rejected by access gateway.');
        showToast(data.message, 'success');
        if (data.redirect_url) setTimeout(() => { window.location.href = data.redirect_url; }, 650);
      } catch (error) {
        showToast(error.message, 'error');
        button.disabled = false;
        button.innerHTML = original;
      }
    });
  });
})();
