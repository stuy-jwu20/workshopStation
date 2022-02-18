// Team Keyboard:: Jonathan Wu, Angela Zhang
// SoftDev pd2
// K32 -- more canvas based JS animation
// 2022-02-17t
// time spent: xx minutes

// model for HTML5 canvas-based animation

// SKEELTON

//access canvas and buttons via DOM
var c = document.getElementById("playground"); // GET CANVAS
var dotButton = document.getElementById("buttonCircle"); // GET DOT BUTTON
var stopButton = document.getElementById("buttonStop"); // GET STOP BUTTON
var dvdButton = document.getElementById("dvdScreensaver"); // GET DVD BUTTON

//prepare to interact with canvas in 2D
var ctx = c.getContext("2d");

//set fill color to team color
ctx.fillStyle = 'purple';

var requestID;  //init global var for use with animation frames
var dvdrequestID; //for dvd animation frames


//var clear = function(e) {
var clear = (e) => {
  console.log("clear invoked...")
  ctx.clearRect(0, 0, c.clientWidth, c.clientHeight); //clears canvas
};


var radius = 0;
var growing = true;


//var drawDot = function() {
var drawDot = () => {
  console.log("drawDot invoked...")
  clear();
  window.cancelAnimationFrame(requestID);
  ctx.beginPath();
  ctx.arc(250, 250, radius, 0, 2 * Math.PI);
  ctx.stroke();
  ctx.fill();
  if (growing) { //checks if the dot is growing - if so, the radius will increase; if not, it will decrease
    if (radius >= 250) { //checks if the dot hits the sides of the canvas (or grows larger than that)
      growing = false;
    }
    else {
      radius += 1.75;
    }
  }
  else {
    if (radius === 0) { //checks if the dot shrinks back to having a radius of 0
      growing = true;
    }
    else {
      radius -= 1.75;
    }
  }
  requestID = window.requestAnimationFrame(drawDot);
};

//var stopIt = function() {
var stopIt = () => {
  console.log("stopIt invoked...")
  console.log( requestID );
  console.log( dvdrequestID );
  window.cancelAnimationFrame(requestID);
  window.cancelAnimationFrame(dvdrequestID);
};


//dvd variables h and w are for the picture
var DVDh = 100;
var DVDw = 150;

var DVDx = Math.floor(Math.random() * (c.clientHeight-DVDw))
var DVDy = Math.floor(Math.random() * (c.clientHeight-DVDh))


var drawDVD = () => {

  console.log("drawDVD invoked...")
  clear();
  
  var img = new Image();
  img.src = 'logo_dvd.jpg';
  ctx.drawImage(img, DVDx, DVDy, DVDw, DVDh);;
  
  window.cancelAnimationFrame(dvdrequestID);  
  dvdrequestID = window.requestAnimationFrame(drawDVD);

}

// var img = new Image();
// img.addEventListener('load', function() {
//   drawImage(logo_dvd.jpg, 100, 100)
// }, false);
// img src = 'logo_dvd.jpg'


dotButton.addEventListener( "click", drawDot );
stopButton.addEventListener( "click", stopIt );
dvdScreensaver.addEventListener("click", drawDVD );