#!/bin/bash
# Bash script that takes in a URL as an argument, sends a GET request to URL + displays response
curl -sX GET -H "X-School-User-Id: 98" "$1"
