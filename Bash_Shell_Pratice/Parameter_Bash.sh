#pass in arguements into the Command before execution
#-lt is less than
#$# is the paramers
if [ $# -lt 1 ]; then
  echo "parameter is not given"
  exit 1
fi

# The first argument provided is stored in the variable 'name'
name="$1"

# Display a greeting message using the provided argument
echo "Parameter is $name"