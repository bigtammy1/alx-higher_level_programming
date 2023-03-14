#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  const occur = list.filter((element) => element === searchElement);
  return occur.length;
};
