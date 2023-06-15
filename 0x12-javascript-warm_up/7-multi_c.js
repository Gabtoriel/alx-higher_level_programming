#!/usr/bin/node

const argv = process.argv;
const counts = parseInt(argv[2]);

if (isNaN(counts) === true) {
  console.log('Missing number of occurences');
} else {
  for (let i = 0; i < counts; i++) {
    console.log('C is fun');
  }
}
