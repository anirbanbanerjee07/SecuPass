// Generate password from backend
async function genPassword() {
  const len = parseInt(document.getElementById('length').value) || 16;
  const res = await fetch('/api/generate-password', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ length: len })
  });
  const data = await res.json();
  document.getElementById('generated').value = data.password;
  checkStrength(data.password);
}

// Simple password strength meter
function checkStrength(pw) {
  const el = document.getElementById('strength');
  let score = 0;
  if (pw.length >= 8) score++;
  if (/[a-z]/.test(pw) && /[A-Z]/.test(pw)) score++;
  if (/[0-9]/.test(pw)) score++;
  if (/[^A-Za-z0-9]/.test(pw)) score++;
  const labels = ['Very Weak','Weak','Okay','Strong','Very Strong'];
  el.textContent = 'Strength: ' + labels[score];
}

// Save entry to backend
document.getElementById('saveBtn').addEventListener('click', async () => {
  const label = document.getElementById('label').value.trim();
  const username = document.getElementById('username').value.trim();
  const password = document.getElementById('password').value.trim() || document.getElementById('generated').value;
  const notes = document.getElementById('notes').value.trim();

  if (!label || !password) {
    alert('Label and password are required');
    return;
  }

  const res = await fetch('/api/save', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ label, username, password, notes })
  });

  const data = await res.json();
  if (data.status === 'ok') {
    alert('Saved');
    refreshList();
  } else {
    alert('Error: ' + (data.message || 'unknown'));
  }
});

// Refresh saved entries
async function refreshList() {
  const res = await fetch('/api/list');
  const data = await res.json();
  const cont = document.getElementById('entries');
  cont.innerHTML = '';
  if (data.status !== 'ok') {
    cont.textContent = data.message || 'error';
    return;
  }

  data.entries.forEach(e => {
    const d = document.createElement('div');
    d.className = 'entry';

    const left = document.createElement('div');
    left.innerHTML = `
      <div><strong>${e.label}</strong> <span class="small">${e.username || ''}</span></div>
      <div class="small">Password: <code>${e.password}</code></div>
      <div class="small">${e.notes || ''}</div>
    `;

    const right = document.createElement('div');
    const del = document.createElement('button');
    del.textContent = 'Delete';
    del.style.background = '#e11d48';
    del.onclick = async () => {
      if (!confirm('Delete this entry?')) return;
      await fetch('/api/delete/' + e.id, { method: 'DELETE' });
      refreshList();
    };

    right.appendChild(del);
    d.appendChild(left);
    d.appendChild(right);
    cont.appendChild(d);
  });
}

// Event listeners
document.getElementById('genBtn').addEventListener('click', genPassword);
document.getElementById('refreshBtn').addEventListener('click', refreshList);
window.addEventListener('load', refreshList);
