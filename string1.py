# Generating Unicide Code Point of each character in a string

S='mumbai'
total=0

for i in S :
    print(" The Unicode code point of letter {0}, is {1}".format(i,ord(i)))
    total+=ord(i)
print(" The sum of these values is : ",total)
