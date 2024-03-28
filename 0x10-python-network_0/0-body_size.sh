#!/bin/bash
# Check if a URL is provided

if [ -z "$1" ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi
content_length=$(curl -sI "$1" | grep -i "Content-Length" | awk '{print $2}')
if [ -z "$content_length" ]; then
    echo "Content-Length header not found in the response."
    exit 1
fi
echo "Size of the body: $content_length bytes"
