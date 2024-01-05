#!/bin/bash
# HTTP methods the server
curl -sI -X OPTIONS "$1" | grep 'Allow:' | cut -d ' ' -f2-
