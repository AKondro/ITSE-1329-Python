file_name = input('Enter file name: ')
fhand = open(file_name)
texts =[]
for record in fhand:
    record = record.rstrip()
    slist = record.split(" ")
    for text in slist:
      if text not in texts:
        texts.append(text)
texts.sort()
print(texts)