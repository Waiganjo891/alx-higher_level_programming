#!/bin/bash
# This script sends a request to a given URL and displays the size of the response body in bytes.
curl -s -w "\n%{size_download}" "$1"
