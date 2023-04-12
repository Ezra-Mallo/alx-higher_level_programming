#!/usr/bin/node
const add = require('./13-myMath').add;
const mul = require('./13-myMath').mul;
const sub = require('./13-myMath').sub;
const div = require('./13-myMath').div;
const a = 6;
const b = 2;

console.log(a, '+', b, '=', add(a, b));
console.log(a, '-', b, '=', sub(a, b));
console.log(a, '*', b, '=', mul(a, b));
console.log(a, '/', b, '=', div(a, b));
