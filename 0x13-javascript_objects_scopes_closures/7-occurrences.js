#!/usr/bin/node

/*
  Write a function that returns the number of occurrences in a list:
    Prototype: exports.nbOccurences = function (list, searchElement)
*/

exports.nbOccurences = function (list, searchElement) {
  const listLen = list.length;
  let count = 0;

  for (let i = 0; i < listLen; i++) {
    if (list[i] === searchElement) {
      count++;
    }
  }
  return (count);
};
