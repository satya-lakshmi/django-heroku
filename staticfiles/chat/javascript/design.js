/*This script is for adding the every selected design in the form as a input for multipe tag*/

window.addEventListener('load', (event) => {
      var styleIds = [];//globally initializing the styleIds array
      function initStyles() { // function for getting the ids from the local storage into the styleIds array
        var storedNames = JSON.parse(localStorage.getItem("styles") || '[]');
        styleIds = storedNames.map(element => JSON.parse(element).id);
        console.log('styleIds'.styleIds)
      }
      function addArrToList() {
        var select = document.getElementById("design");
        for (var i = 0; i < styleIds.length; i++) {
          var option = document.createElement("OPTION");
          var txt = document.createTextNode(styleIds[i]);
          option.appendChild(txt);
          option.setAttribute("selected",styleIds[i]);
          select.appendChild(option);
}
}
initStyles();
addArrToList();
});