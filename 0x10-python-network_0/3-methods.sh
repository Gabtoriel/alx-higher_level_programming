#!/bin/bash
# script to retrieve all the http methods allowed by a server
curl -sX OPTIONS $1 | grep Allow: | cut -d " " -f 2
