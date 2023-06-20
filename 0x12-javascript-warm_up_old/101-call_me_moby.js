#!/usr/bin/node

exports.callMeMoby = function (a, recursiveFunction) {
  let i = 0;

  while (i < a) {
    recursiveFunction();
    i++;
  }
};
