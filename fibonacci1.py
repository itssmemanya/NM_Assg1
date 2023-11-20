# Calculating first 10 terms of Fibonacci series
# Initializing the series with first 2 numbers
fibonacci = [0, 1] 

while len(fibonacci) < 10:
      next_number = fibonacci[-1] + fibonacci[-2]
      # Next sumber is the sum of last 2 numbers in the list 
      fibonacci.append(next_number)
      # Appending the last number to the list
      
# Printing result
print(fibonacci) 
