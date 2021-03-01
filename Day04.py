# Day03
# Given an integer n, print its first 10 multiples. Each multiple n x i (where 1 <= i <= 10) should be printed on a new line in the form: n x i = result.
# Constraints 2 <= n <= 20
# The code starts here:
n = int (input())
for i in range (1,11):
    x = n*i
    print (n, "x", i, "=", x)


  