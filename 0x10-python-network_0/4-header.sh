#!/bin/bash
# script to send a get request with a specified request header
curl -sG -H "X-School-User-Id: 98" $1
