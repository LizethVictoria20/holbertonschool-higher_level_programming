#!/usr/bin/node
const request = require('request');
const id = process.argv[2];
const options = {
  url: 'https://swapi-api.hbtn.io/api/films/' + id,
  headers: {
    'User-Agent': 'request'
  }
};

function callback (error, response, body) {
  if (!error && response.statusCode === 200) {
    const info = JSON.parse(body);
    const allCharacters = info.characters;
    for (let i = 0; i < allCharacters.length; i++) {
      request(allCharacters[i], (err, response, body) => {
        if (!err && response.statusCode === 200) {
          const character = JSON.parse(body);
          console.log(character.name);
        }
      });
    }
  }
}
request(options, callback);
