grades = [98, 79, 85, 75, 93, 63, 82, 90, 82, 84, 74]

lowest_so_far = 100

for the_num in grades:
    if the_num < lowest_so_far:
        lowest_so_far = the_num

print('Lowest grade is', lowest_so_far)
