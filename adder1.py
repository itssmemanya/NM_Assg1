# Defining the adder function to add two numbers
def adder(a, b):
    return a + b


# Calling the function 
adder_string = adder("Manya ", "Arora")
adder_list = adder([1, 2, 3], [4, 5, 6])
adder_float = adder(3.1415, 2.7182)

# Print the results
print(" Adding strings :", adder_string)
print(" Adding lists : ", adder_list)
print(" Adding floats : ", adder_float)
