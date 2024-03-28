#!/bin/bash

# Check if URL argument is provided
if [ $# -ne 1 ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi

# Send DELETE request using curl and display the body of the response
curl -X DELETE -s "$1"
