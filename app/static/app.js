const state = { buildings: [], governorate: "", type: "" };

async function load() {
  const [bRes, sRes] = await Promise.all([
    fetch("/api/buildings"),
    fetch("/api/stats"),
  ]);
  state.buildings = await bRes.json();
  const stats = await sRes.json();
  renderCards(stats);
  populateFilters(stats);
  renderTable();
}

function renderCards(stats) {
  const topGov = Object.entries(stats.by_governorate)
    .sort((a, b) => b[1] - a[1]).slice(0, 3)
    .map(([k, v]) => `<li>${k}: ${v}</li>`).join("");
  const topType = Object.entries(stats.by_type)
    .sort((a, b) => b[1] - a[1])
    .map(([k, v]) => `<li>${k}: ${v}</li>`).join("");
  document.getElementById("cards").innerHTML = `
    <div class="card"><div class="label">Total Buildings</div><div class="value">${stats.total}</div></div>
    <div class="card"><div class="label">Total Units</div><div class="value">${stats.total_units}</div></div>
    <div class="card"><div class="label">Top Governorates</div><ul>${topGov}</ul></div>
    <div class="card"><div class="label">By Type</div><ul>${topType}</ul></div>
  `;
}

function populateFilters(stats) {
  const gov = document.getElementById("f-gov");
  const typ = document.getElementById("f-type");
  for (const k of Object.keys(stats.by_governorate).sort()) {
    gov.insertAdjacentHTML("beforeend", `<option value="${k}">${k}</option>`);
  }
  for (const k of Object.keys(stats.by_type).sort()) {
    typ.insertAdjacentHTML("beforeend", `<option value="${k}">${k}</option>`);
  }
  gov.addEventListener("change", e => { state.governorate = e.target.value; renderTable(); });
  typ.addEventListener("change", e => { state.type = e.target.value; renderTable(); });
  document.getElementById("f-reset").addEventListener("click", () => {
    state.governorate = ""; state.type = "";
    gov.value = ""; typ.value = "";
    renderTable();
  });
}

function renderTable() {
  const rows = state.buildings.filter(b =>
    (!state.governorate || b.governorate === state.governorate) &&
    (!state.type || b.type === state.type)
  );
  const tbody = document.querySelector("#tbl tbody");
  tbody.innerHTML = rows.map(b => `
    <tr>
      <td>${b.id}</td><td>${b.building_no}</td><td>${b.governorate}</td>
      <td>${b.wilayat}</td><td>${b.type}</td><td>${b.units}</td>
      <td>${b.lat.toFixed(4)}</td><td>${b.lng.toFixed(4)}</td>
    </tr>
  `).join("");
  document.getElementById("empty").hidden = rows.length > 0;
  document.getElementById("tbl").hidden = rows.length === 0;
}

load();
