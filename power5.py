# Taking 2**x outside the loop to improve the performance of the code 

import timeit

#method1
X = 5
L = [2 ** i for i in range(10)]

start_time1 = timeit.default_timer()  
if 2 ** X in L:
    print(' Element was found at index : ', L.index(2 ** X))
else:
    print(X, ' was not found in list ')
elapsed_time1 = timeit.default_timer() - start_time1  
print(f" The time taken to find index without 2^X outside the loop : {elapsed_time1} seconds")

#method2
value = 2**X
start_time2 = timeit.default_timer()  
if value in L:
    print(' Element was found at index', L.index(value))
else:
    print(X, ' was not found in list ')
elapsed_time2 = timeit.default_timer() - start_time2  
print(f" The time taken to find the index with 2^5 outside the loop : {elapsed_time2} seconds")
difference=elapsed_time2-elapsed_time1
print(f" The difference in time of calculation is : {difference} seconds")

