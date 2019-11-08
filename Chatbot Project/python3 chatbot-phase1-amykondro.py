first_name = input('What is your first name? ')
last_name = input('What is your last name? ')
last_initial = (last_name[0:1])
time_of_day= input('What time of day is it (Morning, Afternoon, Evening): ')
if time_of_day == 'Morning':
    print('Good Morning',first_name,last_initial)
elif time_of_day == 'Afternoon':
    print('Good Afternoon',first_name,last_initial)
elif time_of_day == 'Evening':
    print('Good Evening',first_name,last_initial)