from ctypes import *
import timeit

fact = CDLL("./factorial.so")

n = int(input(" Enter a non-negative integer : "))

start_time = timeit.default_timer()
fact.factorial(n)
elapsed_time = timeit.default_timer() - start_time

print(f" Factorial of ", n, ": ", result)
print(f" Time taken : {elapsed_time} seconds")
