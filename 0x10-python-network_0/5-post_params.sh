#!/bin/bash
# script to send a post request with data to a url
curl -sX POST --data-raw "email:test@gmail.com&subject=I%20will%20always%20be%20here%20for%20PLD" $1
