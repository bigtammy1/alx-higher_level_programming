#!/usr/bin/node
const myDict = require('./101-data').dict;
const newDict = {};
for (const i in myDict) {
  if (myDict[i] in newDict) {
    newDict[myDict[i]].push(i);
  } else {
    newDict[myDict[i]] = [i];
  }
}
console.log(newDict);
