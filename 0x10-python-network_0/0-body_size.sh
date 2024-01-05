#!/bin/bash
# script that checks the body
curl -sI $1 | grep "Content-Length:" | cut -d' ' -f2
