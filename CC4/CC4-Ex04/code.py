with open('mbox-short.txt', 'r') as file:
    count = 0
    for line in file:
        count += 1  # this same as count = count + 1

print(count)
