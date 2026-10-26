// Gambling loss calculator, shared by every translated page. The page supplies
// window.LOSSCALC = { locale: "es-ES" } and a <select id="currency"> whose
// option values are ISO 4217 codes. Same maths as the app's LossMath and the
// English page: weekly * 52, and the "instead" column compounds monthly
// contributions at 8%/yr — an illustration, never advice.
(function () {
  var C = window.LOSSCALC || { locale: "en-US" };
  var amount = document.getElementById("amount");
  var currency = document.getElementById("currency");
  if (!amount || !currency) return;

  function money(code, n) {
    try {
      return new Intl.NumberFormat(C.locale, {
        style: "currency", currency: code, maximumFractionDigits: 0
      }).format(Math.round(n));
    } catch (e) {
      return code + " " + Math.round(n).toLocaleString(C.locale);
    }
  }

  function invested(weekly, years) {
    var monthly = weekly * 52 / 12;
    var r = 0.08 / 12;
    var n = years * 12;
    return monthly * ((Math.pow(1 + r, n) - 1) / r);
  }

  function update() {
    var weekly = parseFloat(amount.value);
    if (!isFinite(weekly) || weekly < 0) weekly = 0;
    var code = currency.value;
    document.getElementById("year").textContent = money(code, weekly * 52);
    [1, 5, 10, 20].forEach(function (y) {
      document.getElementById("l" + y).textContent = money(code, weekly * 52 * y);
      document.getElementById("i" + y).textContent = money(code, invested(weekly, y));
    });
  }

  amount.addEventListener("input", update);
  currency.addEventListener("change", update);
  update();
})();
