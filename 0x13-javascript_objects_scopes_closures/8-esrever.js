#!/usr/bin/node
/*
  Write a function that returns the reversed version of a list:
   Prototype: exports.esrever = function (list)
   You are not allow to use the built-in method reverse
*/

exports.esrever = function (list) {
  const listLen = list.length;
  const newList = [];
  let j = 0;

  for (let i = listLen; i > 0; i--) {
    newList[j] = list[i - 1];
    j++;
  }
  return (newList);
};
