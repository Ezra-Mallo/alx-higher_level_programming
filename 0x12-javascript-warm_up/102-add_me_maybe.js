#!/usr/bin/node

exports.addMeMaybe = function (a, recursiveFunction) {
  recursiveFunction(++a);
};
