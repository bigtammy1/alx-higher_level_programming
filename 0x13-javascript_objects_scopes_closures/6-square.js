#!/usr/bin/node
const Rectangle = require('./5-square');

module.exports = class Squares extends Rectangle {
  charPrint (c = 'X') {
    let symbol = c;
    for (let i = 0; i < this.height; i++) {
      for (let j = 1; j < this.width; j++) {
        symbol = symbol.concat(c);
      }
      console.log(symbol);
      symbol = c;
    }
  }
};
