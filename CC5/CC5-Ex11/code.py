fhand= open("mbox-short.txt")
records = 0
for record in fhand:
  if record.startswith("From "):
    split_record = record.split()
    print(split_record(1))
    records += 1

print("There were",records,"lines in the file with From as the first word")