#!/usr/local/bin/node
function add (a, b) {
  const myArgs = process.argv[2];
  const num = parseInt(myArgs);

  if (isNaN(num)) {
    console.log('NaN');
  } else {
    const suma = parseInt(a) + parseInt(b);
    console.log(suma);
  }
}
add(process.argv[2], process.argv[3]);
