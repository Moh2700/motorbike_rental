const modal = document.getElementById("deleteModal");
const deleteForm = document.getElementById("deleteForm");
const modalText = document.getElementById("modalText");

const AddEditBikeModal = document.getElementById("AddEditBikeModal");
const AddEditBikeForm = document.getElementById("AddEditBikeForm");

function openModal(bikeId, bikeName) {
  modal.style.display = "flex";

  modalText.innerHTML = `Are you sure you want to delete <b>${bikeName}</b>?`;

  deleteForm.action = `/motorbikes/delete/${bikeId}/`;
}

function closeModal() {
  modal.style.display = "none";
}

function closeMotorbikeform() {
  AddEditBikeModal.style.display = "none";
}
function AddMotorbike() {
  AddEditBikeModal.style.display = "flex";
  document.getElementById("AddEditBikeForm").reset();
  document.getElementById("edit-add-ModalTitle").innerHTML = "🏍️ Add Motorbike";
}

function EditMotorbike(id, make, model, plate, year, imgsrc, status, rate) {
  document.getElementById("edit-add-ModalTitle").innerHTML =
    "✏️ Edit Motorbike";
  AddEditBikeModal.style.display = "flex";

  AddEditBikeForm["bike_make"].value = make;
  AddEditBikeForm["bike_model"].value = model;
  AddEditBikeForm["bike_plate_number"].value = plate;
  AddEditBikeForm["bike_year"].value = year;
  AddEditBikeForm["bike_imgsrc"].value = imgsrc;
  AddEditBikeForm["bike_status"].value = status;
  AddEditBikeForm["bike_daily_rate"].value = rate;

  AddEditBikeForm.action = `/motorbikes/edit/${id}/`;
}

function searchMotorbikes() {
  const filter = searchInput.value.toLowerCase();

  const rows = document.querySelectorAll("#bikeTable tbody tr");

  rows.forEach((row) => {
    const text = row.innerText.toLowerCase();

    if (text.includes(filter)) {
      row.style.display = "";
      row.style.backgroundColor = "#fff3cd";
    } else {
      row.style.display = "none";
    }
  });
}

// Window Keydown Event
window.addEventListener("keydown", function (event) {
  if (event.key === "Enter") {
    searchMotorbikes();
  }
});
