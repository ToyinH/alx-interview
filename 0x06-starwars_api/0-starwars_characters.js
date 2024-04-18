#!/usr/bin/node

const request = require('request');


const movieId = process.argv[2];


const movieUrl = `https://swapi-api.alx-tools.com/films/${movieId}/`;

// Make request to fetch movie details
request(movieUrl, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
  } else if (response.statusCode !== 200) {
    console.error('Status Code:', response.statusCode);
  } else {
    const movie = JSON.parse(body);
    // Fetch characters for the movie
    const charactersUrls = movie.characters;
    // Print characters' names
    charactersUrls.forEach(characterUrl => {
      request(characterUrl, (error, response, body) => {
        if (error) {
          console.error('Error:', error);
        } else if (response.statusCode !== 200) {
          console.error('Status Code:', response.statusCode);
        } else {
          const character = JSON.parse(body);
          console.log(character.name);
        }
      });
    });
  }
});