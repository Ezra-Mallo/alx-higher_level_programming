#!/usr/bin/node

const process = require('process');
const fs = require('fs');

const file1 = process.argv[2];
const file2 = process.argv[3];
const file3 = process.argv[4];

if (file1 !== '') {
  fs.readFile(file1, 'utf-8', (err, data) => {
    if (err) {
      console.log(err);
    }
    fs.appendFile(file3, data, () => {});
  });
}

if (file2 !== '') {
  fs.readFile(file2, 'utf-8', (err, data) => {
    if (err) {
      console.log(err);
    }
    fs.appendFile(file3, data, () => {});
  });
}
