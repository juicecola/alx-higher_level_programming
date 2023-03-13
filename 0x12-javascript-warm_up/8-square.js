#!/usr/bin/node

const args = process.argv[2];

const arg = parseInt(args, 10);

if (!isNaN(arg)) {
  for (let i = 0; i <= arg; i++) {
    let num = '';
    for (let j = 0; j <= arg; j++) {
      num += 'X';
    }
    console.log(num);
  }
} else {
  console.log('Missing size');
}
