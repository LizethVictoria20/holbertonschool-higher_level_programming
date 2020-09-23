#!/usr/bin/node
const request = require('request');
const fs = require('fs');
const url = process.argv[2];
const options = {
  url: url,
  headers: {
    'User-Agent': 'request'
  }
};

function callback(error, response, body) {
  if (!error && response.statusCode === 200) {
    fs.writeFile(process.argv[3], body, 'utf-8', (err) => {
      if (err) {
        console.log(err);
      }
    });
  }
}
request(options, callback);
