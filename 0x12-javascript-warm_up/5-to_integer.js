#!/usr/bin/node
const myArgs = process.argv[2];

if (isNaN(myArgs)) {
  console.log('Not a number');
} else {
  console.log('My number: ' + myArgs);
}
