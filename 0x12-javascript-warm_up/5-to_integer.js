#!/usr/bin/node

const argv = process.argv;

if (argv[2] === undefined) {
  console.log('Not a number');
} else if (isNaN(parseInt(argv[2])) === true) {
  console.log('Not a number');
} else {
  console.log('My Number:' + ' ' + Number(argv[2]));
}
