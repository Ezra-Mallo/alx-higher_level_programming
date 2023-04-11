#!/usr/bin/node
/*
Write a script that prints the first argument passed to it:
  If no arguments are passed to the script, print “No argument”
  You must use console.log(...) to print all output
  You are not allowed to use var
  You are not allowed to use length
 */

const process = require('process');
const myVar = process.argv;
const varCount = myVar.length;
if (varCount === 2) {
  console.log('No argument');
} else {
  for (let i = 2; i < varCount; i++) {
    console.log(myVar[i]);
  }
}
/*
const process = require('process');
var args = process.argv;
console.log("number of arguments is "+args.length);
args.forEach((val, index) => {
    console.log(`${index}: ${val}`);
});

*/
