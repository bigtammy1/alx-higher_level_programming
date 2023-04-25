#!/usr/bin/node
const request = require('request');
const myargs = process.argv.slice(2);

request(myargs[0], (err, response, body) => {
  if (err) { return console.log(`code: ${response.statusCode}`); } else {
    console.log(`code: ${response.statusCode}`);
  }
});
