#!/usr/bin/node
const math = require('./14-myMath');
const a = 6;
const b = 2;

console.log(a, '+', b, '=', math.add(a, b));
console.log(a, '-', b, '=', math.sub(a, b));
console.log(a, '*', b, '=', math.mul(a, b));
console.log(a, '/', b, '=', math.div(a, b));
console.log(a, '**', b, '=', math.sqr(a, b));
console.log(a, '%', b, '=', math.mod(a, b));
