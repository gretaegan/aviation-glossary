// Code to validate form from Bootstrap docs

(function() {
    'use strict';
    window.addEventListener('load', function() {
      var forms = document.getElementsByClassName('needs-validation');
      var validation = Array.prototype.filter.call(forms, function(form) {
        form.addEventListener('submit', function(event) {
          if (form.checkValidity() === false) {
            event.preventDefault();
            event.stopPropagation();
          }
          form.classList.add('was-validated');
        }, false);
      });
    }, false);
  })();


// Scroll button to top of page - code help from w3schools

var scrollButton = document.getElementById("scrollBtn");

window.onscroll = function() {scrollFunction();
};

function scrollFunction() {
  if (document.body.scrollTop > 30 || document.documentElement.scrollTop > 30) {
    scrollButton.style.display = "block";
  } else {
    scrollButton.style.display = "none";
  }
}

function topFunction() {
  document.body.scrollTop = 0;
  document.documentElement.scrollTop = 0;
}


// Code to fade in text on hero image - code from https://www.geeksforgeeks.org/how-to-add-fade-in-effect-using-pure-javascript/


var opacity = 0;
var intervalID = 0;
window.onload = fadeIn;

function fadeIn() {
  setInterval(show, 200);
}

function show() {
  var body = document.getElementById("body");
  opacity = Number(window.getComputedStyle(body).getPropertyValue("opacity"));

  if (opacity < 1) {
    opacity = opacity + 0.1;
    body.style.opacity = opacity;
  } else {
    clearInterval(intervalID);
  }
}
