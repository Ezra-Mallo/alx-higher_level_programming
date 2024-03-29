#!/usr/bin/node
/*
A script that prints My number: <first argument converted in integer>
if the first argument can be converted to an integer:

If the argument can’t be converted to an integer, print “Not a number”
You must use console.log(...) to print all output
You are not allowed to use var
You are not allowed to use try/catch
 */

const process = require('process');

if (Number.isInteger(parseInt(process.argv[2]))) {
  console.log('My number:', parseInt(process.argv[2]));
} else {
  console.log('Not a number');
}
