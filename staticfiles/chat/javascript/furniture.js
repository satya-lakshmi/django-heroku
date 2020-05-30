window.onload = function() {
  var imagePath = "../static/images/";
  var localStorageSliderNumber;
  var localStorageImagePath;
  if (window.localStorage.getItem('sliderValue') != null) {
    localStorageSliderNumber = window.localStorage.getItem('sliderValue');
  } else {
    window.localStorage.setItem('sliderValue', '1');
    localStorageSliderNumber = 1;
  }
  if (window.localStorage.getItem('imagePath') != null) {
    imagePath = imagePath + window.localStorage.getItem('imagePath') + ".jpg";
  }
  var rangeslider = document.getElementById("sliderRange");
  var output = document.getElementById("sliderOutput");
  var images = document.getElementById("sliderImages");
  rangeslider.value = localStorageSliderNumber;
  //The common line of code extracted into a method
  setData(rangeslider, output, images, localStorageSliderNumber);
  rangeslider.addEventListener('input', function() {
    //call the method once again
    setData(rangeslider, output, images, this.value);
  });
}

function setData(rangeslider, output, images, value) {
  for (var i = 0; i < output.children.length; i++) {
    output.children[i].style.display = 'none';
    images.children[i].style.display = 'none';
  }
  i = Number(value) - 1;
  output.children[i].style.display = 'block';
  images.children[i].style.display = 'block';
  window.localStorage.setItem('imagepath', rangeslider.getAttribute('value'));
  window.localStorage.setItem('sliderValue', (i + 1));
  window.localStorage.setItem('sliderPosition', (i + 1))
}