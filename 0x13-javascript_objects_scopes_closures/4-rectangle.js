#!/usr/bin/node
/*
 Write a class Rectangle that defines a rectangle:
   You must use the class notation for defining your class
   The constructor must take 2 arguments: w and h
   Initialize the instance attribute width with the value of w
   Initialize the instance attribute height with the value of h
   If w or h is equal to 0 or not a positive integer, create an empty object
   Create an instance method called print() that prints the rectangle usingi
   the character X
   Create an instance method called rotate() that exchanges the width and
   the height of the rectangle
   Create an instance method called double() that multiples the width and
   the height of the rectangle by 2
 */

class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      if (typeof (w) !== 'undefined' && typeof (h) !== 'undefined') {
        this.width = w;
        this.height = h;
      }
    }
  }

  print (w, h) {
    for (let i = 0; i < this.height; i++) {
      let text = '';
      for (let j = 0; j < this.width; j++) {
        text += 'X';
      }
      console.log(text);
    }
  }

 rotate () {
    let newWidth = this.height;
    let newHeight = this.width;

    this.height = newHeight;
    this.width =  newWidth;
  }


  double () {
    const newWidth = this.width * 2;
    const newHeight = this.height * 2;

    this.width = newWidth;
    this.height = newHeight;
  }
}

module.exports = Rectangle;
