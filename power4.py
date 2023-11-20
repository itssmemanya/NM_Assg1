# Using the append method

X=5
L = [2 ** i for i in range(10)] 

if 2 ** X in L:
    print(' Found at index : ', L.index(2 ** X))
else:
    print(X, ' was not found here ')
