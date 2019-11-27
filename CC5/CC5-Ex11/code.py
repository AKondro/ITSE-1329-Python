fhand= open("mbox-short.txt")
records = 0
for record in fhand:
  if record.startswith("From "):
    records+=1

print("There are",records,"lines in the file with From as the first word")