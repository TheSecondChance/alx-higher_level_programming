#!/usr/bin/node
const request = require('request');
const url = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];
request(url, function (error, response, body) {
  if (!error) {
    const char = JSON.parse(body).characters;
    charOutPut(char, 0);
  }
});

function charOutPut (char, index) {
  request(char[index], function (error, response, body) {
    if (!error) {
      console.log(JSON.parse(body).name);
      if (index + 1 < char.length) {
        charOutPut(char, index + 1);
      }
    }
  });
}
