#!/usr/local/bin/node
const myArgs = process.argv[2];
const num = parseInt(myArgs);

if (isNaN(myArgs)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < num; i++) {
    let print = '';
    for (let j = 0; j < num; j++) {
      print += 'X';
    }
    console.log(print);
  }
}
