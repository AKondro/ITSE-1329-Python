#   open mbox-short.txt, transform to uppercase
fhand = open("mbox-short.txt")
for line in fhand:
    line = line.upper()
    print(line)