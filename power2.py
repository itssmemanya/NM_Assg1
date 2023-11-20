L = [1, 2, 4, 8, 16, 32, 64]
X = 5

i = 0
found = False

# Using for else 

for index, val in enumerate(L):
    if 2 ** X == val:
        print(' Found at index ', index)
        break
else:
    print(X, ' not found ')
