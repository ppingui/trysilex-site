// PGSI self-check, shared by every translated page. The page supplies its
// strings as window.SELFCHECK before loading this file:
//   { items: [9 questions], scale: [[label, 0..3] x4],
//     bands: [{max, label, line} x4], next: {bandLabel: html},
//     progress: "{n} of 9 answered.", done: "..." }
// Scoring is the standard PGSI: 0 / 1-2 / 3-7 / 8+, identical to the app's
// PGSIBand and to the English page. Nothing is stored or sent.
(function () {
  var S = window.SELFCHECK;
  var form = document.getElementById("pgsi");
  var host = document.getElementById("pgsi-questions");
  if (!S || !form || !host) return;

  S.items.forEach(function (text, i) {
    var fs = document.createElement("fieldset");
    var legend = document.createElement("legend");
    legend.textContent = (i + 1) + ". " + text;
    fs.appendChild(legend);
    var opts = document.createElement("div");
    opts.className = "opts";
    S.scale.forEach(function (pair) {
      var label = document.createElement("label");
      var input = document.createElement("input");
      input.type = "radio";
      input.name = "q" + i;
      input.value = String(pair[1]);
      var span = document.createElement("span");
      span.textContent = pair[0];
      label.appendChild(input);
      label.appendChild(span);
      opts.appendChild(label);
    });
    fs.appendChild(opts);
    host.appendChild(fs);
  });

  var result = document.getElementById("pgsi-result");
  var progress = document.getElementById("pgsi-progress");

  form.addEventListener("change", function () {
    var total = 0, answered = 0;
    for (var i = 0; i < S.items.length; i++) {
      var picked = form.querySelector('input[name="q' + i + '"]:checked');
      if (picked) { answered++; total += parseInt(picked.value, 10); }
    }
    if (answered < S.items.length) {
      progress.textContent = S.progress.replace("{n}", answered);
      result.hidden = true;
      return;
    }
    var band = S.bands.find(function (b) { return total <= b.max; });
    document.getElementById("pgsi-score").textContent = total + " / 27";
    document.getElementById("pgsi-band").textContent = band.label;
    document.getElementById("pgsi-line").textContent = band.line;
    document.getElementById("pgsi-next").innerHTML = S.next[band.label];
    progress.textContent = S.done;
    result.hidden = false;
  });
})();
