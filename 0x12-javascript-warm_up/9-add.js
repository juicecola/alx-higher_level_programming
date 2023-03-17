#!/usr/bin/node

const input = process.argv;
const i = parseInt(input[2]);
const j = parseInt(input[3]);

function add (i, j) {
  console.log(i + j);
}
add(i, j);
