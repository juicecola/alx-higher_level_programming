#!/usr/bin/node

const request = require('request');
const foo = require('fs');
const url = process.argv[2];
const file = process.argv[3];

request(url, (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    foo.writeFile(file, body, 'utf8', (error) => {
      if (error) {
        console.log(error);
      }
    });
  }
});
