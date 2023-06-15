#!/usr/bin/node

const argv = process.argv;
const f = parseInt(argv[2]);

function factorial (f) {
  if (isNaN(f) === true) {
    return 1;
  }
  if (f === 1) {
    return 1;
  } else {
    const total = f * factorial(f - 1);
    return total;
  }
}

console.log(factorial(f));
