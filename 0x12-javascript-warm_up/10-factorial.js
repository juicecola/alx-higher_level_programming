#!/usr/bin/node

const input = process.argv;
const i = parseInt(input[2]);

function factorial (i) {
  if (i <= 1) {
    return 1;
  } else {
    return i * factorial(i - 1);
  }
}
if (isNaN(i)) {
  console.log(1);
} else {
  console.log(factorial(i));
}
