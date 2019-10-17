#Complete code below to count number of letters

fav_word = "supercalifragilisticexpialidocious"

count = 0 
for letter in fav_word :
    if letter == 'i' :
        count = count + 1
print(count)