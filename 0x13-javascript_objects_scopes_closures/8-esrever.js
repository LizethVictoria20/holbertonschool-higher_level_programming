#!/usr/bin/node
exports.esrever = function (list) {
  const lastElement = list.length - 1;
  const arr = [];
  for (let i = lastElement; i >= 0; i--) {
    arr.push(list[i]);
  }
  return arr;
};
