# Dividing 1 by 0,1,2,3,4,5

for i in range(0, 6):
    try:
        print("1 /", i, ":", 1/i)
    except ZeroDivisionError:     # To prevent the code from crashing due to zero division error
        print("Indeterminate.")





