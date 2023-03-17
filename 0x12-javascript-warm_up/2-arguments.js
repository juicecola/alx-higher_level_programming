#!/usr/bin/node

const input = process.argv.length;

if (input < 3) {
  console.log('No argument');
} else if (input === 3) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
