#!/usr/bin/node

const args = process.argv.slice(2);

const add = (a, b) => {
  return a + b;
};

const a = parseInt(args[0], 10);
const b = parseInt(args[1], 10);

if (isNaN(a) || isNaN(b)) {
  console.log('Invalid input. Please enter two integers.');
} else {
  console.log(add(a, b));
}
