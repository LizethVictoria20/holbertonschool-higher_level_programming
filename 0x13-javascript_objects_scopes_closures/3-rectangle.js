#!/usr/local/bin/node
class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let i = 0; i < this.height; i++) {
      let outp = '';
      for (let j = 0; j < this.width; j++) {
        outp += 'X';
      }
      console.log(outp);
    }
  }
}
module.exports = Rectangle;
