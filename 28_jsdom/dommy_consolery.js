// Team Splendid Slugs :: Jonathan Wu, Roshani Shrestha
// SoftDev pd2
// K28 -- Getting more comfortable with the dev console and the DOM
// 2022-02-08t
// time spent: 45 minutes
// --------------------------------------------------


//send diagnostic output to console
//(Ctrl-Shift-K in Firefox to reveal console)
//alternatively, just right click and then inspect.
console.log("AYO");

//assigns strings and intergers to a variable
//notice how there isn't any declaration of what speciifc type of value it is
var i = "hello";
var j = 20;

//assign an anonymous fxn to a var
//if given a value, it will add it with variable j and print it to the console
var f = function(x) {
  var j=30;
  return j+x;
};

//instantiate an object
var o = { 'name' : 'Thluffy',
          age : 15,
          items : [10, 20, 30, 40],
          morestuff : {a : 1, b : 'ayo'},
          func : function(x) {
            return x+30;
          }
        };


//adds a new list item in real time
//appends to the end of the list
var addItem = function(text) {
  var list = document.getElementById("thelist");
  var newitem = document.createElement("li");
  newitem.innerHTML = text;
  list.appendChild(newitem);
};


//removes the nth list item (starting from 0, unlike the list numbering which starts at 1) in real time 
//unlike the addItem, this takes an integer which represents location
var removeItem = function(n) {
  var listitems = document.getElementsByTagName('li');
  listitems[n].remove();
};

//given a list of uncolored text, this will color all the text red.
//it is called with red()
var red = function() {
  var items = document.getElementsByTagName("li");
  for(var i = 0; i < items.length; i++) {
    items[i].classList.add('red');
  }
};

//given a list of text that are already not in stripes (and are uncolored), this will
//change the text color in alternating fashion by calling stripe()
//every even list item is red and every odd list item is blue
var stripe = function() {
  var items = document.getElementsByTagName("li");
  for(var i = 0; i < items.length; i++) {
    if (i%2==0){
      items[i].classList.add('red');
    } else {
      items[i].classList.add('blue');
    }
  }
};

// FIB
var fib = function(n) {
  if (n <= 1) {
      return n;
  }
  else {
      return fib(n - 1) + fib(n - 2);
  }
};

// FAC
var fact = function(n) {
  if (n == 0) {
      return 1;
  }
  else {
      return n * fact(n - 1);
  }
};

// GCD
var gcd = function(a, b) {
  if (a <= b) {
    return gcf(b, a, a);
  }
  else {
    return gcf(a, b, b);
  }
};

//gcd helper function
var gcf = function(a, b, i) {
  if (i == 1) {
    return 1;
  }
  if (a % i == 0 && b % i == 0) {
    return i;
  }
  else {
    return gcf(a, b, (i - 1));
  }
};

//allows one call to each of our calculator functions to appear 
//on the page upon loading index.html
addItem("fib(5) = " + fib(5))
addItem("fact(5) = " + fact(5))
addItem("gcd(15, 39) = " + gcd(15, 39))