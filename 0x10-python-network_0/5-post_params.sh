#!/bin/bash
# script to send a post request with data to a url
curl -s -d "email:test@gmail.com&subject=I will always be here for PLD" -X POST $1
