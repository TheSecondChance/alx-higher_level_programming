#!/usr/bin/node
const reques = require('request');
const id = process.argv[2];
const url = 'https://swapi-api.hbtn.io/api/films/';
reques.get(url + id, function (error, response, body) {
  if (error) {
    console.log(error);
  }  
  const data = JSON.parse(body);
  const dataChar = data.characters;
  for (const i of dataChar) {
    reques.get(i, function (error, response, bodyOne) {
      if (error) {
        console.log(error);
      }
      const dataOne = JSON.parse(bodyOne);
      console.log(dataOne.name);
    });
  }
});
