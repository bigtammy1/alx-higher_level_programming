#!/usr/bin/node
const logs = [0];
exports.logMe = function (item) {
  console.log(`${logs[logs.length - 1]}: ${item}`);
  logs.push(logs[logs.length - 1] + 1);
};
