# Modifying the function 

def adder_keyword(good=1, bad=2, ugly=3):
    return good + bad + ugly


# Calling the function with specified keyword arguments
result_keyword = adder_keyword(ugly=1, good=5)
print(" Adding keywords result : ", result_keyword)
