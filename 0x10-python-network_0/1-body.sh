#!/bin/bash
# This script sends a GET request to a given URL and displays the body of the response if the status code is 200.
curl -s -o /tmp/response_body -w "%{http_code}" "$1" && if [ $(cat /tmp/response_body) -eq 200 ]; then cat /tmp/response_body; fi
