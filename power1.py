L = [1, 2, 4, 8, 16, 32, 64]
X = 5

i = 0

# Using while else and eliminating flag

while 2 ** X != L[i]:
        i = i+1
else:
    print(' Required element found at ',i)
