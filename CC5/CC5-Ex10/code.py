input('Enter file name: ')
fhand = open("romeo.txt")
texts =[]
for record in fhand:
  slist = record.split(" ")
  for text in slist:
    text= text.strip()
    if text not in texts:
      texts.append(text)
texts.sort()
print(texts)