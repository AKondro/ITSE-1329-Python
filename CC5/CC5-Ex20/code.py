file_name = input('Enter file: ')
handle = open(file_name)

counts = dict()
for line in handle:
    if line.startswith('From '):
         words = line.split()
         email = words[1]
         counts[email] = counts.get(email, 0) + 1
        
print(counts)

bigcount = None
bigword = None
for word,count in count.items():
    if bigcount is None or count > bigcount:
        bigword = word
        bigcount = count
print(bigword, bigcount)