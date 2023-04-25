#!/usr/bin/node
const request = require('request');
const myargs = process.argv.slice(2);

request(`https://swapi-api.hbtn.io/api/films/${myargs[0]}`, (err, response, body) => {
  if (err) { return console.log(err); } else {
    console.log(JSON.parse(body).title);
  }
});
