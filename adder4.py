# Generalizing the function to take an arbitrary number of keyword arguments

def adder_keyword(**keys):
    return sum(keys.values())


# Calling the function with arbitrary keyword arguments
result = adder_keyword(ugly=20, good=40, bad=60, beautiful=80, worse=100)
print(" Adding arbitrary Keywords : ", result)


