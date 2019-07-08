print ("Hello, World!")
print ("It's going to rain on Saturday.")

print ("\n")

print ("these\nare\non\nseparate\nlines")
print ("tab over\tto here")

print ("\n")

print ("Team\t\tWon\tLost\nLeafs\t\t1\t1\nSabres\t\t0\t2")

print ("\n")

print ("%s scored %d and completed %.1f of the quest" % ('Sloan', 15, 55))
print ("%20s%20d" % ('Sloan', 15))
print ("%-20s%20d" % ('Sloan', 15))

print ("\n")

print ("%-10s%10s%10s\n%-10s%10d%10d\n%-10s%10d%10d" % ('Team', 'Won', 'Lost', 'Leafs',1,1, 'Sabers',0,2))

print ("\n")

formatter="%-10s%10s%10s\n"
header=formatter % ('Team', 'Won', 'Lost')
leafs=formatter % ('Leafs', 1, 1)
sabres=formatter % ('Sabres', 0, 2)

print ("\n")

print ("%s%s%s" % (header, leafs, sabres))
table = "%s%s%s" % (header, leafs, sabres)
'Team Won Lost\nLeafs1 1\nSabres 0 2\n'
print (table)

print ("\n")

print ("This program will take two strings and decide which one is greater")
tup = None
first = raw_input("First string: ")
second = raw_input("Second string: ")

if first > second:
    tup = (first, second)
elif second > first:
    tup = (second, first)

if tup !=  None:
    print ("%s is greater than %s") % tup
else:
    print ("The strings were equal")
