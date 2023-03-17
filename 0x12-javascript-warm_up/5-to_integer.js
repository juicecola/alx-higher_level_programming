#!/usr/bin/node

const input = process.argv;

const number = parseInt(input[2]);
if (isNaN(number)) {
  console.log('Not a number');
} else {
  console.log('My number:', number);
}
