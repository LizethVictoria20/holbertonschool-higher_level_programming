#!/usr/bin/node
const request = require('request');
const url = process.argv[2];
const options = {
  url: url,
  headers: {
    'User-Agent': 'request'
  }
};

function callback (error, response, body) {
  if (!error && response.statusCode === 200) {
    const info = JSON.parse(body);
    let count = 0;
    for (let i = 0; i < info.results.length; i++) {
      const allcharacters = info.results[i].characters;
      const url = 'https://swapi-api.hbtn.io/api/people/18/';
      for (let j = 0; j < allcharacters.length; j++) {
        if (url == allcharacters[j]) {
          count += 1;
        }
      }
    }
    console.log(count);
  }
}
request(options, callback);
