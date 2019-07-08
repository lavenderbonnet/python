print ("This program will take two strings and decide which one is greater")


first = input("First string: ")
second = input("Second string: ")

#print("debug: " , first, second)

tup = None
if first > second:
    tup = (first, second)
elif second > first:
    tup = (second, first)

#print("debug: ", tup)

if tup !=  None:
    print ("%s is greater than %s" % tup)
else:
    print ("The strings were equal")
