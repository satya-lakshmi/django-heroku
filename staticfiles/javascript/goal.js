// This is for getting the goal ids that are clicked into the <select> field as selected options in form.html

window.addEventListener('load', (event) => {
      var goalIds = [];
      function initGoals() {
        var storedNames = JSON.parse(localStorage.getItem("goal") || '[]');
        goalIds = storedNames.map(element => JSON.parse(element).id);
      }
      function addArrToList() {
        var select = document.getElementById("goal");
        for (var i = 0; i < goalIds.length; i++) {
          var option = document.createElement("OPTION");
          var txt = document.createTextNode(goalIds[i]);
          option.appendChild(txt);
          option.setAttribute("selected",goalIds[i]);
          select.appendChild(option);
        }
      }
      initGoals();
      addArrToList();//This function calling here will push the goalids as options in <select> field in form.
    });