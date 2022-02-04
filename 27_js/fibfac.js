// Team Splendid Slugs :: Jonathan Wu, Roshani Shrestha
// SoftDev pd2
// K27 -- Basic functions in JavaScript
// 2022-02-04r
// time spent: 45 minutes
// --------------------------------------------------


var fact = function(n) {
    if (n == 0) {
        return 1
    }
    else {
        return n * fact(n - 1)
    }
}

var fib = function(n) {
    if (n <= 1) {
        return n
    }
    else {
        return fib(n - 1) + fib(n - 2)
    }
}
