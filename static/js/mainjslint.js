/**
 * UK Vehicle Registration Validation Module
 */

// Banned positional characters based on DVLA rules
const RESTRICTED_AREA_LETTERS = /[IQZ]/;
const RESTRICTED_SUFFIX_LETTERS = /[IQ]/;

// Core profanity/offensive substrings explicitly banned by DVLA acr
const BANNED_OFFENSIVE_PHRASES = [
  "ARS",
  "ASS",
  "BOM",
  "BNP",
  "CNT",
  "CUM",
  "DCK",
  "FAG",
  "FCK",
  "FUK",
  "GAY",
  "HEL",
  "JAD",
  "KLL",
  "NAZ",
  "NGR",
  "NOB",
  "PAK",
  "PED",
  "SHG",
  "SHT",
  "SEX",
  "VAG",
  "WNK",
];

const modal = document.getElementById("deleteModal");
const deleteForm = document.getElementById("deleteForm");
const modalText = document.getElementById("modalText");
const navLinks = document.getElementById("mnuMotorbikes");

const inputStatus = document.getElementById("searchStatus");
const statusSelect = document.getElementById("bike_status");
const bikeCards = document.querySelectorAll(".bikecard");

const showAvailableMotorbikes = document.getElementById("btnAvailMotorbikes");
const signin = document.getElementById("hyplinkSignin");
const registration = document.getElementById("mnuRegistration");
const browsemotorbikes = document.getElementById("submnubikelisting");
const motorbikeStatus = document.getElementById("submnuMotorbikeStatus");

const browsemembers = document.getElementById("submnuMembersListing");
const showmembers = document.getElementById("btnshowMembers");

//const hiremotorbike = document.getElementById("btnHire");
const frmUser = document.getElementById("frmUserRegistration");
//const frmBike = document.getElementById("frmUserRegistration");

const usrpass = document.getElementById("userpassword");
const usrpass2 = document.getElementById("userpassword2");

const btnRate = document.getElementById("btnCalculateRate");
const startDate = document.getElementById("pickup_date");
const endDate = document.getElementById("return_date");
const rate = document.getElementById("bike_daily_rate");

let openHam = document.querySelector("#openHam");
let closeHam = document.querySelector("#closeHam");
let navigationItems = document.querySelector("#navigation-items");

//let registration = new usrRegistration();

//class usrRegistration {

