#!/usr/bin/node

const request = require('request');
const movieId = process.argv[2];
const apiBaseUrl = 'https://swapi.dev/api/';
function fetchCharacters (movieId, callback) {
  const url = `${apiBaseUrl}films/${movieId}/`;
  request(url, { json: true }, (error, response, body) => {
    if (error) {
      console.error('Error fetching movie data:', error);
      return;
    }
    if (response.statusCode !== 200) {
      console.error('Error fetching movie data:', response.statusCode);
      return;
    }
    const characterUrls = body.characters;
    characterUrls.forEach(characterUrl => {
      request(characterUrl, { json: true }, (error, response, body) => {
        if (error) {
          console.error('Error fetching character data:', error);
          return;
        }
        if (response.statusCode !== 200) {
          console.error('Error fetching character data:', response.statusCode);
          return;
        }
        console.log(body.name);
      });
    });
  });
}
fetchCharacters(movieId);
