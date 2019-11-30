name = input('Enter file: ')
handle = open(name)

counts = dict()
for line in handle:
    if line.startswith('From '):
        words = line.split()
        day = words[2]
        counts[day] = counts.get(day, 0) + 1
        
print(counts)