// Client-side models for the dashboard; mirrors pipeline/active_learning.py (GP),
// pipeline/strength_model.py and pipeline/hea_properties.density. Checked by tests/test_dashboard.py.
const ELS = ["W", "Mo", "Ta", "Nb", "V"], FREE = ["Mo", "Ta", "Nb", "V"];
const K_B = 8.617333262e-5, GPA_A3_TO_EV = 1e9 * 1e-30 / 1.602176634e-19;
let D;
function setData(d) { D = d; }

function gpPredict(g, x) {
  const n = D.X.length, k = new Float64Array(n);
  for (let i = 0; i < n; i++) {
    let s = 0;
    for (let j = 0; j < 5; j++) { const d = (x[j] - D.X[i][j]) / g.length[j]; s += d * d; }
    k[i] = g.const * Math.exp(-0.5 * s);
  }
  let mu = 0; for (let i = 0; i < n; i++) mu += k[i] * g.alpha[i];
  const v = new Float64Array(n);                       // forward substitution L v = k
  for (let i = 0; i < n; i++) { let s = k[i]; for (let j = 0; j < i; j++) s -= g.L[i][j] * v[j]; v[i] = s / g.L[i][i]; }
  let vv = 0; for (let i = 0; i < n; i++) vv += v[i] * v[i];
  const varN = Math.max(g.const + g.noise - vv, 0);
  return {mu: mu * g.y_std + g.y_mean, sd: Math.sqrt(varN) * g.y_std * g.calib};
}

function strength(c, T) {
  const S = D.strength, f = ELS.map(e => c[e] / 100);
  const V = ELS.map(e => S.lattice_A[e] ** 3 / 2);
  const vbar = f.reduce((a, x, i) => a + x * V[i], 0);
  let mis = 0; f.forEach((x, i) => mis += x * (V[i] - vbar) ** 2);
  const C = [0, 1, 2].map(j => f.reduce((a, x, i) => a + x * S.elastic_GPa[ELS[i]][j], 0));
  const mu = Math.sqrt(0.5 * C[2] * (C[0] - C[1])), B = (C[0] + 2 * C[1]) / 3;
  const nu = (3 * B - 2 * mu) / (2 * (3 * B + mu));
  const b = Math.sqrt(3) / 2 * Math.cbrt(2 * vbar), pf = (1 + nu) / (1 - nu), x = mis / b ** 6;
  const tau0 = 0.040 * S.alpha ** (-1 / 3) * mu * pf ** (4 / 3) * x ** (2 / 3) * 1e3;
  const de = 2.00 * S.alpha ** (1 / 3) * mu * b ** 3 * pf ** (2 / 3) * x ** (1 / 3) * GPA_A3_TO_EV;
  if (!(de > 0)) return 0;
  const s = K_B * T / de * Math.log(S.eps0 / S.strain_rate), low = 1 - s ** (2 / 3);
  return S.taylor * tau0 * (low > 0.5 ? low : Math.exp(-s / 0.55));
}

function density(c) {
  let m = 0, v = 0;
  ELS.forEach(e => { const x = c[e] / 100; m += x * D.mass[e]; v += x * D.mass[e] / D.rho[e]; });
  return m / v;
}

const normCdf = z => 0.5 * (1 + erf(z / Math.SQRT2));
function erf(x) { const t = 1 / (1 + 0.3275911 * Math.abs(x)), y = 1 - (((((1.061405429 * t - 1.453152027) * t) + 1.421413741) * t - 0.284496736) * t + 0.254829592) * t * Math.exp(-x * x); return x >= 0 ? y : -y; }

function full(c) { const w = 100 - FREE.reduce((a, e) => a + c[e], 0); return {W: w, ...c}; }

function predict(c) {
  const fc = full(c), x = ELS.map(e => fc[e] / 100);
  const sol = gpPredict(D.gp_solidus, x), sp = gpPredict(D.gp_split, x);
  let dmin = Infinity; D.X.forEach(r => { let s = 0; for (let j = 0; j < 5; j++) s += (r[j] - x[j]) ** 2; dmin = Math.min(dmin, Math.sqrt(s)); });
  return {fc, sol, sp, p: normCdf((D.split_goal - sp.mu) / Math.max(sp.sd, 1e-6)), rho: density(fc),
          ys25: strength(fc, 298.15), ys1300: strength(fc, 1573.15), dmin};
}


if (typeof module !== "undefined") module.exports = {setData, predict, full};
