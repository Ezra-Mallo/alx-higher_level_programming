#!/usr/bin/node
/*
Write a script that prints My number: <first argument converted in integer> if the first argument can be converted to an integer:
  If the argument can’t be converted to an integer, print “Not a number”
  You must use console.log(...) to print all output
  You are not allowed to use var
  You are not allowed to use try/catch
 */

const process = require('process');
const myVar = process.argv;

if (typeof (myVar[2]) !== 'undefined') {
  const arg = parseInt(myVar[2]);

  if ((typeof (arg === 'number')) || (arg !== 'NaN')) {
    console.log('My number: ' + arg);
  } else {
    console.log('Not a number');
  }
}
