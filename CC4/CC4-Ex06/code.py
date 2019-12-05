#   open mbox-short.txt, print lines that startwith
#   From: and print out result with right-hand whitespace
#   removed
fhand = open("mbox-short.txt")
for line in fhand:
    line1 = line.rstrip()
    if line1.startwith('From:') :
        print(line1)