#!/usr/bin/node
const myArgs = process.argv[2];

const num = parseInt(myArgs);
if (myArgs === undefined) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < num; i++) {
    console.log('C is fun');
  }
}
