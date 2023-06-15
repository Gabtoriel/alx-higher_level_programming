#!/usr/bin/node

const argv = process.argv;

function add(a, b) {
  if (isNaN(a) === true || isNaN(b) === true) {
    console.log(NaN);
  } else {
    const total = a + b;
    console.log(total);
  }
}

add(parseInt(argv[2]), parseInt(argv[3]));
