#!/usr/bin/node
/*
 Write a function that returns the addition of 2 integers.
   The function must be visible from outside
   The name of the function must be add
   You are not allowed to use var
*/

exports.add = function add (a, b) {
  return (a + b);
};

exports.sub = function sub (a, b) {
  return (a - b);
};

exports.div = function div (a, b) {
  return (a / b);
};

exports.mul = function mul (a, b) {
  return (a * b);
};


exports.mod = (a, b) => a % b;

exports.sqr = (a, b) => a ** b;


/*
    OR

exports.add = (a, b) => a + b;

 */
