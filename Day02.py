# Day02
# There are  lines of numeric input:
# The first line has a double, meal_cost (the cost of the meal before tax and tip)
# The second line has an integer, tip_percent (the percentage of meal_cost being added as tip)
# The third line has an integer, tax_percent (the percentage of meal_cost  being added as tax)
# Print out the total_cost being rounded
# The code starts here:

# Initializing the variables
meal_cost = float (input())
tip_percent = int (input())
tax_percent = int (input())

# Defining the function
def total_cost ():
    tip = (tip_percent*meal_cost)/100
    tax = (tax_percent*meal_cost)/100
    bill = round (meal_cost + tip + tax)
    print (bill)

# Calling the function
total_cost ()