#!/bin/bash
# JSON POST request to a URL
curl -s -d "@$2" -X POST -H 'Content-Type: application/json' "$1"
