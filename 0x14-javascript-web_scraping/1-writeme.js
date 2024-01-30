#!/usr/bin/node
const fs = require('fs');
fs.writeFile(process.argv[2], process.argv[3], error => {
    console.log(process.argv[3])
  if (error) console.log(error);
});
