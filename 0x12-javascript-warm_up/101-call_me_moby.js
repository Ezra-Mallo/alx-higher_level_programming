#!/usr/bin/node
/*
Write a function that executes x times a function.

The function must be visible from outside
Prototype: function (x, theFunction)
You are not allowed to use var
*/
exports.callMeMoby = function callMeMoby (x, theFunction) {
  if (x > 0) {
    console.log('C is fun');
    x -= 1;
    callMeMoby(x, theFunction);
  }
};
