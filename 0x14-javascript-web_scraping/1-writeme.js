#!/usr/bin/node

const foo = require('fs');
const bar = process.argv[2];
const foobar = process.argv[3];

foo.writeFile(bar, foobar, 'utf-8', (error) => {
  if (error) {
    console.log(error);
  }
});
