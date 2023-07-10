#!/bin/bash
# script to retrieve all the http methods allowed by a server
curl -sI -X OPTIONS "$1" | grep -i "Allow:" | cut -d " " -f 2
