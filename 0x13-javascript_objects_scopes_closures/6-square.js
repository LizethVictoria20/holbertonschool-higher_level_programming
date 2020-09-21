#!/usr/bin/node
const Square2 = require('./5-square');
class Square extends Square2 {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }
    for (let i = 0; i < this.height; i++) {
      let outp = '';
      for (let j = 0; j < this.width; j++) {
        outp += c;
      }
      console.log(outp);
    }
  }
}

module.exports = Square;
