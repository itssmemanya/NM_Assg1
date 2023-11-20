#  Using fibonacci2.py to claculate first 100 fibonacci numbers

from fibonacci2 import generate_fibonacci
import timeit

start_time = timeit.default_timer() 
fibonacci = generate_fibonacci(100)
time = timeit.default_timer() - start_time  

print(" \n First 100 Fibonacci numbers : \n ")

# Printing 100 numbers nicely
i=0
while i<len(fibonacci) :
      print("\t",fibonacci[i],end='')
      if i%10==0 :
          print("\n")
      elif i>60 :
          if i%5==0 :
              print("\n")
      i+=1
# Time taken
print(" \n\n Time taken to generate 10\t 0 Fibonacci numbers : ",time," seconds")
