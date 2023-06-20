#!/usr/bin/node
/*
 Write a script that prints the addition of 2 integers
   The first argument is the first integer
   The second argument is the second integer
   You have to define a function with this prototype: function add(a, b)
   You must use console.log(...) to print all output
   You are not allowed to use var
 */

const process = require('process');
const myVar = process.argv;

if ((parseInt(myVar[2])) && (parseInt(myVar[3]))) {
  console.log(parseInt(myVar[2]) + parseInt(myVar[3]));
} else {
  console.log('NaN');
}
