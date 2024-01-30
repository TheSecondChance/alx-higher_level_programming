#!/usr/bin/node
const request = require('request');

request(process.argv[2], function (err, response, body) {
  if (err == null) {
    const respo = {};
    const json = JSON.parse(body);

    for (let i = 0; i < json.length; i++) {
      if (json[i].completed === true) {
        if (respo[json[i].userId] === undefined) {
          respo[json[i].userId] = 0;
        }
        respo[json[i].userId]++;
      }
    }
    console.log(respo);
  }
});
