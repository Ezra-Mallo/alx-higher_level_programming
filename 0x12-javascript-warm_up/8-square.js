#!/usr/bin/node
/*
 Write a script that prints a square
   The first argument is the size of the square
   If the first argument can’t be converted to an integer, print “Missing size”
   You must use the character X to print the square
   You must use console.log(...) to print all output
   You are not allowed to use var
   You must use a loop (while, for, etc.) 
 */

const process = require('process');
const myVar = process.argv;

if (parseInt(myVar[2])) {
  const myNum = Number(myVar[2]);
  for (let i = 0; i < myNum; i++) {
    let myStr = ""
    for (let j = 0; j < myNum; j++){
      myStr +="X"
    }
    console.log(myStr);
  }
} else {
  console.log('Missing size');
}
