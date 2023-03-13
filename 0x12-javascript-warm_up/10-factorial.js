#!/usr/bin/node
function fact (num = 1) {
  if (num === 0) {
    return 1;
  }
  if (isNaN(num)) {
    return 1;
  }
  return num * fact(num - 1);
}

const num = parseInt(process.argv[2]);
console.log(fact(num));
