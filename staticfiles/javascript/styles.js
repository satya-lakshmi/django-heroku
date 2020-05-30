var styles = []
var styleIds = []
function getStyle(id) {
    if (styles.length > 0) {
        var data = { id: id, image: $("#img_"+id).attr('src'),content: $("#cont_" + id).text() }
        var x = JSON.stringify(data)
        var index = styles.indexOf(x)
        if (index == -1) {
            styles.push(x)
        }
        else {
            styles.splice(index, 1)
        }
    }
    else {
        var data = { id: id, image: $("#img_"+id).attr('src'),content: $("#cont_" + id).text() }
        var x = JSON.stringify(data)
        styles.push(x)
    }
    localStorage.setItem("styles", JSON.stringify(styles))
    styleIds = styles.map(element => JSON.parse(element).id);
    console.log(styleIds)
    assample();
}
function assample() {
    $("#design").val(styleIds);
    console.log(styleIds)
}
function initStyles() {
  styles = JSON.parse(localStorage.getItem("styles") || '[]');
  styleIds = styles.map(element => JSON.parse(element).id);
  styleIds.forEach(function(i){$("#design_"+i).addClass('blue');});
}
initStyles();


