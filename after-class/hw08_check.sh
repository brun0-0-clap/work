#!/bin/bash
if [ -f "$1" ]; then
    echo "File $1 exists."
else
    echo "File $1 does NOT exist."
fi
