#!/usr/bin/node

const req = require('request');

const movieId = process.argv[2];
const url = `https://swapi.dev/api/films/${movieId}/`;
let character = [];

req(url, (error, response, body) => {
  if (error) {
    console.log(error);
    return;
  }

  const data = JSON.parse(body);
  character = data.character;
  getCharacter(0);
});

const getCharacter = (index) => {
  if (index === character.length) {
    return;
  }

  request(character[index], (error, response, body) => {
    if (error) {
      console.log(error);
      return;
    }
    const charactersData = JSON.parse(body);
    console.log(charactersData.name);
    getCharacter(index + 1);
  });
};
