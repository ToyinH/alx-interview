#!/usr/bin/node

const request = require('request');

// Function to retrieve characters for a given movie ID
function getMovieCharacters(movieId) {
  return new Promise((resolve, reject) => {
    // Make a request to the Star Wars API to get the movie details
    const movieUrl = `https://swapi.dev/api/films/${movieId}/`;
    request.get(movieUrl, (error, response, body) => {
      if (error) {
        reject(`Error fetching movie details: ${error}`);
        return;
      }

      if (response.statusCode !== 200) {
        reject(`Failed to fetch movie details: ${response.statusCode}`);
        return;
      }

      const movieData = JSON.parse(body);
      const charactersUrls = movieData.characters;
      const charactersPromises = [];

      // Iterate through each character URL to get their details
      charactersUrls.forEach((url) => {
        charactersPromises.push(new Promise((resolveCharacter, rejectCharacter) => {
          request.get(url, (errorCharacter, responseCharacter, bodyCharacter) => {
            if (errorCharacter) {
              rejectCharacter(`Error fetching character details: ${errorCharacter}`);
              return;
            }

            if (responseCharacter.statusCode !== 200) {
              rejectCharacter(`Failed to fetch character details: ${responseCharacter.statusCode}`);
              return;
            }

            const characterData = JSON.parse(bodyCharacter);
            resolveCharacter(characterData.name);
          });
        }));
      });

      Promise.all(charactersPromises)
        .then((characters) => {
          resolve(characters);
        })
        .catch((errorCharacters) => {
          reject(errorCharacters);
        });
    });
  });
}

// Main function
function main() {
  if (process.argv.length !== 3) {
    console.error('Usage: ./script.js <movie_id>');
    process.exit(1);
  }

  const movieId = process.argv[2];

  getMovieCharacters(movieId)
    .then((characters) => {
      characters.forEach((character) => {
        console.log(character);
      });
    })
    .catch((error) => {
      console.error(error);
      process.exit(1);
    });
}

// Execute main function
main();
