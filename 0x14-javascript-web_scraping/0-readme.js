#!/usr/bin/node

const foo = require('fs');
const bar = process.argv[2];

foo.readFile(bar, 'utf-8', (error, content) => {
  if (error) {
    console.log(error);
  } else {
    console.log(content);
  }
});
