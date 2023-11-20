# Generalizing the code to generate fibonacci numbers upto n terms
# Initializing the series with first 2 numbers
fibonacci = [0, 1] 

def generate_fibonacci(n):
    if n <= 0:
        print("Incorrect input")
    else:
        while len(fibonacci) < n:
            next_number = fibonacci[-1] + fibonacci[-2]
            # Next sumber is the sum of last 2 numbers in the list 
            fibonacci.append(next_number)
            # Appending the last number to the list
    return fibonacci

      
