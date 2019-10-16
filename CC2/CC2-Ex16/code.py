grades = [98, 79, 85, 75, 93, 63, 82, 90, 82, 84, 74]

highest_so_far = -1

for the_num in [98, 79, 85, 75, 93, 63, 82, 90,82, 84, 74]:
    if the_num > highest_so_far:
        highest_so_far = the_num
    
print('Highest grade is', highest_so_far)
