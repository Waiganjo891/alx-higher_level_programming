#!/bin/bash
# Check if a URL is provided
# Send request using curl and get the size of the response body in bytes
# Display the size of the response body

if [ $# -ne 1 ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi
response_size=$(curl -s -o /dev/null -w "%{size_download}" "$1")
echo "$response_size"
