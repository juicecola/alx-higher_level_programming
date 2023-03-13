#!/usr/bin/node

const args = process.argv.slice(2);

const factorial = (n) => {
  if (isNaN(n)) {
    return 1;
  } else if (n === 0) {
    return 1;
  } else {
    return n * factorial(n - 1);
  }
};

const n = parseInt(args[0], 10);

console.log(factorial(n));
