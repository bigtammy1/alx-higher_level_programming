#!/usr/bin/node
let [, , ...values] = process.argv;
if (values.length === 0 || values.length === 1) {
  console.log(0);
} else {
  values = values.map(element => {
    return parseInt(element);
  });
  const start = values.findIndex((value) => value === Math.max(...values));
  values.splice(start, 1);
  console.log(Math.max(...values));
}
