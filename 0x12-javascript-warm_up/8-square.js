#!/usr/bin/node
const num = parseInt(process.argv[2]);
let string = 'X';
if (!isNaN(num)) {
  for (let i = 0; i < num; i++) {
    for (let j = 1; j < num; j++) {
      string = string.concat('X');
    }
    console.log(string);
    string = 'X';
  }
} else {
  console.log('Missing size');
}
