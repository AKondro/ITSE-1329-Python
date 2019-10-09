height = input('What is your height in inches? ')
height_int = int(height)

if height_int > 48 :
    print('Welcome aboard, enjoy the ride!')
elif height_int < 48 :
    print('Sorry, you are not tall enough for this ride')
else:
    print('That is not a valid number')