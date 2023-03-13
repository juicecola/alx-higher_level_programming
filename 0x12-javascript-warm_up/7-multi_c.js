#!/usr/bin/node

const args = process.argv[2];

const arg = parseInt(args, 10);

if (!isNaN(arg)) {
  for (let i = 0; i <= arg; i++) { console.log('C is fun'); }
} else {
  console.log('Missing number of occurrences');
}
