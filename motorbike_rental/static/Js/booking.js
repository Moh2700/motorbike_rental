const startInput = document.getElementById("id_start_time");
const endInput = document.getElementById("id_end_time");
const bikeSelect = document.getElementById("id_motorbike");
const priceDisplay = document.getElementById("price");

// Example price map (you will improve this later)
const bikePrices = {
  1: 20,
  2: 25,
  3: 30,
};

function calculatePrice() {
  const start = new Date(startInput.value);
  const end = new Date(endInput.value);
  const bikeId = bikeSelect.value;

  if (!start || !end || !bikeId) return;

  const hours = (end - start) / (1000 * 60 * 60);
  const rate = bikePrices[bikeId] || 0;

  const total = Math.max(0, hours * rate);

  priceDisplay.innerText = "£" + total.toFixed(2);
}

startInput.addEventListener("change", calculatePrice);
endInput.addEventListener("change", calculatePrice);
bikeSelect.addEventListener("change", calculatePrice);
