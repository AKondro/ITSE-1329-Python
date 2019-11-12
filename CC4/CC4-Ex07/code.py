#   open alice.txt, print lines that startwith
#   'Alice' and print out result with right-hand whitespace
#   removed
fhand = open("alice.txt")
for line in fhand:
    line = line.rstrip()
    if line.startwith('alice') :
        print(line)