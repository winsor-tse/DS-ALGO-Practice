#!/bin/bash

#create new files and folders automatically based on parameters given

#create x amount of files that are txt
$amount="$1"
$type="$2"

# Check if both arguments are provided
if [ -z "$amount" ] || [ -z "$type" ]; then
    echo "Usage: $0 <amount> <file_type>"
    exit 1
fi

# For loop to create files
for ((i = 1; i <= amount; i++)); do
    filename="file_$i.$type"
    touch "$filename"
    echo "Created $filename"
done

