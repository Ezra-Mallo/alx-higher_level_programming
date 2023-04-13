#!/usr/bin/node
/*
 Write a script that concats 2 files.
   The first argument is the file path of the first source file
   The second argument is the file path of the second source file
   The third argument is the file path of the destination
 */

const fs = require('fs');
const process = require('process');
const readline = require('readline');

const firstSrcFile = process.argv[2];
const secondSrcFile = process.argv[3];
const destFile = process.argv[4];

const inputStreamA = fs.createReadStream(firstSrcFile);
const inputStreamB = fs.createReadStream(secondSrcFile);
const outputStream = fs.createWriteStream(destFile, { encoding: 'utf8' });

const lineReaderA = readline.createInterface({
  input: inputStreamA, terminal: false
});

const lineReaderB = readline.createInterface({
  input: inputStreamB, terminal: false
});

lineReaderA.on('line', function (line) {
  outputStream.write(line + '\n');
});

lineReaderB.on('line', function (line) {
  outputStream.write(line + '\n');
});
