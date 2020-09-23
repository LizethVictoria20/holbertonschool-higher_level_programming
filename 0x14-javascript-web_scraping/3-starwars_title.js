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
    console.log(info.title);
  }
}
request(options, callback);
