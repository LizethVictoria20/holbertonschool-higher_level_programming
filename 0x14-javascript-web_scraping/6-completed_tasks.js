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
    const result = {};
    for (let i = 0; i < info.length; i++) {
      if (info[i].completed) {
        if (!(info[i].userId in result)) {
          result[info[i].userId] = 0;
        }
        result[info[i].userId] += 1;
      }
    }
    console.log(result);
  }
}
request(options, callback);
