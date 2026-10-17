(function () {
'use strict';
var D = window.DATA, $main = document.getElementById('main');
var ALLQ = D.questions.concat(D.numericals), QBY = {};
ALLQ.forEach(function (q) { QBY[q.id] = q; });
var KEY = 'sts_prep_v1';

/* ---------- storage (local to this browser only) ---------- */
function blank() { return { attempts: [], quizzes: [], bookmarks: [], completed: {}, hardCards: [], activity: [] }; }
var S = blank(), storageOK = true;
try { var raw = localStorage.getItem(KEY); if (raw) S = Object.assign(blank(), JSON.parse(raw)); } catch (e) { storageOK = false; }
function save() { try { localStorage.setItem(KEY, JSON.stringify(S)); } catch (e) { storageOK = false; } }
function log(msg) { S.activity.unshift({ t: Date.now(), m: msg }); S.activity = S.activity.slice(0, 30); save(); }

/* ---------- helpers ---------- */
function h(s) { return String(s == null ? '' : s).replace(/[&<>"']/g, function (c) { return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[c]; }); }
function toast(m) { var t = document.getElementById('toast'); t.textContent = m; t.style.display = 'block'; clearTimeout(toast.t); toast.t = setTimeout(function () { t.style.display = 'none'; }, 2200); }
function shuffle(a) { a = a.slice(); for (var i = a.length - 1; i > 0; i--) { var j = Math.floor(Math.random() * (i + 1)); var t = a[i]; a[i] = a[j]; a[j] = t; } return a; }
function pct(a, b) { return b ? Math.round(a / b * 100) : 0; }
function uniq(a) { return a.filter(function (x, i) { return a.indexOf(x) === i; }); }
function wkTitle(n) { var w = D.weeks[n - 1]; return w ? 'Week ' + n + ': ' + w.title : 'General'; }
function sameSet(a, b) { return a.length === b.length && a.every(function (x) { return b.indexOf(x) > -1; }); }
function fmtTime(s) { s = Math.max(0, s); var m = Math.floor(s / 60), r = s % 60; return (m < 10 ? '0' : '') + m + ':' + (r < 10 ? '0' : '') + r; }
function csvCell(v) { v = v == null ? '' : String(v); return /[",\n]/.test(v) ? '"' + v.replace(/"/g, '""') + '"' : v; }
function download(name, text, mime) {
  try { var b = new Blob([text], { type: mime || 'text/csv;charset=utf-8' }), a = document.createElement('a'); a.href = URL.createObjectURL(b); a.download = name; document.body.appendChild(a); a.click(); a.remove(); setTimeout(function () { URL.revokeObjectURL(a.href); }, 500); toast('Downloaded ' + name); }
  catch (e) { toast('Download not supported in this browser'); }
}
function srcTag(q) { var off = q.source.type !== 'generated'; return '<span class="tag' + (off ? ' off' : ' gen') + '" title="' + h(q.source.verification) + '">' + (off ? '\u2605 ' : '') + h(q.source.label) + '</span>'; }
function stats(filter) { // per question: latest attempt
  var a = S.attempts.filter(filter || function () { return true; });
  var c = a.filter(function (x) { return x.ok; }).length; return { n: a.length, c: c, acc: pct(c, a.length) };
}
function record(q, ok) { S.attempts.push({ qid: q.id, ok: !!ok, t: Date.now(), week: q.week, topic: q.topic }); save(); }
function latestWrong() { var last = {}; S.attempts.forEach(function (a) { last[a.qid] = a; }); return Object.keys(last).filter(function (k) { return !last[k].ok && QBY[k]; }); }
function weekOpts(sel) { var o = '<option value="">All weeks</option>'; D.weeks.forEach(function (w) { o += '<option value="' + w.id + '"' + (String(sel) === String(w.id) ? ' selected' : '') + '>Week ' + w.id + ' - ' + h(w.title.slice(0, 50)) + '</option>'; }); return o; }
function topicsFor(wk) { return uniq(ALLQ.filter(function (q) { return !wk || q.week == wk; }).map(function (q) { return q.topic; })).sort(); }

/* ---------- router ---------- */
var R = {};
var cleanup = null;
function route() {
  if (cleanup) { cleanup(); cleanup = null; }
  var hash = location.hash.replace(/^#\/?/, '').split('?')[0], parts = hash.split('/'), name = parts[0] || 'home', arg = parts.slice(1).join('/');
  document.querySelectorAll('.nav a').forEach(function (a) { a.classList.toggle('on', a.getAttribute('href') === '#/' + (name === 'home' ? '' : name) || (name === 'week' && a.getAttribute('href') === '#/weeks')); });
  var f = R[name] || R.notfound;
  f(decodeURIComponent(arg));
  document.getElementById('nav').classList.remove('open');
  document.getElementById('menuBtn').setAttribute('aria-expanded', 'false');
  window.scrollTo(0, 0);
}
function render(html) { $main.innerHTML = html; }

/* ---------- dashboard ---------- */
R.home = function () {
  var st = stats(), done = Object.keys(S.completed).filter(function (k) { return S.completed[k]; }).length;
  var wrong = latestWrong(), wk = weekPerf().filter(function (x) { return x.n >= 2 && x.acc < 60; }).sort(function (a, b) { return a.acc - b.acc; }).slice(0, 4);
  var topics = topicPerf().filter(function (x) { return x.n >= 2 && x.acc < 60; }).sort(function (a, b) { return a.acc - b.acc; }).slice(0, 5);
  var uniqAtt = uniq(S.attempts.map(function (a) { return a.qid; })).length;
  var nextWeek = 1; for (var i = 1; i <= 12; i++) { if (!S.completed[i]) { nextWeek = i; break; } }
  var g = D.weeks.map(function (w) { var s = stats(function (a) { return a.week == w.id; }); return '<a class="weekcard" href="#/week/' + w.id + '"><b>Week ' + w.id + '</b>' + (S.completed[w.id] ? ' ✔' : '') + '<div>' + h(w.title) + '</div><div class="bar"><i style="width:' + (S.completed[w.id] ? 100 : 0) + '%"></i></div><div class="mut">' + (s.n ? 'Accuracy ' + s.acc + '% (' + s.n + ' attempts)' : 'No attempts yet') + '</div></a>'; }).join('');
  render('<h1>' + h(D.course.name) + '</h1><p class="mut">' + h(D.course.institute) + ' · ' + h(D.course.instructor) + ' · Course ' + h(D.course.code) + ' · 12 weeks. <b>Unofficial</b> study platform; not affiliated with NPTEL.</p>' +
    '<div class="row"><a class="btn" href="#/week/' + nextWeek + '">Continue studying (Week ' + nextWeek + ')</a><a class="btn sec" href="#/quiz">Start practice quiz</a><a class="btn sec" href="#/mocks">Start mock examination</a><a class="btn sec" href="#/official">Official assignments by year</a><a class="btn sec" href="#/quiz?source=generated">Self-made practice</a></div>' +
    '<div class="grid"><div class="card"><div class="stat">' + done + ' / 12</div>weeks completed<div class="bar"><i style="width:' + pct(done, 12) + '%"></i></div></div>' +
    '<div class="card"><div class="stat">' + ALLQ.length + '</div>questions available<div class="mut">' + uniqAtt + ' attempted</div></div>' +
    '<div class="card"><div class="stat">' + (st.n ? st.acc + '%' : '-') + '</div>overall accuracy<div class="mut">' + st.c + ' correct of ' + st.n + ' answers</div></div>' +
    '<div class="card"><div class="stat">' + S.bookmarks.length + '</div>bookmarked<div class="mut"><a href="#/review">View bookmarks &amp; ' + wrong.length + ' mistakes</a></div></div></div>' +
    '<h2>Weekly modules</h2><div class="grid">' + g + '</div>' +
    '<h2>Recent quiz results</h2>' + (S.quizzes.length ? '<div class="card tbl"><table><tr><th>When</th><th>Quiz</th><th>Score</th></tr>' + S.quizzes.slice(-5).reverse().map(function (z) { return '<tr><td>' + new Date(z.t).toLocaleString() + '</td><td>' + h(z.title) + '</td><td>' + z.score + '/' + z.total + ' (' + pct(z.score, z.total) + '%)</td></tr>'; }).join('') + '</table></div>' : '<div class="card mut">No quizzes taken yet.</div>') +
    '<h2>Weak areas needing revision</h2><div class="card">' + (wk.length || topics.length ? (wk.map(function (x) { return '<a class="tag" href="#/week/' + x.week + '">Week ' + x.week + ' · ' + x.acc + '%</a>'; }).join('') + topics.map(function (x) { return '<span class="tag">' + h(x.topic) + ' · ' + x.acc + '%</span>'; }).join('')) : '<span class="mut">Answer at least 2 questions per week/topic to see weak areas (below 60%).</span>') + '</div>' +
    '<h2>Recent activity</h2><div class="card">' + (S.activity.slice(0, 6).map(function (a) { return '<div>' + new Date(a.t).toLocaleString() + ' - ' + h(a.m) + '</div>'; }).join('') || '<span class="mut">Nothing yet.</span>') + '</div>' +
    '<p class="mut">' + (storageOK ? 'Progress is saved only in this browser (localStorage). It does not sync between devices and is lost if you clear site data. Use Progress &amp; export to back up.' : 'Browser storage is unavailable: progress will not be saved.') + '</p>');
};
function weekPerf() { return D.weeks.map(function (w) { var s = stats(function (a) { return a.week == w.id; }); return { week: w.id, n: s.n, acc: s.acc, c: s.c }; }); }
function topicPerf() { var m = {}; S.attempts.forEach(function (a) { var k = a.topic; m[k] = m[k] || { topic: k, n: 0, c: 0 }; m[k].n++; if (a.ok) m[k].c++; }); return Object.keys(m).map(function (k) { m[k].acc = pct(m[k].c, m[k].n); return m[k]; }); }

/* ---------- study pages ---------- */
R.weeks = function () {
  render('<h1>Study modules</h1><p class="mut">Titles follow the official NPTEL syllabus PDF for course 105107210.</p><div class="grid">' + D.weeks.map(function (w) { return '<a class="weekcard" href="#/week/' + w.id + '"><b>Week ' + w.id + '</b>' + (S.completed[w.id] ? ' ✔' : '') + '<div>' + h(w.title) + '</div></a>'; }).join('') + '</div>');
};
function list(a) { return '<ul>' + a.map(function (x) { return '<li>' + h(x) + '</li>'; }).join('') + '</ul>'; }
R.week = function (arg) {
  var n = parseInt(arg, 10), w = D.weeks[n - 1];
  if (!w) return R.notfound();
  var wq = ALLQ.filter(function (q) { return q.week === n; });
  render('<p><a href="#/weeks">&larr; All weeks</a></p><h1>Week ' + n + ': ' + h(w.title) + '</h1>' +
    '<div class="row noprint"><button class="btn" id="done">' + (S.completed[n] ? 'Mark as not completed' : 'Mark week completed') + '</button><a class="btn sec" href="#/quiz?week=' + n + '" data-quiz="' + n + '">Practice this week (' + wq.length + ' Q)</a><a class="btn sec" href="#/flashcards?week=' + n + '">Flashcards</a><button class="btn sec" onclick="window.print()">Print notes</button>' + (n > 1 ? '<a class="btn sec" href="#/week/' + (n - 1) + '">Prev</a>' : '') + (n < 12 ? '<a class="btn sec" href="#/week/' + (n + 1) + '">Next</a>' : '') + '</div>' +
    '<div class="card"><h2>Overview</h2><p>' + h(w.overview) + '</p><h3>Learning objectives</h3>' + list(w.objectives) + '</div>' +
    '<div class="card"><h2>Notes</h2>' + w.notes.map(function (s) { return '<h3>' + h(s.h) + '</h3>' + s.p.map(function (p) { return '<p>' + h(p) + '</p>'; }).join(''); }).join('') + '</div>' +
    '<div class="card"><h2>Important definitions</h2>' + w.definitions.map(function (d) { return '<p><b>' + h(d.term) + ':</b> ' + h(d.def_) + '</p>'; }).join('') + '<h2>Key concepts</h2>' + list(w.concepts) + '</div>' +
    '<div class="card"><h2>Formulas and units</h2><div class="tbl"><table><tr><th>Name</th><th>Formula</th><th>Unit</th></tr>' + w.formulas.map(function (f) { return '<tr><td>' + h(f.name) + '</td><td><code>' + h(f.formula) + '</code></td><td>' + h(f.unit) + '</td></tr>'; }).join('') + '</table></div>' +
    '<h3>Worked example</h3><p>' + h(w.example.q) + '</p><ol>' + w.example.steps.map(function (s) { return '<li>' + h(s) + '</li>'; }).join('') + '</ol><p><b>Answer:</b> ' + h(w.example.ans) + '</p></div>' +
    '<div class="card"><h2>Real-world applications</h2>' + list(w.applications) + '<h2>Case studies</h2>' + list(w.cases) + '<p class="mut">Case references are general pointers; consult the lectures and public project documents for details.</p></div>' +
    '<div class="card"><h2>Common misconceptions</h2>' + list(w.misconceptions) + '<h2>Quick revision</h2>' + list(w.revision) + '</div>' +
    '<div class="card"><h2>References</h2>' + list(w.refs) + '<p class="mut">These notes are original summaries written for this app from the syllabus and standard references. They are not a substitute for the lectures.</p></div>');
  document.getElementById('done').onclick = function () { S.completed[n] = !S.completed[n]; save(); log((S.completed[n] ? 'Completed' : 'Un-completed') + ' Week ' + n); R.week(arg); };
  var qa = $main.querySelector('[data-quiz]'); if (qa) qa.onclick = function (e) { e.preventDefault(); startQuiz({ week: n, count: Math.min(10, wq.length), mode: 'practice', title: 'Week ' + n + ' practice' }); };
};

/* ---------- quiz setup ---------- */
function qparam() { var m = {}; (location.hash.split('?')[1] || '').split('&').forEach(function (p) { var kv = p.split('='); if (kv[0]) m[kv[0]] = decodeURIComponent(kv[1] || ''); }); return m; }
R.quiz = function () {
  var p = qparam();
  render('<h1>Practice quiz</h1><div class="card"><form id="qf"><div class="formgrid">' +
    '<div><label for="fw">Week</label><select id="fw">' + weekOpts(p.week) + '</select></div>' +
    '<div><label for="ft">Topic</label><select id="ft"></select></div>' +
    '<div><label for="fd">Difficulty</label><select id="fd"><option value="">Any</option><option>easy</option><option>medium</option><option>hard</option></select></div>' +
    '<div><label for="ff">Question type</label><select id="ff"><option value="">Any</option><option value="mcq">Single-answer MCQ</option><option value="multi">Multiple-select</option><option value="tf">True / False</option><option value="ar">Assertion-reason</option><option value="num">Numerical</option></select></div>' +
    '<div><label for="fs">Category</label><select id="fs"><option value="">Any</option><option value="assignment">Official assignments</option><option value="generated">Self-made practice (reviewed)</option></select></div><div><label for="fy">Official year</label><select id="fy"><option value="">Any</option>' + [2021, 2022, 2023, 2024, 2025, 2026].map(function (y) { return '<option>' + y + '</option>'; }).join('') + '</select></div><div><label for="fn">Number of questions</label><input id="fn" type="number" min="1" max="100" value="10"></div>' +
    '<div><label for="fm">Mode</label><select id="fm"><option value="practice">Practice (instant feedback)</option><option value="timed">Timed (answers at the end)</option></select></div>' +
    '<div><label for="fmin">Minutes (timed)</label><input id="fmin" type="number" min="1" max="180" value="15"></div>' +
    '</div><p id="avail" class="mut"></p><button class="btn" type="submit">Start quiz</button></form></div>');
  var fw = document.getElementById('fw'), ft = document.getElementById('ft');
  function fillTopics() { ft.innerHTML = '<option value="">All topics</option>' + topicsFor(fw.value).map(function (t) { return '<option>' + h(t) + '</option>'; }).join(''); upd(); }
  function cfg() { return { week: fw.value, topic: ft.value, difficulty: document.getElementById('fd').value, format: document.getElementById('ff').value, source: document.getElementById('fs').value, year: document.getElementById('fy').value }; }
  function upd() { document.getElementById('avail').textContent = filterQ(cfg()).length + ' questions match these filters.'; }
  if (p.source) document.getElementById('fs').value = p.source; if (p.year) document.getElementById('fy').value = p.year; fw.onchange = fillTopics; ['ft', 'fd', 'ff', 'fs', 'fy'].forEach(function (i) { document.getElementById(i).onchange = upd; }); fillTopics();
  document.getElementById('qf').onsubmit = function (e) {
    e.preventDefault(); var c = cfg(); c.count = parseInt(document.getElementById('fn').value, 10); c.mode = document.getElementById('fm').value; c.minutes = parseInt(document.getElementById('fmin').value, 10);
    if (!(c.count >= 1)) return toast('Enter a valid number of questions');
    if (c.mode === 'timed' && !(c.minutes >= 1)) return toast('Enter a valid time limit');
    c.title = 'Custom quiz' + (c.week ? ' (Week ' + c.week + ')' : ''); startQuiz(c);
  };
};
function filterQ(c) { return ALLQ.filter(function (q) { return (!c.week || q.week == c.week) && (!c.topic || q.topic === c.topic) && (!c.difficulty || q.difficulty === c.difficulty) && (!c.format || q.format === c.format) && (!c.source || q.source.type === c.source) && (!c.year || (q.years || []).indexOf(+c.year) > -1); }); }

/* ---------- quiz engine (used by quizzes, mocks and retries) ---------- */
var Z = null; // active session
function startQuiz(c) {
  var pool = c.ids ? c.ids.map(function (i) { return QBY[i]; }).filter(Boolean) : shuffle(filterQ(c));
  if (!pool.length) { toast('No questions match those filters'); return; }
  var qs = pool.slice(0, c.count || pool.length);
  if (!c.keepOrder && !c.ids) qs = shuffle(qs);
  Z = { minutes: c.minutes, title: c.title || 'Quiz', mode: c.mode || 'practice', retry: !!c.retry, i: 0, done: false, mockId: c.mockId || null,
    endAt: c.mode === 'timed' ? Date.now() + (c.minutes || 15) * 60000 : null,
    items: qs.map(function (q) { var n = q.options ? q.options.length : 0, order = q.format === 'tf' || q.format === 'ar' ? n ? Array.apply(null, Array(n)).map(function (_, k) { return k; }) : [] : shuffle(Array.apply(null, Array(n)).map(function (_, k) { return k; })); return { q: q, order: order, sel: [], val: '', marked: false, submitted: false, ok: null }; }) };
  var was = location.hash === '#/run'; location.hash = '#/run'; if (was) route();
}
R.run = function () {
  if (!Z) { render('<div class="card">No active quiz. <a href="#/quiz">Start one</a>.</div>'); return; }
  if (Z.done) return showResults();
  var z = Z, it = z.items[z.i], q = it.q, instant = z.mode === 'practice', timed = z.mode === 'timed';
  var ans = z.items.filter(function (x) { return x.sel.length || x.val !== ''; }).length;
  var html = '<div class="row"><b>' + h(z.title) + '</b><span class="mut">Question ' + (z.i + 1) + ' of ' + z.items.length + ' · answered ' + ans + '</span>' + (timed ? '<span class="timer" id="tm"></span>' : '') + '</div>' +
    '<div class="bar"><i style="width:' + pct(z.i + 1, z.items.length) + '%"></i></div>' +
    '<div class="card"><div><span class="tag">Week ' + q.week + '</span><span class="tag">' + h(q.topic) + '</span><span class="tag">' + q.difficulty + '</span><span class="tag">' + ({ mcq: 'Single answer', multi: 'Select ALL that apply', tf: 'True/False', ar: 'Assertion-reason', num: 'Numerical' }[q.format]) + '</span>' + (instant ? srcTag(q) : '') + '</div>' +
    '<h2 style="margin-top:.6em">' + h(q.format === 'num' ? q.text : q.text) + '</h2>';
  if (q.format === 'num') {
    html += '<label for="nv">Your answer (' + h(q.unit) + ')</label><input id="nv" type="number" step="any" inputmode="decimal" value="' + h(it.val) + '"' + (it.submitted ? ' disabled' : '') + '>';
  } else {
    html += it.order.map(function (oi, k) {
      var cls = 'opt', on = it.sel.indexOf(oi) > -1, correct = q.answer.indexOf(oi) > -1;
      if (on) cls += ' sel';
      if (it.submitted && instant) { if (correct) cls += ' right'; else if (on) cls += ' wrong'; }
      return '<button type="button" class="' + cls + '" data-o="' + oi + '" role="' + (q.format === 'multi' ? 'checkbox' : 'radio') + '" aria-checked="' + on + '"' + (it.submitted && instant ? ' disabled' : '') + '><span class="k">' + String.fromCharCode(65 + k) + '.</span><span>' + h(q.options[oi]) + '</span></button>';
    }).join('');
  }
  html += '</div>';
  if (it.submitted && instant) html += feedback(it);
  html += '<div class="row">' +
    '<button class="btn sec" id="prev"' + (z.i === 0 ? ' disabled' : '') + '>Previous</button>' +
    (instant && !it.submitted ? '<button class="btn" id="sub">Submit answer</button>' : '') +
    '<button class="btn sec" id="mark">' + (it.marked ? 'Unmark review' : 'Mark for review') + '</button>' +
    '<button class="btn sec" id="bm">' + (S.bookmarks.indexOf(q.id) > -1 ? 'Remove bookmark' : 'Bookmark') + '</button>' +
    (z.i < z.items.length - 1 ? '<button class="btn" id="next">Next</button>' : '') +
    '<button class="btn ' + (z.i === z.items.length - 1 ? '' : 'sec') + '" id="fin">Finish &amp; submit</button></div>' +
    '<h3>Question palette</h3><div class="pal" role="group" aria-label="Question palette">' + z.items.map(function (x, k) { var c = (x.sel.length || x.val !== '' ? 'ans ' : '') + (x.marked ? 'mk ' : '') + (k === z.i ? 'cur' : ''); return '<button class="' + c + '" data-g="' + k + '" aria-label="Question ' + (k + 1) + (x.marked ? ' marked' : '') + '">' + (k + 1) + '</button>'; }).join('') + '</div><p class="mut">Highlighted = answered · orange border = marked for review.</p>';
  render(html);
  if (timed) tick();
  var set = function (id, fn) { var e = document.getElementById(id); if (e) e.onclick = fn; };
  $main.querySelectorAll('.opt').forEach(function (b) { b.onclick = function () { if (it.submitted && instant) return; var oi = +b.dataset.o; if (q.format === 'multi') { var p = it.sel.indexOf(oi); if (p > -1) it.sel.splice(p, 1); else it.sel.push(oi); } else it.sel = [oi]; R.run(); }; });
  var nv = document.getElementById('nv'); if (nv) nv.oninput = function () { it.val = nv.value; };
  $main.querySelectorAll('[data-g]').forEach(function (b) { b.onclick = function () { saveVal(); z.i = +b.dataset.g; R.run(); }; });
  function saveVal() { var e = document.getElementById('nv'); if (e) it.val = e.value; }
  set('prev', function () { saveVal(); z.i--; R.run(); });
  set('next', function () { saveVal(); z.i++; R.run(); });
  set('mark', function () { saveVal(); it.marked = !it.marked; R.run(); });
  set('bm', function () { saveVal(); toggleBm(q.id); R.run(); });
  set('sub', function () { saveVal(); if (!hasAnswer(it)) return toast('Select or enter an answer first'); grade(it); record(q, it.ok); R.run(); });
  set('fin', function () { saveVal(); var un = z.items.filter(function (x) { return !hasAnswer(x); }).length, mk = z.items.filter(function (x) { return x.marked; }).length; if (confirm('Submit now?\n' + un + ' unanswered, ' + mk + ' marked for review.')) finish(); });
};
function hasAnswer(it) { return it.q.format === 'num' ? (it.val !== '' && !isNaN(parseFloat(it.val))) : it.sel.length > 0; }
function grade(it) {
  var q = it.q; it.submitted = true;
  if (q.format === 'num') { var v = parseFloat(it.val); it.ok = !isNaN(v) && Math.abs(v - q.answer) <= q.tolerance + 1e-9; }
  else it.ok = sameSet(it.sel.slice(), q.answer);
  return it.ok;
}
function feedback(it) {
  var q = it.q, right;
  if (q.format === 'num') right = '<b>Correct answer:</b> ' + q.answer + ' ' + h(q.unit) + ' (accepted within ±' + q.tolerance + ')' + numSteps(q);
  else right = '<b>Correct answer:</b> ' + q.answer.map(function (a) { return h(q.options[a]); }).join('; ');
  var partial = (q.format === 'multi' && !it.ok && it.sel.length) ? '<br><small>Multiple-select questions are marked correct only when the selected set exactly matches.</small>' : '';
  return '<div class="fb ' + (it.ok ? 'ok' : 'bad') + '"><b>' + (it.ok ? 'Correct.' : (hasAnswer(it) ? 'Incorrect.' : 'Not answered.')) + '</b> ' + right + partial + '</div><div class="card"><b>Explanation:</b> ' + h(q.explanation) + wrongWhy(it) + '</div>';
}
function wrongWhy(it) { var q = it.q; if (q.format === 'num' || !it.sel.length) return ''; var bad = it.sel.filter(function (s) { return q.answer.indexOf(s) < 0; }); return bad.length ? '<p class="mut">Why your choice' + (bad.length > 1 ? 's do' : ' does') + ' not fit: ' + bad.map(function (b) { return '"' + h(q.options[b]) + '"'; }).join(', ') + ' - ' + 'see the explanation above for the governing concept.</p>' : ''; }
function numSteps(q) { return '<p><b>Formula:</b> <code>' + h(q.formula) + '</code></p><ol>' + q.steps.map(function (s) { return '<li>' + h(s) + '</li>'; }).join('') + '</ol>'; }
function tick() { var z = Z; if (!z || !z.endAt || z.done) return; var e = document.getElementById('tm'); var left = Math.round((z.endAt - Date.now()) / 1000); if (e) e.textContent = '⏱ ' + fmtTime(left); if (left <= 0) { toast('Time is up - submitting'); finish(); return; } cleanup = (function (t) { return function () { clearTimeout(t); }; })(setTimeout(tick, 500)); }
function finish() {
  var z = Z; if (!z || z.done) return;
  z.items.forEach(function (it) { if (!it.submitted) { var had = hasAnswer(it); grade(it); if (had || z.mode === 'timed') record(it.q, it.ok); if (!had) it.ok = false; } });
  z.done = true; z.score = z.items.filter(function (x) { return x.ok; }).length;
  S.quizzes.push({ t: Date.now(), title: z.title, mock: z.mockId, score: z.score, total: z.items.length, mode: z.mode }); log('Finished "' + z.title + '": ' + z.score + '/' + z.items.length); save();
  route();
}
function showResults() {
  var z = Z, wrongs = z.items.filter(function (x) { return !x.ok; });
  var tp = {}; z.items.forEach(function (x) { var k = 'Week ' + x.q.week; tp[k] = tp[k] || { n: 0, c: 0 }; tp[k].n++; if (x.ok) tp[k].c++; });
  var weak = Object.keys(tp).filter(function (k) { return tp[k].c / tp[k].n < 0.6; });
  render('<h1>Results: ' + h(z.title) + '</h1><div class="card"><div class="stat">' + z.score + ' / ' + z.items.length + ' (' + pct(z.score, z.items.length) + '%)</div>' + z.items.filter(function (x) { return !hasAnswer(x); }).length + ' unanswered · ' + wrongs.length + ' not correct</div>' +
    '<div class="row noprint"><button class="btn" id="retry"' + (wrongs.length ? '' : ' disabled') + '>Retry incorrect (' + wrongs.length + ')</button><button class="btn sec" id="again">Restart this quiz</button><a class="btn sec" href="#/quiz">New quiz</a><button class="btn sec" id="csv">Download results CSV</button><button class="btn sec" onclick="window.print()">Print</button></div>' +
    '<h2>Topic-wise performance</h2><div class="card tbl"><table><tr><th>Week</th><th>Correct</th><th>Accuracy</th></tr>' + Object.keys(tp).map(function (k) { return '<tr><td>' + k + '</td><td>' + tp[k].c + '/' + tp[k].n + '</td><td>' + pct(tp[k].c, tp[k].n) + '%</td></tr>'; }).join('') + '</table></div>' +
    '<h2>Recommendation</h2><div class="fb info">' + (weak.length ? 'Revise: ' + weak.map(function (k) { var n = k.split(' ')[1]; return '<a href="#/week/' + n + '">' + k + '</a>'; }).join(', ') + ' (below 60%).' : 'No week below 60% in this attempt. Keep practising mixed questions.') + ' This is an unofficial test and does not predict the real exam.</div>' +
    '<h2>Question-wise review</h2>' + z.items.map(function (it, k) {
      var q = it.q, mine = q.format === 'num' ? (it.val === '' ? '(none)' : it.val) : (it.sel.length ? it.sel.map(function (s) { return h(q.options[s]); }).join('; ') : '(none)');
      return '<div class="card"><b>Q' + (k + 1) + '. ' + (it.ok ? '✔' : '✘') + '</b> <span class="tag">Week ' + q.week + '</span><span class="tag">' + h(q.topic) + '</span> ' + srcTag(q) + '<p>' + h(q.text) + '</p><p><b>Your answer:</b> ' + (q.format === 'num' ? h(mine) : mine) + '</p>' + feedback(it).replace(/<div class="fb[^>]*>.*?<\/div>/, '<p><b>Correct answer:</b> ' + (q.format === 'num' ? q.answer + ' ' + h(q.unit) : q.answer.map(function (a) { return h(q.options[a]); }).join('; ')) + '</p>') + '<button class="btn sec noprint" data-bm="' + q.id + '">' + (S.bookmarks.indexOf(q.id) > -1 ? 'Remove bookmark' : 'Bookmark') + '</button></div>';
    }).join(''));
  document.getElementById('retry').onclick = function () { startQuiz({ ids: wrongs.map(function (x) { return x.q.id; }), mode: 'practice', title: 'Retry: ' + z.title, retry: true }); };
  document.getElementById('again').onclick = function () { startQuiz({ ids: z.items.map(function (x) { return x.q.id; }), mode: z.mode === 'timed' ? 'timed' : 'practice', minutes: z.minutes || 15, title: z.title, mockId: z.mockId }); };
  document.getElementById('csv').onclick = function () { var rows = [['question_id', 'week', 'topic', 'result', 'your_answer', 'correct_answer']].concat(z.items.map(function (it) { var q = it.q; return [q.id, q.week, q.topic, it.ok ? 'correct' : 'incorrect', q.format === 'num' ? it.val : it.sel.map(function (s) { return q.options[s]; }).join('|'), q.format === 'num' ? q.answer : q.answer.map(function (a) { return q.options[a]; }).join('|')]; })); download('quiz-results.csv', rows.map(function (r) { return r.map(csvCell).join(','); }).join('\n')); };
  $main.querySelectorAll('[data-bm]').forEach(function (b) { b.onclick = function () { toggleBm(b.dataset.bm); b.textContent = S.bookmarks.indexOf(b.dataset.bm) > -1 ? 'Remove bookmark' : 'Bookmark'; }; });
}
function toggleBm(id) { var p = S.bookmarks.indexOf(id); if (p > -1) { S.bookmarks.splice(p, 1); toast('Bookmark removed'); } else { S.bookmarks.push(id); toast('Bookmarked'); } save(); }

/* ---------- mocks ---------- */
R.mocks = function () {
  render('<h1>Mock examinations</h1><div class="fb info">These are <b>unofficial</b> mock tests built from this app\'s newly written question bank. The official NPTEL exam pattern was not verifiable from public pages here, so no claim is made about matching it. They do not predict the real exam. Mocks share questions with the bank and may overlap each other.</div>' +
    D.mocks.map(function (m) { var best = S.quizzes.filter(function (z) { return z.mock === m.id; }).map(function (z) { return pct(z.score, z.total); }); return '<div class="card"><h2>' + h(m.title) + '</h2><p>' + m.ids.length + ' questions · covers weeks ' + uniq(m.ids.map(function (i) { return QBY[i].week; })).sort(function (a, b) { return a - b; }).join(', ') + '</p><label for="mt' + m.id + '">Time limit (minutes)</label><input id="mt' + m.id + '" type="number" min="1" max="240" value="' + m.minutes + '" style="max-width:140px"><p class="mut">' + (best.length ? 'Attempts: ' + best.length + ' · best ' + Math.max.apply(null, best) + '%' : 'Not attempted') + '</p><button class="btn" data-m="' + m.id + '">Start</button></div>'; }).join(''));
  $main.querySelectorAll('[data-m]').forEach(function (b) { b.onclick = function () { var m = D.mocks.filter(function (x) { return x.id === b.dataset.m; })[0], mins = parseInt(document.getElementById('mt' + m.id).value, 10); if (!(mins >= 1)) return toast('Enter a valid time'); startQuiz({ ids: m.ids, mode: 'timed', minutes: mins, title: m.title, mockId: m.id, keepOrder: true }); }; });
};

/* ---------- numerical practice ---------- */
R.numerical = function () {
  var p = qparam();
  render('<h1>Numerical practice</h1><p class="mut">Attempt first, then reveal the full solution. Constants such as emission factors are stated assumptions in each problem.</p><div class="row"><label for="nw" style="margin:0">Week</label><select id="nw" style="max-width:320px">' + weekOpts(p.week) + '</select></div><div id="nl"></div>');
  function draw() { var w = document.getElementById('nw').value, ns = D.numericals.filter(function (q) { return !w || q.week == w; });
    document.getElementById('nl').innerHTML = ns.length ? ns.map(function (q) { return '<div class="card" data-id="' + q.id + '"><span class="tag">Week ' + q.week + '</span><span class="tag">' + h(q.topic) + '</span><span class="tag">' + q.difficulty + '</span>' + srcTag(q) + '<p><b>Given:</b> ' + h(q.given) + '</p><p><b>Find:</b> ' + h(q.required) + ' in ' + h(q.unit) + '</p><div class="row"><input type="number" step="any" inputmode="decimal" aria-label="Your answer" style="max-width:200px"><button class="btn" data-chk>Check</button><button class="btn sec" data-show>Show solution</button></div><div class="out"></div></div>'; }).join('') : '<div class="card mut">No numerical problems for this selection.</div>';
    document.querySelectorAll('#nl .card[data-id]').forEach(function (c) { var q = QBY[c.dataset.id], out = c.querySelector('.out'), inp = c.querySelector('input');
      c.querySelector('[data-chk]').onclick = function () { var v = parseFloat(inp.value); if (isNaN(v)) return toast('Enter a number'); var ok = Math.abs(v - q.answer) <= q.tolerance + 1e-9; record(q, ok); out.innerHTML = '<div class="fb ' + (ok ? 'ok' : 'bad') + '">' + (ok ? 'Correct!' : 'Not correct. Try again or view the solution.') + '</div>'; };
      c.querySelector('[data-show]').onclick = function () { out.innerHTML = '<div class="card"><p><b>Formula:</b> <code>' + h(q.formula) + '</code></p><p><b>Substitution and calculation:</b></p><ol>' + q.steps.map(function (s) { return '<li>' + h(s) + '</li>'; }).join('') + '</ol><p><b>Final answer:</b> ' + q.answer + ' ' + h(q.unit) + '</p><p>' + h(q.explanation) + '</p></div>'; }; }); }
  document.getElementById('nw').onchange = draw; draw();
};

/* ---------- flashcards ---------- */
R.flashcards = function () {
  var p = qparam(), st = { cards: [], i: 0, show: false, onlyHard: false };
  var kinds = ['', 'qa', 'definition', 'formula', 'case', 'misconception', 'abbreviation'];
  render('<h1>Flashcards</h1><div class="card"><div class="formgrid"><div><label for="cw">Week</label><select id="cw"><option value="">All weeks</option>' + D.weeks.map(function (w) { return '<option value="' + w.id + '"' + (String(p.week) === String(w.id) ? ' selected' : '') + '>Week ' + w.id + '</option>'; }).join('') + '<option value="0">Abbreviations</option></select></div><div><label for="ck">Type</label><select id="ck">' + kinds.map(function (k) { return '<option value="' + k + '">' + (k || 'All types') + '</option>'; }).join('') + '</select></div><div><label for="ch">Show</label><select id="ch"><option value="">All cards</option><option value="1">Difficult only</option></select></div></div></div><div id="fc"></div>');
  function load() { var w = document.getElementById('cw').value, k = document.getElementById('ck').value, hd = document.getElementById('ch').value;
    st.cards = D.cards.filter(function (c) { return (w === '' || c.week == w) && (!k || c.kind === k) && (!hd || S.hardCards.indexOf(c.id) > -1); }); st.i = 0; st.show = false; draw(); }
  function draw() { var e = document.getElementById('fc'); if (!st.cards.length) { e.innerHTML = '<div class="card mut">No cards match. ' + (document.getElementById('ch').value ? 'Mark some cards as difficult first.' : '') + '</div>'; return; }
    var c = st.cards[st.i], hard = S.hardCards.indexOf(c.id) > -1;
    e.innerHTML = '<p class="mut">Card ' + (st.i + 1) + ' of ' + st.cards.length + ' · ' + c.kind + (c.week ? ' · Week ' + c.week : '') + '</p><div class="flash" id="fl" tabindex="0" role="button" aria-label="Reveal answer">' + (st.show ? '<div><small class="mut">Answer</small><br>' + h(c.back) + '</div>' : '<div>' + h(c.front) + '</div>') + '</div><div class="row"><button class="btn sec" id="p">Previous</button><button class="btn" id="r">' + (st.show ? 'Hide answer' : 'Reveal answer') + '</button><button class="btn sec" id="n">Next</button><button class="btn sec" id="s">Shuffle</button><button class="btn sec" id="d">' + (hard ? 'Unmark difficult' : 'Mark difficult') + '</button></div>';
    var go = function (d) { st.i = (st.i + d + st.cards.length) % st.cards.length; st.show = false; draw(); };
    document.getElementById('p').onclick = function () { go(-1); }; document.getElementById('n').onclick = function () { go(1); };
    document.getElementById('r').onclick = document.getElementById('fl').onclick = function () { st.show = !st.show; draw(); };
    document.getElementById('s').onclick = function () { st.cards = shuffle(st.cards); st.i = 0; st.show = false; draw(); };
    document.getElementById('d').onclick = function () { var q = S.hardCards.indexOf(c.id); if (q > -1) S.hardCards.splice(q, 1); else S.hardCards.push(c.id); save(); draw(); }; }
  ['cw', 'ck', 'ch'].forEach(function (i) { document.getElementById(i).onchange = load; }); load();
};

/* ---------- question bank, search, filters ---------- */
function bankFilterUI(f) {
  return '<div class="card"><div class="formgrid"><div><label for="bq">Keyword</label><input id="bq" type="search" value="' + h(f.q || '') + '"></div><div><label for="bw">Week</label><select id="bw">' + weekOpts(f.week) + '</select></div><div><label for="bf">Format</label><select id="bf"><option value="">Any</option><option value="mcq">MCQ</option><option value="multi">Multiple-select</option><option value="tf">True/False</option><option value="ar">Assertion-reason</option><option value="num">Numerical</option></select></div><div><label for="bd">Difficulty</label><select id="bd"><option value="">Any</option><option>easy</option><option>medium</option><option>hard</option></select></div><div><label for="bs">Source type</label><select id="bs"><option value="">Any</option><option value="pyq">Official final-exam PYQ</option><option value="assignment">Official assignment</option><option value="generated">Self-made practice (reviewed)</option></select></div><div><label for="by">Year</label><input id="by" type="text" placeholder="e.g. 2023" inputmode="numeric"></div></div></div>';
}
function matches(q, f) {
  var s = (f.q || '').toLowerCase();
  if (s) { var hay = (q.text + ' ' + q.topic + ' ' + q.explanation + ' ' + (q.options || []).join(' ') + ' ' + (q.formula || '') + ' week ' + q.week).toLowerCase(); if (!s.split(/\s+/).every(function (t) { return hay.indexOf(t) > -1; })) return false; }
  if (f.week && q.week != f.week) return false; if (f.format && q.format !== f.format) return false; if (f.diff && q.difficulty !== f.diff) return false;
  if (f.src) { var t = q.source.type === 'generated' ? 'generated' : q.source.type; if (t !== f.src) return false; }
  if (f.year && (q.years || []).indexOf(+f.year.trim()) < 0) return false; return true;
}
R.bank = function () {
  var p = qparam(); var f = { q: p.q || '', week: p.week || '', src: p.source || '' };
  render('<h1>Question bank</h1><p class="mut">' + ALLQ.length + ' questions: ' + ALLQ.filter(function (q) { return q.source.type === 'assignment'; }).length + ' <b>official NPTEL assignment questions (2021 and 2026 sessions)</b> and ' + ALLQ.filter(function (q) { return q.source.type === 'generated'; }).length + ' self-made practice questions (reviewed twice, not official). No final-exam PYQs are included (none were available). <a href="#/about">Sources</a></p>' + bankFilterUI(f) + '<div class="row"><button class="btn sec" id="exp">Export filtered as CSV</button></div><p id="cnt" class="mut"></p><div id="bl"></div>');
  function draw() {
    f = { q: document.getElementById('bq').value, week: document.getElementById('bw').value, format: document.getElementById('bf').value, diff: document.getElementById('bd').value, src: document.getElementById('bs').value, year: document.getElementById('by').value };
    var res = ALLQ.filter(function (q) { return matches(q, f); }); draw.res = res;
    document.getElementById('cnt').textContent = res.length + ' result(s)';
    document.getElementById('bl').innerHTML = res.slice(0, 60).map(function (q) { return qCard(q); }).join('') + (res.length > 60 ? '<p class="mut">Showing first 60. Refine filters to see more.</p>' : '') || '<div class="card mut">No matching questions.</div>';
    $main.querySelectorAll('[data-bm]').forEach(function (b) { b.onclick = function () { toggleBm(b.dataset.bm); draw(); }; });
    $main.querySelectorAll('[data-rev]').forEach(function (b) { b.onclick = function () { var d = b.nextElementSibling; d.hidden = !d.hidden; }; });
  }
  ['bq', 'bw', 'bf', 'bd', 'bs', 'by'].forEach(function (i) { var e = document.getElementById(i); e.oninput = draw; e.onchange = draw; }); document.getElementById('bw').value = f.week; if (f.src) document.getElementById('bs').value = f.src; draw();
  document.getElementById('exp').onclick = function () { exportQuestions(draw.res, 'question-bank.csv'); };
};
function ansText(q) { return q.format === 'num' ? q.answer + ' ' + q.unit : q.answer.map(function (a) { return q.options[a]; }).join('; '); }
function qCard(q) {
  return '<div class="card"><span class="tag">' + q.id + '</span><span class="tag">Week ' + q.week + '</span><span class="tag">' + h(q.topic) + '</span><span class="tag">' + q.format + '</span><span class="tag">' + q.difficulty + '</span>' + srcTag(q) + '<p><b>' + h(q.text) + '</b></p>' + (q.options ? '<ol type="A">' + q.options.map(function (o) { return '<li>' + h(o) + '</li>'; }).join('') + '</ol>' : '') + '<button class="btn sec" data-rev>Show answer</button><div hidden><p><b>Answer:</b> ' + h(ansText(q)) + '</p><p>' + h(q.explanation) + '</p>' + (q.steps ? numSteps(q) : '') + '</div> <button class="btn sec" data-bm="' + q.id + '">' + (S.bookmarks.indexOf(q.id) > -1 ? 'Remove bookmark' : 'Bookmark') + '</button></div>';
}
function exportQuestions(qs, name) {
  if (!qs.length) return toast('Nothing to export');
  var rows = [['id', 'week', 'topic', 'format', 'difficulty', 'question', 'options', 'correct_answer', 'explanation', 'source_type', 'verification', 'year', 'source_url']].concat(qs.map(function (q) { return [q.id, q.week, q.topic, q.format, q.difficulty, q.text, (q.options || []).join(' | '), ansText(q), q.explanation, q.source.type, q.source.verification, q.source.year || '', q.source.url || '']; }));
  download(name, rows.map(function (r) { return r.map(csvCell).join(','); }).join('\n'));
}

R.search = function (arg) {
  var qs = arg.toLowerCase().trim(); if (!qs) return render('<h1>Search</h1><p>Type something in the search box.</p>');
  var terms = qs.split(/\s+/), has = function (s) { s = s.toLowerCase(); return terms.every(function (t) { return s.indexOf(t) > -1; }); };
  var qres = ALLQ.filter(function (q) { return matches(q, { q: qs }); });
  var wres = D.weeks.filter(function (w) { return has(w.title + ' ' + w.overview + ' ' + w.concepts.join(' ') + ' ' + w.revision.join(' ') + ' ' + w.notes.map(function (n) { return n.h + ' ' + n.p.join(' '); }).join(' ')); });
  var fres = []; D.weeks.forEach(function (w) { w.formulas.forEach(function (f) { if (has(f.name + ' ' + f.formula)) fres.push([w.id, f]); }); w.definitions.forEach(function (d) { if (has(d.term + ' ' + d.def_)) fres.push([w.id, { name: d.term, formula: d.def_, unit: 'definition' }]); }); });
  render('<h1>Search: "' + h(arg) + '"</h1><h2>Study notes (' + wres.length + ')</h2>' + (wres.map(function (w) { return '<div class="card"><a href="#/week/' + w.id + '">Week ' + w.id + ': ' + h(w.title) + '</a></div>'; }).join('') || '<p class="mut">None</p>') +
    '<h2>Formulas &amp; definitions (' + fres.length + ')</h2>' + (fres.slice(0, 25).map(function (x) { return '<div class="card"><b>' + h(x[1].name) + '</b> <span class="tag">Week ' + x[0] + '</span><div>' + h(x[1].formula) + '</div></div>'; }).join('') || '<p class="mut">None</p>') +
    '<h2>Questions (' + qres.length + ')</h2><div id="sq">' + (qres.slice(0, 30).map(qCard).join('') || '<p class="mut">None</p>') + '</div>');
  $main.querySelectorAll('[data-bm]').forEach(function (b) { b.onclick = function () { toggleBm(b.dataset.bm); b.textContent = S.bookmarks.indexOf(b.dataset.bm) > -1 ? 'Remove bookmark' : 'Bookmark'; }; });
  $main.querySelectorAll('[data-rev]').forEach(function (b) { b.onclick = function () { var d = b.nextElementSibling; d.hidden = !d.hidden; }; });
};

/* ---------- bookmarks and mistakes ---------- */
R.review = function () {
  var p = qparam(); var wk = p.week || '', tp = p.topic || '';
  var wrong = latestWrong().map(function (i) { return QBY[i]; }).filter(function (q) { return (!wk || q.week == wk) && (!tp || q.topic === tp); });
  var bms = S.bookmarks.map(function (i) { return QBY[i]; }).filter(Boolean);
  render('<h1>Bookmarks &amp; mistakes</h1><div class="card"><div class="formgrid"><div><label for="rw">Filter mistakes by week</label><select id="rw">' + weekOpts(wk) + '</select></div><div><label for="rt">Topic</label><select id="rt"><option value="">All topics</option>' + topicsFor(wk).map(function (t) { return '<option' + (t === tp ? ' selected' : '') + '>' + h(t) + '</option>'; }).join('') + '</select></div></div></div>' +
    '<h2>Mistakes (' + wrong.length + ')</h2><p class="mut">Questions whose most recent attempt was incorrect.</p><div class="row"><button class="btn" id="rm"' + (wrong.length ? '' : ' disabled') + '>Retry these mistakes</button><button class="btn sec" id="em">Export mistakes CSV</button></div>' + (wrong.map(qCard).join('') || '<div class="card mut">No mistakes recorded for this filter.</div>') +
    '<h2>Bookmarks (' + bms.length + ')</h2><div class="row"><button class="btn" id="rb"' + (bms.length ? '' : ' disabled') + '>Practice bookmarks</button><button class="btn sec" id="eb">Export bookmarks CSV</button></div>' + (bms.map(qCard).join('') || '<div class="card mut">No bookmarks yet. Use the Bookmark button on any question.</div>'));
  var nav = function () { location.hash = '#/review?week=' + document.getElementById('rw').value + '&topic=' + encodeURIComponent(document.getElementById('rt').value); };
  document.getElementById('rw').onchange = function () { location.hash = '#/review?week=' + this.value; }; document.getElementById('rt').onchange = nav;
  document.getElementById('rm').onclick = function () { startQuiz({ ids: wrong.map(function (q) { return q.id; }), mode: 'practice', title: 'Retry mistakes' }); };
  document.getElementById('rb').onclick = function () { startQuiz({ ids: bms.map(function (q) { return q.id; }), mode: 'practice', title: 'Bookmarked questions' }); };
  document.getElementById('em').onclick = function () { exportQuestions(wrong, 'incorrect-questions.csv'); };
  document.getElementById('eb').onclick = function () { exportQuestions(bms, 'bookmarked-questions.csv'); };
  $main.querySelectorAll('[data-bm]').forEach(function (b) { b.onclick = function () { toggleBm(b.dataset.bm); R.review(); }; });
  $main.querySelectorAll('[data-rev]').forEach(function (b) { b.onclick = function () { var d = b.nextElementSibling; d.hidden = !d.hidden; }; });
};

/* ---------- formula handbook ---------- */
R.formulas = function () {
  render('<h1>Formula handbook</h1><div class="row noprint"><button class="btn sec" onclick="window.print()">Print / save as PDF</button><button class="btn sec" id="fcsv">Download CSV</button></div>' + D.weeks.map(function (w) { return '<div class="card"><h2>Week ' + w.id + ': ' + h(w.title) + '</h2><div class="tbl"><table><tr><th>Name</th><th>Formula</th><th>Unit</th></tr>' + w.formulas.map(function (f) { return '<tr><td>' + h(f.name) + '</td><td><code>' + h(f.formula) + '</code></td><td>' + h(f.unit) + '</td></tr>'; }).join('') + '</table></div></div>'; }).join(''));
  document.getElementById('fcsv').onclick = function () { var rows = [['week', 'name', 'formula', 'unit']]; D.weeks.forEach(function (w) { w.formulas.forEach(function (f) { rows.push([w.id, f.name, f.formula, f.unit]); }); }); download('formula-handbook.csv', rows.map(function (r) { return r.map(csvCell).join(','); }).join('\n')); };
};

/* ---------- progress + export ---------- */
R.progress = function () {
  var wp = weekPerf(), tp = topicPerf().sort(function (a, b) { return a.acc - b.acc; });
  render('<h1>Progress &amp; export</h1><div class="card"><div class="stat">' + stats().n + '</div>answers recorded · ' + stats().c + ' correct · ' + (stats().n - stats().c) + ' incorrect</div>' +
    '<h2>Accuracy by week</h2><div class="card tbl"><table><tr><th>Week</th><th>Attempts</th><th>Accuracy</th></tr>' + wp.map(function (x) { return '<tr><td><a href="#/week/' + x.week + '">Week ' + x.week + '</a></td><td>' + x.n + '</td><td>' + (x.n ? x.acc + '%' : '-') + '</td></tr>'; }).join('') + '</table></div>' +
    '<h2>Accuracy by topic</h2><div class="card tbl"><table><tr><th>Topic</th><th>Attempts</th><th>Accuracy</th></tr>' + (tp.map(function (x) { return '<tr><td>' + h(x.topic) + '</td><td>' + x.n + '</td><td>' + x.acc + '%</td></tr>'; }).join('') || '<tr><td colspan="3" class="mut">No data yet</td></tr>') + '</table></div>' +
    '<h2>Mock results</h2><div class="card tbl"><table><tr><th>When</th><th>Mock</th><th>Score</th></tr>' + (S.quizzes.filter(function (z) { return z.mock; }).map(function (z) { return '<tr><td>' + new Date(z.t).toLocaleString() + '</td><td>' + h(z.title) + '</td><td>' + z.score + '/' + z.total + '</td></tr>'; }).join('') || '<tr><td colspan="3" class="mut">None yet</td></tr>') + '</table></div>' +
    '<h2>Export &amp; backup</h2><div class="card"><div class="row"><button class="btn sec" id="e1">Question bank CSV</button><button class="btn sec" id="e2">Quiz history CSV</button><button class="btn sec" id="e3">Backup progress (JSON)</button><label class="btn sec" style="margin:4px 0">Restore backup<input id="e4" type="file" accept="application/json" hidden></label><button class="btn warn" id="e5">Reset all progress</button></div><p class="mut">' + (storageOK ? 'Progress is stored only in this browser on this device (localStorage). It does NOT sync across devices; clearing site data erases it. Use the JSON backup to move progress manually.' : 'Browser storage is unavailable here, so progress is not being saved.') + '</p></div>');
  document.getElementById('e1').onclick = function () { exportQuestions(ALLQ, 'question-bank.csv'); };
  document.getElementById('e2').onclick = function () { var rows = [['time', 'quiz', 'mode', 'score', 'total', 'percent']].concat(S.quizzes.map(function (z) { return [new Date(z.t).toISOString(), z.title, z.mode, z.score, z.total, pct(z.score, z.total)]; })); if (rows.length < 2) return toast('No quiz history yet'); download('quiz-history.csv', rows.map(function (r) { return r.map(csvCell).join(','); }).join('\n')); };
  document.getElementById('e3').onclick = function () { download('sts-progress-backup.json', JSON.stringify(S), 'application/json'); };
  document.getElementById('e4').onchange = function (e) { var f = e.target.files[0]; if (!f) return; var r = new FileReader(); r.onload = function () { try { var o = JSON.parse(r.result); if (!o || !Array.isArray(o.attempts)) throw 0; S = Object.assign(blank(), o); save(); toast('Progress restored'); R.progress(); } catch (x) { toast('Invalid backup file'); } }; r.readAsText(f); };
  document.getElementById('e5').onclick = function () { if (confirm('Erase all progress stored in this browser?')) { S = blank(); save(); toast('Progress reset'); R.progress(); } };
};


/* ---------- official assignments by year ---------- */
var YEARS = [2021, 2022, 2023, 2024, 2025, 2026];
R.official = function (arg) {
  var yr = parseInt(arg, 10); if (YEARS.indexOf(yr) < 0) yr = 2021;
  var all = ALLQ.filter(function (q) { return q.source.type === 'assignment'; });
  var tabs = YEARS.map(function (y) { var n = all.filter(function (q) { return q.years.indexOf(y) > -1; }).length; return '<a class="btn' + (y === yr ? '' : ' sec') + '" href="#/official/' + y + '">' + y + ' (' + n + ')</a>'; }).join('');
  var qs = all.filter(function (q) { return q.years.indexOf(yr) > -1; });
  var html = '<h1>Official weekly assignments</h1><p class="mut">Questions from NPTEL\'s own weekly assignments for this course, grouped by year. Only 2021 and 2026 have been added so far; 2022-2025 can be added later (see README). Questions that appeared in more than one year are listed under each year.</p><div class="row">' + tabs + '</div>';
  if (!qs.length) html += '<div class="card"><b>' + yr + ': not added yet.</b><p class="mut">No questions for this year have been supplied. When you have the ' + yr + ' assignment PDFs or screenshots, they can be added with their year and answer key.</p></div>';
  else {
    html += '<div class="row"><button class="btn" id="oy">Practice all ' + yr + ' (' + qs.length + ')</button><button class="btn sec" id="oc">Export ' + yr + ' as CSV</button></div>';
    for (var w = 1; w <= 12; w++) {
      var wq = qs.filter(function (q) { return q.week === w; });
      if (!wq.length) continue;
      html += '<details class="card"><summary><b>Week ' + w + ' - ' + h(D.weeks[w - 1].title) + '</b> <span class="tag">' + wq.length + ' questions</span></summary><div class="row"><button class="btn" data-pw="' + w + '">Practice Week ' + w + ' (' + yr + ')</button></div>' + wq.map(qCard).join('') + '</details>';
    }
  }
  render(html);
  var oy = document.getElementById('oy'); if (oy) oy.onclick = function () { startQuiz({ ids: qs.map(function (q) { return q.id; }), mode: 'practice', title: 'Official ' + yr + ' assignments' }); };
  var oc = document.getElementById('oc'); if (oc) oc.onclick = function () { exportQuestions(qs, 'official-' + yr + '.csv'); };
  $main.querySelectorAll('[data-pw]').forEach(function (b) { b.onclick = function () { var w = +b.dataset.pw; startQuiz({ ids: qs.filter(function (q) { return q.week === w; }).map(function (q) { return q.id; }), mode: 'practice', title: 'Official ' + yr + ' - Week ' + w }); }; });
  $main.querySelectorAll('[data-bm]').forEach(function (b) { b.onclick = function () { toggleBm(b.dataset.bm); b.textContent = S.bookmarks.indexOf(b.dataset.bm) > -1 ? 'Remove bookmark' : 'Bookmark'; }; });
  $main.querySelectorAll('[data-rev]').forEach(function (b) { b.onclick = function () { var d = b.nextElementSibling; d.hidden = !d.hidden; }; });
};

/* ---------- about ---------- */
R.about = function () {
  var c = D.course;
  render('<h1>Sources &amp; about</h1><div class="card"><h2>Course</h2><p>' + h(c.name) + ' (' + h(c.code) + '), ' + h(c.institute) + ', ' + h(c.instructor) + '.<br><a href="' + c.url + '" target="_blank" rel="noopener">Official course page</a> · <a href="' + c.syllabus_pdf + '" target="_blank" rel="noopener">Official syllabus PDF</a> (week titles in this app are taken from this PDF).</p></div>' +
    '<div class="card"><h2>Question provenance</h2><table><tr><th>Category</th><th>Count</th></tr><tr><td>A. Official assignment questions (2021 session from portal screenshots; 2026 session from the assignment PDFs)</td><td>' + ALLQ.filter(function (q) { return q.source.type === 'assignment'; }).length + '</td></tr><tr><td>B. Verified official final-exam PYQs</td><td>0</td></tr><tr><td>C. Adapted lecture-based questions</td><td>0</td></tr><tr><td>D. Self-made practice questions (reviewed, not official)</td><td>' + ALLQ.filter(function (q) { return q.source.type === 'generated'; }).length + '</td></tr></table><p>Official assignment questions are from the Jul-Oct 2021 session (Assignments 0-12) with the accepted answers shown on the NPTEL portal, copied by hand from screenshots; a few keys look questionable and are flagged in their explanations. No final-exam papers or other sessions\' assignments were available, so there are no PYQs and nothing is labelled as one. Self-made questions are never labelled official.</p></div>' +
    '<div class="card"><h2>Limitations</h2><ul><li>Unofficial; not affiliated with NPTEL or IIT Roorkee.</li><li>Notes are original summaries from the official syllabus and standard references, not lecture transcripts. Verify details against the lectures.</li><li>Mock tests are unofficial and do not predict the real exam.</li><li>Progress is local to one browser; there is no account system or cross-device sync in this build.</li><li>Offline reading works after the first online load only if your browser supports service workers on your hosting origin.</li></ul></div>');
};
R.notfound = function () { render('<h1>Page not found</h1><p><a href="#/">Go to dashboard</a></p>'); };

/* ---------- wiring ---------- */
document.getElementById('menuBtn').onclick = function () { var n = document.getElementById('nav'); var o = n.classList.toggle('open'); this.setAttribute('aria-expanded', o); };
document.getElementById('gsearch').onsubmit = function (e) { e.preventDefault(); var v = document.getElementById('gq').value.trim(); if (v) location.hash = '#/search/' + encodeURIComponent(v); else toast('Type something to search'); };
window.addEventListener('hashchange', function () { var n = location.hash.replace(/^#\/?/, '').split(/[\/?]/)[0]; if (n === 'run' && !Z) { location.hash = '#/quiz'; return; } route(); });
if ('serviceWorker' in navigator && location.protocol.indexOf('http') === 0) navigator.serviceWorker.register('sw.js').catch(function () {});
window.__sts = { D: D, S: function () { return S; }, startQuiz: startQuiz, Z: function () { return Z; } };
route();
})();
