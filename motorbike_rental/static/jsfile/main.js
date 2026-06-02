const HireBike = document.getElementById("btnHireBike");
const navLinks = document.getElementById("navLinks");

const modal = document.getElementById("deleteModal");
const deleteForm = document.getElementById("deleteForm");
const modalText = document.getElementById("modalText");

 //const oSection  = document.getElementById("Bike_Details_Section");
 // const oSection  = document.getElementById("Bike_Details_Section");

const AddEditBikeModal = document.getElementById("AddEditBikeModal");


//alert("XXXXXXXXX");

/* Mobile Menu */
function toggleMenu() {
  navLinks.classList.toggle("active");
  //alert("submenu clicked! VVVVV");
}

/* Submenu */
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

function EditMotorbike(id, make, model, plate, year, imgsrc, status, rate) {
  //document.getElementById("edit-add-ModalTitle").innerHTML =
  // "✏️ Edit Motorbike";
 // alert("" + AddEditBikeForm);
 // AddEditBikeModal.style.display = "flex";

  //frmmotorbike[]["bike_make"].value = make;
  //AddEditBikeForm["bike_model"].value = model;
 // AddEditBikeForm["bike_plate_number"].value = plate;
 // AddEditBikeForm["bike_year"].value = year;
 // AddEditBikeForm["bike_imgsrc"].value = imgsrc;
 // AddEditBikeForm["bike_status"].value = status;
 // AddEditBikeForm["bike_daily_rate"].value = rate;

  //AddEditBikeForm.action = `/motorbikes/edit/${id}/`;

  
   document.getElementById("Bike_Details_Section").style.display = 'block';
  
  document.getElementById("bike_info_title").innerHTML =
   "✏️ Edit Motorbike";
  var form = document.getElementById("frmMotorbike").elements;


for(var i = 0; i < form.length; i++){
	if(form[i].type == 'text'){
	
    if (form[i].id == 'bike_brand')
     {
       	form[i].value = make;
     }

    if (form[i].id == 'bike_model')
     {
       	form[i].value = model;
     }

    if (form[i].id == 'bike_year')
     {
       	form[i].value = year;
     }

    if (form[i].id == 'bike_status')
     {
       	form[i].value = status;
     }

    if (form[i].id == 'bike_plate_number')
     {
       	form[i].value = plate;
     }

    if (form[i].id == 'bike_img_url')
     {
       	form[i].value = imgsrc;
     }

    if (form[i].id == 'bike_rate')
     {
       	form[i].value = rate;
     }

  }
     
}
 
  
}