function validateName(usrname) {
  const trimmed = usrname.trim();

  if (!trimmed) {
    return { message: "Name is required.", valid: false };
  }

  if (trimmed.length < 2 || trimmed.length > 50) {
    return { message: "Name must be 2-50 characters long.", valid: false };
  }

  let nameRegex = /^[a-zA-Z\s']+$/;

  if (!nameRegex.test(trimmed)) {
    return { message: "Name can only contain letters,", valid: false };
  }

  return { message: "Valid name", valid: false };
}

function validateforminput(frm) {
  for (let i = 0; i < frm.length; i++) {
    if (
      frm[i].type === "text" ||
      frm[i].type === "password" ||
      frm[i].type === "email" ||
      frm[i].type === "date"
    ) {
      if (frm[i].value === "") {
        highlightInput(frm[i]);
      }
    }
  }
}

function highlightInput(elem) {
  elem.style.borderWidth = "2px";
  elem.style.borderColor = "#ff3c00";
}

function validateEmail(value) {
  let input = document.createElement("input");

  input.type = "email";
  input.required = true;
  input.value = value;

  if (typeof input.checkValidity === "function") {
    return input.checkValidity();
  }

  return /\S+@\S+\.\S+/.test(value);
}

/*
    function validateEmail(value) {
        let input = document.createElement("input");

        input.type = "email";
        input.required = true;
        input.value = value;

        return typeof input.checkValidity === "function"
            ? input.checkValidity()
            : /\S+@\S+\.\S+/.test(value);
    }
*/
function is18OrOlder(dob) {
  let birth = new Date(dob);
  let limit = new Date();

  limit.setFullYear(limit.getFullYear() - 18);

  return birth <= limit;
}

function confirmpassword(pass1, pass2) {
  return pass1 === pass2;
}

function isValidPhoneNumber(phone) {
  phone = phone.replace(/[\s\-()]/g, "");

  return /^\+?[0-9]{10,15}$/.test(phone);
}
//}

/*
const hamburgerEvent = (navigation, close, open) => {
  navigationItems.style.display = navigation;
  navigationItems.style.width = "86%";
  navigationItems.style.gap = "2px";
  navigationItems.style.marginRight = "20px";
  closeHam.style.display = close;
  openHam.style.display = open;
};
*/

function hamburgerEvent(navigation, close, open) {
  navigationItems.style.display = navigation;
  navigationItems.style.width = "86%";
  navigationItems.style.gap = "2px";
  navigationItems.style.marginRight = "20px";
  closeHam.style.display = close;
  openHam.style.display = open;
}

openHam.addEventListener("click", function () {
  hamburgerEvent("flex", "block", "none");
});

closeHam.addEventListener("click", function () {
  hamburgerEvent("none", "none", "block");
});

function showError(message) {
  let statement = message.replace(/<br>/g, "\n");
  let errorText = document.querySelector("#errorModal p");
  let errorModal = document.getElementById("errorModal");

  errorText.innerText = statement;
  errorText.style.float = "left";
  errorModal.style.display = "flex";
}

function closeError() {
  document.getElementById("errorModal").style.display = "none";
}

function checkRegistration() {
  //const max = new UserRegistration("frmUserRegistration");
  const usrReg = new usrRegistration();
  let Proceed = true;
  let reginfo = "";

  const dob = document.getElementById("date_of_birth").value;
  if (!usrReg.is18OrOlder(dob)) {
    // document.getElementById("user_reg_info").innerText =
    //   "🏍 Create Account --- " + "You must be 18 or over to register";
    reginfo = reginfo + "- You must be 18 or over to register<br>";
    usrReg.highlightInput(document.getElementById("date_of_birth"));
    Proceed = false;
  }

  usrReg.validateforminput(frmUser);

  if (!usrReg.validateEmail(document.getElementById("useremail").value)) {
    // document.getElementById("useremail").value = "Not valid email";
    reginfo = reginfo + "- Not valid email <br>";
    usrReg.highlightInput(document.getElementById("useremail"));
    Proceed = false;
  }

  //check first name
  let name = document.getElementById("first_name");
  let strfname = name.value;
  let result = usrReg.validateName(strfname);

  if (!result.valid) {
    // document.getElementById("user_reg_info").innerText =
    //  "🏍 Create Account --- " + result.message;
    reginfo = reginfo + "- Not valid first name <br>";
    usrReg.highlightInput(document.getElementById("first_name"));
    Proceed = false;
  }

  name = document.getElementById("last_name");
  strfname = name.value;
  result = usrReg.validateName(strfname);

  if (!result.valid) {
    //document.getElementById("user_reg_info").innerText =
    //"🏍 Create Account --- " + result.message;
    reginfo = reginfo + "- Not valid last name <br>";
    usrReg.highlightInput(document.getElementById("last_name"));
    Proceed = false;
  }

  if (!usrReg.confirmpassword(usrpass.value, usrpass2.value)) {
    reginfo = reginfo + "- Not valid password <br>";
    usrReg.highlightInput(usrpass2);
    Proceed = false;
  }

  const phone = document.getElementById("phone_number");
  if (!usrReg.isValidPhoneNumber(phone.value)) {
    reginfo = reginfo + "- Not valid phone <br>";
    usrReg.highlightInput(phone);
    Proceed = false;
  }

  if (Proceed == true) {
    //alert("Go ahead submit the form");
    frmUser.method = "POST";
    //form.action = `/motorbikes/edit/${id}/`;

    frmUser.submit();
  } else {
    showError(reginfo);

    frmUser.preventDefault();
  }
  // return { Proceed: true, message: "Validation OK." };
}

function revealPassword(inputtype) {
  let x = inputtype;
  if (x.type === "password") {
    x.type = "text";
  } else {
    x.type = "password";
  }
}

/* Mobile Menu */
function toggleMenu() {
  navLinks.classList.toggle("active");
}

function toggleSubmenu(event) {
  event.preventDefault();
  const dropdown = event.target.parentElement;
  //dropdown.classList.toggle("active");

  switch (dropdown.id) {
    case "mnuAccessories":
      toggle_visibility("submnuAccessories");
      break;

    case "mnuMotorbikes":
      toggle_visibility("submnuMotorbikes");
      //alert("");
      break;

    case "mnuBookings":
      toggle_visibility("submnuBookings");
      break;

    case "mnuUsers":
      toggle_visibility("submnuUsers");
      break;
  }
}

function showLoginPopup(sectionname) {
  showprogSection(sectionname);
  togglePopup();
}

function togglePopup() {
  const overlay = document.getElementById("popupOverlay");
  overlay.classList.toggle("show");
  overlay.style.zIndex = 10;
}

function toggleUserMenu(menu, bltoggle) {
  const bikeuserRole = document.getElementById("userRole").value;

  if (bltoggle == true) {
    if (bikeuserRole.toUpperCase() == "customer".toUpperCase()) {
      alert("Administrator access required.");
      menu.classList.add("disabled");
    }
  } else {
    menu.classList.remove("disabled");
  }
}

function toggle_visibility(id) {
  let e = document.getElementById(id);
  if (e.style.display == "block") {
    e.style.display = "none";
  } else {
    e.style.display = "block";
  }
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
  container.bike_make.value = data.bikemake;
  container.bike_model.value = data.bikemodel;
  container.bike_plate_number.value = data.bikeplatenumber;
  container.bike_year.value = data.bikeyear;
  container.bike_status.value = data.bikestatus;
  container.bike_daily_rate.value = data.bikedailyrate;

  container.bike_id.value = data.bikeid;

  let image = document.createElement("img");
  let imageParent = document.getElementById("divimg");
  image.id = "Id";
  image.className = "class";
  image.src = data.bikeimgsrc;
  imageParent.innerHTML = "";
  imageParent.appendChild(image);

  const frm = document.getElementById("frmMotorbikeHire");
  frm.bike_id.value = data.bikeid;

  getUserCredentials();
  showprogSection("Motorbike_Hiring");
}

function showuserdetails(container, userElement) {
  //alert("You have selected to view user details for xxxxx ");

  let data = userElement.dataset;

  //container["last_name"].value = data.userlastname;
  container.last_name.value = data.userlastname;
  container.first_name.value = data.userfirstname;
  container.email.value = data.useremail;
  container.phone_number.value = data.userphone;
  container.username.value = data.username;
  container.password.value = data.userpassword;
  container.password2.value = data.userpassword2;
  container.user_id.value = data.userid;
  container.driving_licence_number.value = data.userdrivinglicence;
  container.date_of_birth.value = data.userdateofbirth;
  container.role.value = data.userrole;
  // anotherf code here for role
  container.address.value = data.useraddress;

  // Scroll to the form
  //const form = document.getElementById("HireMotorbikeForm");

  container.scrollIntoView({
    behavior: "smooth",
    block: "start",
  });

  container.first_name.focus();
}

function DeleteUser(container, userid) {
  modal.style.display = "flex";
  let user = container.first_name.value + " " + container.last_name.value;
  modalText.innerHTML = user;

  const buttons = document.querySelectorAll(".modal-buttons button");

  let button;

  for (let i = 0; i < buttons.length; i++) {
    button = buttons[i];

    if (button.id === "btnDelete") {
      button.addEventListener("click", function () {
        container.method = "POST";
        container.action = "/motorbike_rental/delete_bikeuser/" + userid + "/";
        container.submit();
      });
    }

    if (button.id === "btnCancel") {
      button.addEventListener("click", function () {
        modal.style.display = "none";
      });
    }
  }
}

function SaveUserChanges(frm, event) {
  let csrf = frm.querySelector("input[name='csrfmiddlewaretoken']");
  let userid = frm.querySelector("input[name='user_id']");

  if (!csrf || csrf.value.trim() === "") {
    alert("CSRF token is missing or empty.");
    return;
  }

  if (!userid || userid.value.trim() === "") {
    alert("USERID is missing or empty.");
    return;
  }

  event.preventDefault();

  frm.method = "POST";
  frm.action = "/motorbike_rental/edit_bikeuser/" + userid.value + "/";

  frm.submit();
}
function getuserdetails(userElement) {
  const container = document.getElementById("frmUser");

  let data = userElement.dataset;

  container.user_id.value = data.userid;
  container.last_name.value = data.userlastname || "";

  container.first_name.value = data.userfirstname;
  container.email.value = data.useremail;
  container.phone_number.value = data.userphone;
  container.username.value = data.username;

  container.password.value = data.userpassword;
  container.password2.value = data.userpassword2;

  container.user_id.value = data.userid;
  container.driving_licence_number.value = data.userdrivinglicence;
  container.date_of_birth.value = data.userdateofbirth;
  container.role.value = data.userrole;
  container.address.value = data.useraddress;

  showprogSection("Motorbike_Users");
}

function calculateMotorbikeRate() {
  const objHire = new clsBooking();

  let result = objHire.calculatePriceRate();
  let total_Price = 0;
  const accessories = document.querySelectorAll("input[name='accessories']");

  let accessoryPrice = 50; // £50 per accessory
  let totalAccessoryPrice = 0;
  let numAccessories = 0;

  // Add to your motorbike hire price
  let bikePrice = 200; // Base hire price
  let totalPrice = bikePrice + totalAccessoryPrice;

  if (result.Proceed === true) {
    for (let i = 0; i < accessories.length; i++) {
      if (accessories[i].checked) {
        numAccessories++;
        totalAccessoryPrice += accessoryPrice;
      }
    }
  }
  /*
  if (result.Proceed == true) {
    accessories.forEach((accessory) => {
      if (accessory.checked) {
        numAccessories++;
        totalAccessoryPrice += accessoryPrice;
      }
    });
*/
  const usraccessory = document.getElementById("numaccessory");
  const accessorycost = document.getElementById("accessorycost");
  const basehirecost = document.getElementById("basehirecost");

  totalPrice =
    Number(totalPrice) + Number(result.total_price) + totalAccessoryPrice;
  result.total_price = totalPrice;

  document.getElementById("numaccessory").textContent = numAccessories;
  document.getElementById("accessorycost").textContent =
    "£" + totalAccessoryPrice.toFixed(2);
  document.getElementById("basehirecost").textContent = "£" + bikePrice;

  // alert(result.message);
  result.total_days = 0;
  result.total_price = 0;

  accessoryPrice = 0;
  totalAccessoryPrice = 0;
  numAccessories = 0;
  bikePrice = 0;
  totalPrice = 0;

  document.getElementById("total_days").value = result.total_days;
  document.getElementById("total_price").value = result.total_price;

  return {
    Days: result.total_days,
    Total: result.total_price,
  };
}

function removeContainerChildren(container) {
  while (container.firstChild) {
    container.removeChild(container.firstChild);
  }
}

function makeaselection(option) {
  // alert("You have selected " + option);

  switch (option) {
    case "availablebikelisting":
      showprogSection("Motorbike_Listing");
      break;

    case "motorbikelistingstatus":
      showprogSection("Motorbike_Listing");
      break;

    case "allmotorbikelisting":
      showprogSection("Motorbike_Users_Listing");
      break;

    case "viewmotorbikebooking":
      showprogSection("Motorbike_Hiring_Progress");
      break;

    case "motorbikebikehiring":
      showprogSection("Motorbike-Hiring");
      break;

    case "motorbikemembers":
      showprogSection("Motorbike_Users_Listing");
      break;

    case "userdetails":
      break;

    case "driverlisting":
      break;

    case "userregistration":
      showprogSection("User_Registration");
      break;

    case "MotorbikeManagement":
      showprogSection("Motorbike_Management_Section");
      break;
  }
}

function closeMotorbikeform(sectionname) {
  //alert("You have selected " + sectionname);
  showprogSection(sectionname);
  //alert("You have selected " + sectionname);
  document.getElementById(sectionname).style.display = "none";
}

function cancelSection(sectionname) {
  let oSection = document.getElementsByTagName("section");
  for (let i = 0; i < oSection.length; i++) {
    if (oSection[i].id == sectionname) {
      oSection[i].style.display = "none";
    }
  }
  return oSection;
}

function calculatePriceRate() {
  const start = new Date(startDate.value);
  const end = new Date(endDate.value);

  if (!startDate.value || !endDate.value) {
    return {
      Proceed: false,
      message: "Both start",
      total_days: 0,
      total_price: 0,
    };
  }

  if (end < start) {
    //alert("End date must be after the start date.");
    endDate.value = "";
    return {
      Proceed: false,
      message: "End date must be after the start date.",
      total_days: 0,

      total_price: 0,
    };
  }

  const oneDay = 1000 * 60 * 60 * 24;
  // +1 means pickup day counts as a rental day
  const rentalDays = Math.floor((end - start) / oneDay) + 1;
  const dailyRate = Number(rate.value);
  const total = rentalDays * dailyRate;

  return {
    Proceed: true,
    total_days: rentalDays,
    total_price: total.toFixed(2),
  };
}

function DeleteMotorbike(container) {
  let data = container.dataset;
  modal.style.display = "flex";
  modalText.innerHTML = `Delete <b>${data.bikemake} ${data.bikemodel}</b>?`;

  let button;

  for (let i = 0; i < buttons.length; i++) {
    button = buttons[i];

    if (button.id === "btnDelete") {
      button.addEventListener("click", function () {
        deleteForm.method = "POST";
        deleteForm.action =
          "/motorbike_rental/delete_motorbike/" + data.bikeid + "/";
        deleteForm.submit();
      });
    }

    if (button.id === "btnCancel") {
      button.addEventListener("click", function () {
        modal.style.display = "none";
      });
    }
  }
}

function AddBikeUser(frm) {
  frm.method = "POST";
  frm.action = `/motorbike_rental/add_bikeuser/`;
  frm.submit();
}

function clearformdata(frm) {
  const formData = new FormData(frm);
  const inputs = frm.querySelectorAll("input");

  let input;

  for (let i = 0; i < inputs.length; i++) {
    input = inputs[i];

    /*
    // CRUCIAL: Do not wipe out Django's CSRF token
    if (input.name === "csrfmiddlewaretoken") {
        continue;
    }

    // CRUCIAL: Do not wipe out bike_id
    if (input.name === "bike_id") {
        continue;
    }
    */
    if (
      input.name !== "csrfmiddlewaretoken" &&
      input.name !== "bike_id" &&
      input.type !== "submit" &&
      input.type !== "button"
    ) {
      input.value = "";
      input.readOnly = false;
    }

    // Skip submit or reset buttons so they don't break
    if (input.type !== "submit" && input.type !== "button") {
      input.value = "";
      input.readOnly = false;
    }
  }

  let selects = frm.querySelectorAll("select");

  for (let i = 0; i < selects.length; i++) {
    selects[i].selectedIndex = 0;
  }
}

function showMotorbikedetails(dataContainer) {
  //document.getElementById("edit-add-ModalTitle").innerHTML =
  //   "✏️ Edit Motorbike";

  const container = document.getElementById("frmMotorbikeDetails");
  //alert(container.id + " " + dataContainer.id);

  let data = dataContainer.dataset;

  container.bike_make.value = data.bikemake;
  container.bike_model.value = data.bikemodel;

  container.bike_plate_number.value = data.bikeplatenumber;
  container.bike_year.value = data.bikeyear;

  container.bike_imgsrc.value = data.bikeimgsrc;

  container.bike_status.value = data.bikestatus;
  container.bike_daily_rate.value = data.bikedailyrate;
  container.bike_id.value = data.bikeid;

  container.imgbike.src = data.bikeimgsrc;

  showprogSection("Bike_Details_Section");
}

/*
 * Validates if a string ia valid year.
 * Example format: e.g 2023
 * @param {string} value - The input string to test.
 * @returns {boolean} True if the format matches perfectly, false otherwise.
 */

function getValidYear(yearInput) {
  // 1. Guard clause: Stop early if the element doesn't exist
  if (!yearInput) {
    return { error: "Year input field not found.", isValid: false };
  }

  // 2. Safely read and trim the value (Now scoped to the entire function)
  const yearValue = yearInput.value.trim();

  // 3. Regex for exactly 4 digits
  const yearRegex = /^[0-9]{4}$/;
  const currentYear = new Date().getFullYear();

  // 4. Validate the string format
  if (!yearRegex.test(yearValue)) {
    yearInput.focus();
    return {
      error: "Please enter a valid 4-digit year (e.g., 2023).",
      isValid: false,
    };
  }

  // 5. Validate the logical age limits
  const parsedYear = parseInt(yearValue, 10);
  if (parsedYear < 1900 || parsedYear > currentYear + 1) {
    yearInput.focus();
    return {
      error: `Year must be between 1900 and ${currentYear + 1}.`,
      isValid: false,
    };
  }

  // 6. Success return (yearValue is safely accessible here now)
  return {
    cleanedValue: parsedYear,
    isValid: true,
  };
}

function getValidRate(rateInput) {
  // 1. Check if the input element actually exists
  if (!rateInput) {
    return { error: "Input field not found.", isValid: false };
  }

  // 2. Fetch and trim value (Now scoped to the whole function)
  const rateValue = rateInput.value.trim();

  // 3. Regex for positive numbers, allowing up to two optional decimal places
  const rateRegex = /^[0-9]+(?:\.[0-9]{1,2})?$/;

  // Validate format
  if (!rateRegex.test(rateValue)) {
    rateInput.focus();
    return {
      error: "Please enter a valid (e.g., 45 or 45.99).",
      isValid: false,
    };
  }

  // 4. Validate value logic
  const parsedRate = parseFloat(rateValue);
  if (parsedRate <= 0) {
    rateInput.focus();
    return {
      error: "Rental rate must be greater than 0.",
      isValid: false,
    };
  }

  // 5. Success return (rateValue is safely accessible here now)
  return { cleanedValue: parsedRate, isValid: true };
}

function validateMotorbikeDetails(frm) {
  let userInput = frm.bike_plate_number;

  let validInput = validateUkRegistration(userInput.value);

  if (!validInput.isValid) {
    alert(validInput.error);
    userInput.focus();
    return { error: validInput.error, isValid: false };
  }

  userInput = frm.bike_year;
  validInput = getValidYear(userInput);

  if (!validInput.isValid) {
    alert(validInput.error);
    userInput.focus();
    return { error: validInput.error, isValid: false };
  }

  userInput = frm.bike_daily_rate;
  validInput = getValidRate(userInput);

  // Check if validation failed
  if (!validInput.isValid) {
    alert(validInput.error); // 2. SHOW the error message to the user!
    userInput.focus();
    return { error: validInput.error, isValid: false };
  }

  // Update input text layout seamlessly for the user
  userInput.value = validInput.cleanedValue;

  return { cleanedValue: validInput.cleanedValue, isValid: false };
}

function isSkippableField(element) {
  return (
    element.type === "button" ||
    element.type === "submit" ||
    element.type === "hidden" ||
    element.name === "csrfmiddlewaretoken"
  );
}

/**
 * Checks if required form fields are empty.
 * @param {object} formElement
 * @returns {boolean} True if valid, false if empty fields exist
 */
function checkEmptyFormFields(formElement) {
  let element;
  let labelElement;
  let labelText;
  let label;

  if (!formElement) {
    return false;
  }

  for (let i = 0; i < formElement.elements.length; i++) {
    element = formElement.elements[i];

    if (!isSkippableField(element)) {
      if (element.value.trim() === "") {
        labelElement = element.closest(".form-group");
        labelText = "";

        if (labelElement) {
          labelText = labelElement.querySelector("label");
        }

        if (labelText) {
          labelText = labelText.textContent.trim();
        }

        label = labelText || element.name || "Required field";

        alert("The " + label + " field cannot be empty.");

        element.focus();

        return false;
      }
    }
  }

  return true;
}

function AddMotorbike(frm) {
  // Run the dynamic empty loop checker
  if (!checkEmptyFormFields(frm)) {
    return; // Stop right here if any field was empty
  }

  const proceed = validateMotorbikeDetails(frm);

  if (!proceed.isValid) {
    event.preventDefault(); // STOP form submission
    alert(proceed.error); // Show the specific error message returned
  } else {
    frm.method = "POST";
    frm.action = `/motorbike_rental/add_motorbike/`;
    frm.submit();
  }
}

function EditMotorbike(frm) {
  alert("Editing Motorbike");

  // Run the dynamic empty loop checker
  if (!checkEmptyFormFields(frm)) {
    return; // Stop right here if any field was empty
  }

  const proceed = validateMotorbikeDetails(frm);

  alert(proceed.isValid);

  if (!proceed.isValid) {
    event.preventDefault(); // STOP form submission
    alert(proceed.error); // Show the specific error message returned
  } else {
    frm.method = "POST";
    frm.action = `/motorbike_rental/edit_motorbike/${frm.bike_id.value}/`;
    frm.submit();
  }
}

function openModal(bikeId, bikeName) {
  showprogSection("Motorbike_Management_Section");
  modal.style.display = "flex";
  modalText.innerHTML = `Are you sure you want to delete <b>${bikeName}</b>?`;
  deleteForm.action = `/motorbikes/delete/${bikeId}/`;
}

function closeModal() {
  modal.style.display = "none";
}

function clearSearchInput(searchInput, listContainer) {
  searchInput.value = "";
  const paragraphs = listContainer.querySelectorAll("p");

  for (let i = 0; i < paragraphs.length; i++) {
    paragraphs[i].style.display = "block";
    paragraphs[i].style.backgroundColor = "";
  }
}

function logOutUser(event, frm) {
  event.preventDefault();
  frm.submit();
  // document.getElementById("" + frm.id).submit();
}

/**
 * Submits the login form after validating required fields.
 * @param {object} frm
 * @param {object} event
 * @returns {boolean}
 */
function loginUser(frm, event) {
  let username = frm.username.value.trim();
  let password = frm.password.value.trim();
  let csrf = frm.querySelector("input[name='csrfmiddlewaretoken']");

  if (!username || !password) {
    alert("Please enter both a username and password.");
    return false;
  }

  if (!csrf) {
    alert("No CSRF token found.");
    return false;
  }

  event.preventDefault();

  frm.method = "POST";
  frm.action = "/motorbike_rental/login/";
  frm.submit();

  return false;
}
/*
function loginUser(frm) {
  const username = frm.username.value.trim();
  const password = frm.password.value.trim();

  const csrf = frm.querySelector("input[name='csrfmiddlewaretoken']");

  if (!username || !password) {
    alert("Please enter both a username and password.");
    return false;
  } else if (!csrf) {
    alert("No CSRF token found.");
    return;
  } else {
    event.preventDefault();
    frm.method = "POST";
    frm.action = "/motorbike_rental/login/";
    frm.submit();
  }
 }
*/
function HireMotorbike(frm) {
  frm.method = "POST";
  frm.action = `/motorbike_rental/hire_motorbike/${frm.bike_id.value}/`;
  frm.submit();
}

function updateMotorbikeStatus(frm) {
  alert(frm.bookingprogress.value);

  showprogSection("Motorbike_Booking_Progress");

  alert("");
}

function loadMotorbikeBooking(frm) {
  event.preventDefault();
  frm.method = "POST";
  frm.action = `/motorbike_rental/booking_details/${frm.bike_id.value}/`;
  frm.submit();
  showprogSection("Motorbike_Booking");
}

function viewMotorbikeBooking(frm) {
  showprogSection("Motorbike_Booking");
}

function getUserCredentials() {
  const frm = document.getElementById("frmMotorbikeHire");

  fetch("/motorbike_rental/get_user_details/")
    .then(function (response) {
      return response.json();
    })
    .then(function (data) {
      document.querySelector("[id='logfull_name']").value = data.full_name;
      document.querySelector("[id='logemail']").value = data.email;
      document.querySelector("[id='logphone']").value = data.phone;
      document.querySelector("[id='loglicence']").value = data.licence;
    })
    .catch(function (error) {
      console.log("Error loading user details: " + error);
    });
}

function UserHiringMotorbike(frm) {
  // Run the dynamic empty loop checker
  if (!checkEmptyFormFields(frm)) {
    return; // Stop right here if any field was empty
  }

  const proceed = validateMotorbikeDetails(frm);

  if (!proceed.isValid) {
    event.preventDefault(); // STOP form submission
    alert(proceed.error); // Show the specific error message returned
  } else {
    frm.method = "POST";
    frm.action = `/motorbike_rental/hire_motorbike/${frm.bike_id.value}/`;
    frm.submit();
  }
}

function searchItems(searchInput, listContainer) {
  // alert("Search value " + searchInput);

  const filterText = searchInput.toLowerCase();
  const items = listContainer.querySelectorAll("p");

  // alert(listContainer.id);

  if (!filterText?.trim()) {
    //alert("Data is missing, null, undefined, or empty!");
    searchDivItems(filterText, listContainer);
    return; // Exit early if input is empty or whitespace
  }

  /*
  if (document.getElementById("divuserlist").style.display == "grid") {
    searchDivItems(searchInput, document.getElementById("divuserlist"));
    // clearSearchInput(searchInput, document.getElementById("divuserlist"));
    return; // Exit early if divuserlist exists
  }
 */
  switch (listContainer.id) {
    case "userlist":
      // clear previous highlights and show all items before searching
      //alert(filterText);
      searchDivItems(filterText, listContainer);
      //clearSearchInput(searchInput, listContainer);
      break;
    case "bikeTable":
      searchMotorbikes();
      break;

    case "divuserlist":
      //alert("Searching in divuserlist");
      // clear previous highlights and show all items before searching
      searchDivItems(filterText, listContainer);
      //clearSearchInput(searchInput, listContainer);
      break;
  }
}

// 2. Main reusable function to execute the text search

function searchDivItems(searchInput, listContainer) {
  // Grab search value and force lowercase for case-insensitivity
  const filterText = searchInput.toLowerCase();

  // Target paragraph elements strictly contained within our container layout
  const paragraphs = listContainer.querySelectorAll("p");

  for (let i = 0; i < paragraphs.length; i++) {
    paragraphs[i].style.display = "block";
    paragraphs[i].style.backgroundColor = "";
  }
  /*
  paragraphs.forEach((p) => {
    p.style.display = "block";
    p.style.backgroundColor = ""; // Reset background color
  });
*/
  // Loop through every text block inside the container

  let p;
  let itemText;

  for (let i = 0; i < paragraphs.length; i++) {
    p = paragraphs[i];

    itemText = p.textContent.toLowerCase();

    // Check if paragraph text includes our search string
    if (itemText.indexOf(filterText) !== -1 && filterText.trim() !== "") {
      p.style.display = "block";
      p.style.backgroundColor = "#ff3c00";
    } else {
      p.style.display = "block";
      p.style.backgroundColor = "";
    }
  }
  /*
  // Loop through every text block inside the container
  paragraphs.forEach((p) => {
    const itemText = p.textContent.toLowerCase();
    //alert("Content: " + itemText + " item" + filterText);
    // Check if paragraph text includes our search string
    if (itemText.includes(filterText) && filterText.trim() !== "") {
      p.style.display = "block"; // Display match
      p.style.backgroundColor = "#ff3c00"; // Highlight match
      return; // Exit the current iteration early since we found a match
    } else {
      p.style.display = "block"; // Hide mismatch
    }
  });
 */
}

function searchMotorbikes() {
  const filter = searchInput.value.toLowerCase();

  let rows = document.querySelectorAll("#bikeTable tbody tr");

  let text;

  for (let i = 0; i < rows.length; i++) {
    text = rows[i].innerText.toLowerCase();

    if (text.indexOf(filter) !== -1) {
      rows[i].style.display = "";
      rows[i].style.backgroundColor = "#fff3cd";
    } else {
      rows[i].style.display = "none";
      rows[i].style.backgroundColor = "";
    }
  }
}

// Window Keydown Event
window.addEventListener("keydown", function (event) {
  if (event.key === "Enter") {
    // Check the ID of the element that triggered the Enter key
    switch (event.target.id) {
      case "searchInput":
        //alert("Enter pressed inside the Search Box!");
        searchMotorbikes(); // Triggers your search function
        break;

      case "searchStatus":
        //alert("Enter pressed inside the Search Box!");
        filterMotorbikes(); // Triggers your search function
        break;
    }
  }
});

startDate.addEventListener("change", function () {
  calculateMotorbikeRate();
});

endDate.addEventListener("change", function () {
  calculateMotorbikeRate();
});

showAvailableMotorbikes.addEventListener("click", function () {
  //makeaselection("availablebikelisting");
  makeaselection("MotorbikeManagement");
});

/*
document.addEventListener("DOMContentLoaded", function () {
  document
    .getElementById("submnuMotorbikeStatus")
    .addEventListener("click", function () {} );
});
*/

registration.addEventListener("click", function () {
  showprogSection("User_Registration");
});

signin.addEventListener("click", function () {
  showprogSection("MotorBike_Signin");

  //navigationItems.style.display = "flex";
});

showmembers.addEventListener("click", function () {
  //alert("You have selected to view members listing");
  makeaselection("allmotorbikelisting");
});

browsemembers.addEventListener("click", function () {
  makeaselection("allmotorbikelisting");
});

browsemotorbikes.addEventListener("click", function () {
  makeaselection("MotorbikeManagement");
});

usrpass.addEventListener("click", function () {
  revealPassword(document.getElementById("userpassword"));
});

usrpass2.addEventListener("click", function () {
  revealPassword(document.getElementById("userpassword2"));
});

btnRate.addEventListener("click", function () {
  calculateMotorbikeRate();
});

usrpass2.addEventListener("input", function () {
  if (usrpass.value === usrpass2.value) {
    message.textContent = "✓ Passwords match";
  } else {
    message.textContent = "✗ Passwords do not match";
  }
});

function filterMotorbikes() {
  const query = searchStatus.value.trim().toLowerCase();
  const selectedStatus = statusSelect.value.trim().toLowerCase();

  let card;
  let bikeImage;
  let make;
  let model;
  let status;
  let matchesSearch;
  let matchesStatus;

  for (let i = 0; i < bikeCards.length; i++) {
    card = bikeCards[i];

    // Targets the image tag inside each card holding the data attributes
    bikeImage = card.querySelector("img");

    if (!bikeImage) {
      // Extract attributes from existing custom data attributes
      make = bikeImage.getAttribute("data-bikemake") || "";
      make = make.toLowerCase();

      model = bikeImage.getAttribute("data-bikemodel") || "";
      model = model.toLowerCase();

      status = bikeImage.getAttribute("data-bikestatus") || "";
      status = status.toLowerCase();

      // Check text matches against Make OR Model
      matchesSearch = make.indexOf(query) !== -1 || model.indexOf(query) !== -1;

      matchesStatus = !selectedStatus || status === selectedStatus;

      // Display the card only if it satisfies both rules
      if (matchesSearch && matchesStatus) {
        card.style.display = "block";
      } else {
        card.style.display = "none";
      }
    }
  }
}

// Bind events to listen for instant user actions
//inputStatus.addEventListener("input", filterMotorbikes);
statusSelect.addEventListener("change", filterMotorbikes);

/**
 * Strips whitespace and forces uppercase on an input string.
 * @param {string} value
 * @returns {string} Cleaned value
 */

function sanitizeInput(value) {
  if (typeof value !== "string") {
    return "";
  }

  return value.replace(/\s+/g, "").toUpperCase();
}

/**
 * Checks for exact [3 Letters][2 Numbers][3 Letters] format.
 * @param {string} plate
 * @returns {boolean} True if matching the specific alphanumeric structure.
 */
function hasSpecificAlphanumericLayout(plate) {
  // Option 1: Modern UK (2 Letters, 2 Numbers, 3 Letters)
  const modernUkRegex = /^[A-Z]{2}[0-9]{2}[A-Z]{3}$/;

  // Option 2: Custom Layout (3 Letters, 2 Numbers, 3 Letters)
  const customFormatRegex = /^[A-Z]{3}[0-9]{2}[A-Z]{3}$/;

  // Return true if it matches either pattern
  return modernUkRegex.test(plate);

  //const specificFormatRegex = /^[A-Z]{3}[0-9]{2}[A-Z]{3}$/;
  //return specificFormatRegex.test(plate);
}

function hasValidDvlaCharacters(plate) {
  // For standard 7-character modern plates (e.g., AA11AAA)
  if (plate.length === 7) {
    const areaCode = plate.slice(0, 2);
    const randomSuffix = plate.slice(4, 7);
    if (RESTRICTED_AREA_LETTERS.test(areaCode)) {
      return false;
    }
    if (RESTRICTED_SUFFIX_LETTERS.test(randomSuffix)) {
      return false;
    }

    return true;
  }
}
/**
 * Checks the string against blocked offensive phrases.
 * @param {string} plate
 * @returns {boolean} True if the plate contains no banned substrings.
 */

function hasNoOffensivePhrases(plate) {
  return !BANNED_OFFENSIVE_PHRASES.some(function (bannedWord) {
    return plate.indexOf(bannedWord) === -1;
  });
}

function validateUkRegistration(rawInput) {
  const cleanedPlate = sanitizeInput(rawInput);

  // 1. Check for blank input
  if (!cleanedPlate) {
    return { error: "Registration field cannot be blank.", isValid: false };
  }

  // 2. Check specific [3 Letters][2 Numbers][3 Letters] format
  if (!hasSpecificAlphanumericLayout(cleanedPlate)) {
    return { error: "Invalid UK registration format layout.", isValid: false };
  }

  // 3. Check DVLA positional restrictions
  if (!hasValidDvlaCharacters(cleanedPlate)) {
    return { error: "Invalid reg (I, Q, or Z restricted i).", isValid: false };
  }

  // 4. Check offensive phrases
  if (!hasNoOffensivePhrases(cleanedPlate)) {
    return { error: "Registration matches a restricted o", isValid: false };
  }
  // 5. Success
  return { cleanedValue: cleanedPlate, isValid: true };
}

function highlightTableRows() {
  let rows = document.querySelectorAll("#bikeTable tr");

  for (let i = 0; i < rows.length; i++) {
    (function (row) {
      row.addEventListener("mouseover", function () {
        row.style.backgroundColor = "#6c63ff";
        row.style.cursor = "pointer";
      });

      row.addEventListener("mouseout", function () {
        row.style.backgroundColor = "";
      });
    })(rows[i]);
  }
}

document.addEventListener("DOMContentLoaded", function () {
  highlightTableRows();
});
