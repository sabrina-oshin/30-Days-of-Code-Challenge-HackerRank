# Day05
# The first line contains an integer, N (the size of our array).\
# The second line contains N space-separated integers that describe array A's elements
# Print the elements of array A in reverse order as a single line of space-separated numbers
# The code starts here:

N = int(input())
A = list(map(int,input().rstrip().split())) [:N]

# For loop for reverese order array element
for i in range(N-1, -1, -1):     
    print(A [i], end = " ")
    