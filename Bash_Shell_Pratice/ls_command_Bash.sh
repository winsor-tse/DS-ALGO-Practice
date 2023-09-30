#!/bin/bash

#running commands using variables
variable2=$(ls -la)
#create a new file here and acho it into the new file
echo "$variable2" > newfile.txt
#sleep for 5 seconds
sleep 5
#remove the file
#grep for a file called ls
#open file for 