
var object= [];
function getData(id,image,content)
{
  if (object != []) {
  	if (object[0] == id) {
  		object = [];
  	}else {
  		object = []
  	    var id = id;
  	    var image= $("#img_"+id).attr('src');
  	    var content = $("#cont_"+id).text();
  	    object.push(id);
  	    object.push(image);
  	    object.push(content);
  	    localStorage.setItem("object", JSON.stringify(object));
  }
  }else{
  	object = []
  	var id = id;
  	var image= $("#img_"+id).attr('src');
  	var content = $("#cont_"+id).text();
  	object.push(id);
  	object.push(image);
  	object.push(content);
  }
}
function sample(){  
var storedNames = JSON.parse(localStorage.getItem("object"));
$("#name").val(storedNames[0]);
}

$(document).ready(function(){
var storedNames = JSON.parse(localStorage.getItem("object"));
$('#main_'+storedNames[0]).addClass("blue")
console.log($('#'+storedNames[0]).attr('id'));

});

