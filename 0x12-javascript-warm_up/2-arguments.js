#!/usr/bin/node
/*
 * A script that prints a message depending of the number of arguments passed:
 */

const process = require('process');
const myVar = process.argv;
const varCount = process.argv.length - 2;
if (varCount === 0) {
  console.log('No argument');
} else if (varCount === 1) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
