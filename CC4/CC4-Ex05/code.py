#   open alice.txt, count the lines, and
#   print out number of lines
with open('alice.txt', 'r') as file:
  count = 0
  for line in file:
    count = count + 1  
print('Line Count:', count)