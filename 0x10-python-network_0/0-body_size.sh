#!/bin/bash
#send request to URL with curl n display size f body of response
curl -s -w '{size_download}' -o /dev/null "$1"
