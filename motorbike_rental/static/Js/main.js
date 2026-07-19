/*
alert("");

const HireBike = document.getElementById("btnHireBike");
const navLinks = document.getElementById("navLinks");


function toggleMenu() {
  navLinks.classList.toggle("active");
  alert("submenu clicked! VVVVV");
}


function toggleSubmenu(event) {
  event.preventDefault();
  const dropdown = event.target.parentElement;

  switch (dropdown.id) {
    case "mnuAccessories":
      toggle_visibility("submnuAccessories");
      break;

    case "mnuMotorbikes":
      toggle_visibility("submnuMotorbikes");
      break;
  }
}

function togglePopup() {
  const overlay = document.getElementById("popupOverlay");

  overlay.classList.toggle("show");

  overlay.style.zIndex = 10;
  // showbikedetails(document.getElementById('motorbike-title'), this.parentElement.querySelector('img'));
}

let elements = document.querySelectorAll("img");
// let container = document.getElementById("bike-details");
elements.forEach((element) => {
  element.addEventListener("click", function () {
    //  removeContainerChildren(container)
    // showbikedetails(container, element)
  });
});

function toggle_visibility(id) {
  var e = document.getElementById(id);
  if (e.style.display == "block") e.style.display = "none";
  else e.style.display = "block";
}

function populateHiringForm(bikeid, container, bikeElement) {
  let data = bikeElement.dataset;

  document.getElementById("BikeHiring").style.display = "block";
  document.getElementById("motorbike-title").innerHTML =
    data.bikemake + " " + data.bikemodel + " " + data.bikeyear;

  togglePopup();
}

function showbikedetails(container, bikeElement) {
  let data = bikeElement.dataset;

  let nameElement = document.createElement("h1");
  let nameText = document.createTextNode(data.bikemake);
  nameElement.appendChild(nameText);
  container.innerHTML = "";
  container.append(nameElement);
}

function removeContainerChildren(container) {
  while (container.firstChild) {
    container.removeChild(container.firstChild);
  }
}

function makeaselection(option) {
  //alert("You have selected " + option);
  switch (option) {
    case "bikelisting":
      //alert("You have selected " + option);
      //document.getElementById("BikePickup").style.display = "block";
      document.getElementById("Bike_Details_Section").style.display = "block";
      document.getElementById("BikeSection").style.display = "block";
      break;

    case "driverlisting":
      break;
  }
}

HireBike.addEventListener("click", function () {
  makeaselection("bikelisting");
});

*/
