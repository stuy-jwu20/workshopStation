// Team Splendid Slugs :: Jonathan Wu, Roshani Shrestha
// SoftDev pd2
// K30 -- canvas based JS drawing
// 2022-02-14m
// time spent: 45 minutes

// JavaScript canvas work

//retrieve node in DOM via ID
var c = document.getElementById("slate");

//instantiate a CanvasRenderingContext2D Object
var ctx = c.getContext("2d");

//init global state var 
var mode = "rect";

// var toggleMode = function(e) {
var toggleMode = (e) => {
    console.log("toggling...");
    var toggle = document.getElementById("buttonToggle");
    if (mode === "rect") {
        mode = "circ";
        toggle.innerHTML = "circle";
    }
    else {
        mode = "rect";
        toggle.innerHTML = "rectangle";
    }
}

var drawRect = function(e) {
    var mouseX = e.offsetX;
    var mouseY = e.offsetY;
    console.log("mouseclick registered at ", mouseX, mouseY);
    ctx.strokeStyle = 'red';
    ctx.fillStyle = 'red';
    ctx.beginPath();
    ctx.fillRect(mouseX, mouseY, 50, 150);
}

//var drawCircle = function(e) {
var drawCircle = (e) => {
    var mouseX = e.offsetX;
    var mouseY = e.offsetY;
    console.log("mouseclick registered at ", mouseX, mouseY);
    ctx.strokeStyle = 'red';
    ctx.fillStyle = 'red';
    ctx.beginPath();
    ctx.arc(mouseX, mouseY, 50, 0, 2 * Math.PI);
    ctx.stroke();
    ctx.fill();
}

//var draw = function(e) {
var draw = (e) => {
    console.log("draw");
    if (mode === "rect") {
        drawRect(e);
    }
    else {
        drawCircle(e);
    }
}

//var wipeCanvas = function() {
var wipeCanvas = () => {
    console.log("wipe")
    ctx.clearRect(0, 0, c.clientWidth, c.clientHeight);
}

c.addEventListener("click", draw);
var bToggler = document.getElementById("buttonToggle");
bToggler.addEventListener("click", toggleMode);
var clearB = document.getElementById("buttonClear");
clearB.addEventListener("click", wipeCanvas); 