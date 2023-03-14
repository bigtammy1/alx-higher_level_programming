#!/usr/bin/node
const fs = require('fs');
const sourceA = process.argv[2];
const sourceB = process.argv[3];
const destination = process.argv[4];

const text1 = fs.readFileSync(sourceA, 'utf-8').trim();
const text2 = fs.readFileSync(sourceB, 'utf-8').trim();
const output = `${text1}\n${text2}\n`;
fs.writeFileSync(destination, `${output.trim()}\n`);
