# Defining the adder function to add arbitary number of numbers
def adder(*array):
    return sum(array)

# Calling the function 
result = adder(1,1.414,1.732,2,2.236)

# Print the result
print(" Adding numbers : ", result)
