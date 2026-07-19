function EditMotorbikeold(id, make, model, plate, year, imgsrc, status, rate) {
  //AddEditBikeForm.action = `/motorbikes/edit/${id}/`;

  document.getElementById("Bike_Details_Section").style.display = "block";

  document.getElementById("bike_info_title").innerHTML = "✏️ Edit Motorbike";
  //var form = document.getElementById("frmMotorbike").elements;

  const form = document.getElementById("frmMotorbike");
  form["bike_make"].value = make;
  form["bike_model"].value = model;
  form["bike_plate_number"].value = plate;
  form["bike_year"].value = year;
  form["bike_imgsrc"].value = imgsrc;
  form["bike_status"].value = status;
  form["bike_daily_rate"].value = rate;
  form["bike_id"].value = id;

  form.method = "POST";
  //form.action = `/motorbikes/edit/${id}/`;
  // form.action = "{% url 'add_motorbike' %}";
  //form.action = `/editing_motorbike/`; //working but needs to be fixed to include the bike id in the url
  //form.action = `{% url 'index.html' %}`;
  //form.action = `/managing_motorbike/edit/${id}/`;
  //form.action = `/managing_motorbike/edit/${id}/`;
  //form.action = `/motorbikes/edit/${id}/`; // this works fine nbut data is not being populated in the form
  //form.submit();

  //showprogSection("Bike_Details_Section");
  /*
  for (var i = 0; i < form.length; i++) {
    if (form[i].type == "text") {
      if (form[i].id == "bike_make") {
        form[i].value = make;
      }

      if (form[i].id == "bike_model") {
        form[i].value = model;
      }

      if (form[i].id == "bike_year") {
        form[i].value = year;
      }

      if (form[i].id == "bike_status") {
        form[i].value = status;
      }

      if (form[i].id == "bike_plate_number") {
        form[i].value = plate;
      }

      if (form[i].id == "bike_imgsrc") {
        form[i].value = imgsrc;
      }

      if (form[i].id == "bike_daily_rate") {
        form[i].value = rate;
      }

      if (form[i].id == "bike_id") {
        form[i].value = id;
      }
    }
  }
  */
}
