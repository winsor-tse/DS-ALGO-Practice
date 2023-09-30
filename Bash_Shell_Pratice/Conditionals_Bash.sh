#!/bin/bash

# Prompt the user to enter their age

#-eq: Equal to
#-ne: Not equal to
#-lt: Less than
#-le: Less than or equal to
#-gt: Greater than
#-ge: Greater than or equal to

echo "Please enter your age:"

# Read the user's input into a variable
# The read command is used to capture the user's input and store it in the age variable.
read age

# The if statement checks if the value of age is greater than or equal to 18 using the -ge operator. If this condition is true, it prints a message 
if [ "$age" -ge 18 ]; then
    echo "You are old enough to vote."
else
    echo "You are not old enough to vote yet."
# The fi keyword marks the end of the if statement.
fi

