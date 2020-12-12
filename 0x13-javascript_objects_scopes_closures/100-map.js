#!/usr/bin/node
const list = require('./100-data').list;
let map1 = [];
map1 = list.map(function (num1, num2) {
  return num1 * num2;
});
console.log(list);
console.log(map1);
