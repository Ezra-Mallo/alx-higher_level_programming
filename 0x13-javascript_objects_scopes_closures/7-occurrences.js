#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  let count = 0;
  const myListLen = list.length;
  for (let i = 0; i < myListLen; i++) {
    if (list[i] === searchElement) {
      count++;
    }
  }
  return (count);
};
