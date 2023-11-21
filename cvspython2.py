# Calculating the factorial using recursion function

import timeit


def factorial(n):
    if n <= 1:
        return 1
    else:
        return n * factorial(n - 1)


num = int(input(" Enter a non-negative integer : "))

start_time = timeit.default_timer()  
fact = factorial(num)
elapsed_time = timeit.default_timer() - start_time  

print(f" The factorial of {num} is {fact}")
print(f" Time taken : {elapsed_time} seconds")
