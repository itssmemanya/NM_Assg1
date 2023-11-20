S='mumbai'
# Using list method
unicode1 = []
for i in S:
    unicode1.append(ord(i))
print(" Using list methods : ", unicode1)

# Using List comprehension
unicode2 = [ord(x) for x in S]
print(" Using list comprehension : ", unicode2)

# Using map() function
unicode3 = map(lambda x: ord(x), S)
print(" Using map function : ", list(unicode3))
