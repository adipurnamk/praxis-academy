#!/bin/bash
filename=$1
if [ -f "$filename" ]; then 
echo "File exist"
else
echo "File does not exist"
fi

