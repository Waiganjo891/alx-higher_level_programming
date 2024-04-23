#!/usr/bin/node

const request = require('request');
function printCharacters (movieId) {
  const url = `https://swapi.dev/api/films/${movieId}/`;
  request(url, { json: true }, (err, res, body) => {
    if (err) {
      console.error('Error:', err);
      return;
    }
    if (body.characters) {
      body.characters.forEach(characterUrl => {
        request(characterUrl, { json: true }, (err, res, characterBody) => {
          if (err) {
            console.error('Error:', err);
            return;
          }
          console.log(characterBody.name);
        });
      });
    } else {
      console.error('No characters found for movie ID:', movieId);
    }
  });
}
const movieId = process.argv[2];
printCharacters(movieId);
