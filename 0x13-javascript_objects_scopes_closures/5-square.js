#!/usr/bin/node
class Rectangle {
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

  rotate () {
    [this.width, this.height] = [this.height, this.width];
  }

  double () {
    this.height = this.height * 2;
    this.width = this.width * 2;
  }
}

module.exports = class Square extends Rectangle {
  constructor (s) {
    super(s, s);
  }
};
