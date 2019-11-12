#   open mbox-short.txt, print lines that startwith
#   From: and print out result with right-hand whitespace
#   removed
fhand = open("mbox-short.txt")
for line in fhand:
    line = line.rstrip()
    if line.startwith('From:') :
        print(line)