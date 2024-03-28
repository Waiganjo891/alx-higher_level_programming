#!/bin/bash
# This script sends a POST request to the specified URL with specific data and headers, then displays the response body.
curl -s -X POST -d "email=test@gmail.com&subject=I will always be here for PLD" -H "Content-Type: application/x-www-form-urlencoded" "$1"
