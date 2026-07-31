#!/bin/bash
# Sends a GET request to a URL and displays the body only for a 200 status code response
curl -s -L -o /dev/null -w "%{http_code}" "$1" | grep -q 200 && curl -s -L "$1"
