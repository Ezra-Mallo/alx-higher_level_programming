#!/usr/bin/node
/*
Write a script that prints two arguments passed to it, in the following format: “ is ”
  You must use console.log(...) to print all output
  You are not allowed to use var
 */

const process = require('process');
const myVar = process.argv;
let arg1 = 'undefined';
let arg2 = 'undefined';

if (typeof (myVar[2]) !== 'undefined') {
  arg1 = myVar[2];
}
if (typeof (myVar[3]) !== 'undefined') {
  arg2 = myVar[3];
}
console.log(arg1 + ' is ' + arg2);
