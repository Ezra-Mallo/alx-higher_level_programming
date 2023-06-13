#!/usr/bin/node
/*
 Write a script that computes and prints a factorial
   The first argument is integer (argument can be cast as integer) used
   for computing the factorial
   Factorial of NaN is 1
   You must do it recursively
   You must use a function
   You must use console.log(...) to print all output
   You are not allowed to use var
*/

function factorial (n) {
  let x = 0;

  if (n < 0) {
    return (-1);
  } else if ((n === 0) || (typeof (n) === 'undefined')) {
    return (1);
  } else {
    x = n * factorial(n - 1);
    return (x);
  }
}

const process = require('process');
const myVar = process.argv;

console.log(factorial(myVar[2]));
