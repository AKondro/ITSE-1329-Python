file_name = input('Enter file: ')
handle = open(file_name)

counts = dict()
for line in handle:
    if line.startswith('From '):
         words = line.split()
         email = words[1]
         pieces = email.split('@')
         domain = pieces[1]
         counts[domain] = counts.get(domain, 0) + 1
        
print(counts)