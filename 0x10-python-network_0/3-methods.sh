#!/bin/bash
# script to retrieve all the http methods allowed by a server
curl -X OPTIONS $1
