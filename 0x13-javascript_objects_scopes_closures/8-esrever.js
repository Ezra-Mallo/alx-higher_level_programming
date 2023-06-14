#!/usr/bin/node
/*
Write a function that returns the reversed version of a list:

Prototype: exports.esrever = function (list)
You are not allow to use the built-in method reverse
*/

exports.esrever = function (list) {
  const newList = [];
  const listLen = list.length - 1;
  let count = listLen;
  for (let i = 0; i <= listLen; i++) {
    const value = list[count];
    newList.push(value);
    count = count - 1;
  }
  return (newList);
};
