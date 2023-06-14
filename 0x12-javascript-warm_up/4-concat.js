#!/usr/bin/node

const argv = process.argv;

if (argv.length < 3) {
  console.log('undefined is undefined');
} else if (argv.length === 3) {
  console.log(argv[2] + ' ' + 'is undefined');
} else if (argv.length === 4) {
  console.log(argv[2] + ' ' + 'is' + ' ' + argv[3]);
} else {
  console.log('undefined is undefined');
}
