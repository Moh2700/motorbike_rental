const form = document.getElementById("bikeForm");

form.addEventListener("submit", function (e) {
  const year = document.getElementById("id_year").value;
  const rate = document.getElementById("id_daily_rate").value;

  if (year < 2000) {
    alert("Motorbike year must be 2000 or newer");
    e.preventDefault();
  }

  if (rate <= 0) {
    alert("Daily rate must be greater than 0");
    e.preventDefault();
  }
});
