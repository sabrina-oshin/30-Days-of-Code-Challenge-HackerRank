# Day06
# A single integer, n (the argument to pass to factorial)
# Your submission must contain a recursive function named factorial
# The code starts here:

n = int (input())
val = 1

# Defining a function named factorial
def factorial (val):
    for i in range (1,n+1):
        val = i * val
    print (val)

# Calling the function
factorial (val)