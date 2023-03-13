#!/usr/bin/node

const args = process.argv[2];

const num = parseInt(args, 10);

if (!isNaN(num)) {
  console.log('My number: ', args);
} else {
  console.log('Not a number');
}
