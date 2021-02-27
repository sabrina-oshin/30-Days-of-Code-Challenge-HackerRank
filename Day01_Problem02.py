# Day01_Problem02
# The first line contains an integer that you must sum with i
# The second line contains a double that you must sum with d
# The third line contains a string that you must concatenate with s
# Print the sum of both integers on the first line, the sum of both doubles (scaled to 1 decimal place) on the second line
# Then the two concatenated strings on the third line
# The code starts here:

# Initialized Values
i = 4
d = 4.0
s = 'HackerRank '

# User Input Values
x = int (input())
y = float (input())
z = str (input())

# Solution
line1 = int (x + i)
line2 = d + y
line3 = s + z

# Output
print (line1)
print (line2)
print (line3)
