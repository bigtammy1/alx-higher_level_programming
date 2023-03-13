#!/usr/bin/node
exports.callMeMoby = (x, callback) => {
  for (let i = 0; i < x; i++) {
    callback();
  }
};
