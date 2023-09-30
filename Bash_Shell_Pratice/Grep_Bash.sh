#!/bin/bash

# Pass in the file name you want to grep
file="$1"
pattern="$2"
Delete_after="$3"

#goes through each line and regex for a pattern
if grep -q "$pattern" "$file"; then
    echo "Pattern '$pattern' found in '$file'."
else
    echo "Pattern '$pattern' not found in '$file'."
fi
#if the variable is True then remove the file
if $Delete_after eq "True"; then
    rm -rf $file
else
    exit 1
fi
#grep command