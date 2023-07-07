#!/usr/bin/bash
# script to get a html page through curl and return the length of the response body
curl -sI $1 | grep "content-length:" | cut -d " " -f 2
