#!/bin/bash
# Check if URL argument is provided
# Send GET request using curl and display only the body of a 200 status code response

if [ $# -ne 1 ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi
curl -s -o /dev/null -w "%{http_code}" "$1" | grep -q "200"
if [ $? -eq 0 ]; then
    curl -s "$1"
fi
