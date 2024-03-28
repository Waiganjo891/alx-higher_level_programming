#!/bin/bash
# Check if URL argument is provided
# Send DELETE request using curl and display the body of the response

if [ $# -ne 1 ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi

curl -X DELETE -s "$1"
