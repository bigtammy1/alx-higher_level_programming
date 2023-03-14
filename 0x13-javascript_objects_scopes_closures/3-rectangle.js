#!/usr/bin/node
module.exports = class Rectangle {
  constructor (w, h) {
    if ((w !== 0 && w > 0) && (h !== 0 && h > 0)) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    let symbol = 'X';
    for (let i = 0; i < this.height; i++) {
      for (let j = 1; j < this.width; j++) {
        symbol = symbol.concat('X');
      }
      console.log(symbol);
      symbol = 'X';
    }
  }
};
