#!/usr/bin/node
const fs = require('fs');
const myargs = process.argv.slice(2);

fs.writeFile(myargs[0], myargs[1], 'utf-8', (err) => {
  if (err) { console.log(err); }
});
