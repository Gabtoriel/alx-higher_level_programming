#!/usr/bin/node

const argv = process.argv;
const counts = parseInt(argv[2]);

if (isNaN(counts) === false) {
  let i = 0;
  while (i < counts) {
    let s = ''
    for (let j = 0; j < counts; j++) {
      s += 'X';
    }
    console.log(s);
    i++;
  }
} else {
  console.log('Missing size');
}
