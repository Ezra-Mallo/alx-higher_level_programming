#!/usr/bin/node
/*
Write a script that searches the second biggest integer in the list of arguments.

You can assume all arguments can be converted to integer
If no argument passed, print 0
If the number of arguments is 1, print 0
You must use console.log(...) to print all output
You are not allowed to use var
 */

const process = require('process');
let num = 0;
const argLength = process.argv.length;

if (argLength < 3) {
  console.log('0');
} else {
  for (let i = 3; i < argLength; i++) {
    if (parseInt(process.argv[i]) > num) {
      num = process.argv[i];
    }
  }
  console.log(num);
}
