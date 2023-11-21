#Calculating the factorial from scipy library 

from scipy.special import factorial
import timeit

# Input from the user
n = int(input(" Enter a non-negative integer : "))

# Calling the factorial function from SciPy
start_time = timeit.default_timer()
result = factorial(n)
elapsed_time = timeit.default_timer() - start_time 
print(f" Factorial of ", n, ": ", result)
print(f" Time taken : {elapsed_time} seconds")
