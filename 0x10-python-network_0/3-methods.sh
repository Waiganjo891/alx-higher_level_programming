#!/bin/bash
# Check if URL argument is provided
# Send OPTIONS request using curl to fetch allowed HTTP methods
# Display the allowed HTTP methods

if [ $# -ne 1 ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi
allowed_methods=$(curl -s -I -X OPTIONS "$1" | awk '/Allow/{print $2}')
echo "$allowed_methods"
