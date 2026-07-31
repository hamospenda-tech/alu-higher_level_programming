#!/bin/bash
# Sends a GET request with header X-HolbertonSchool-User-Id: 98 and displays the body
curl -s -H "X-HolbertonSchool-User-Id: 98" "$1"
