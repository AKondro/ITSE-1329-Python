#chatbot-phase3-amykondro.py

def greeter(first_name, last_name, time_of_day) :
    """Returns a sentence containing first name, last name and the meal depending on the time of day"""
    last_initial = last_name[0:1]
    if time_of_day == 'Morning':
        result = 'Have a good breakfast, '+' '+ first_name +' '+ last_initial
    elif time_of_day == 'Afternoon':
        result = 'Have a good lunch, '+' '+ first_name +' '+ last_initial
    elif time_of_day == 'Evening':
        result = 'Have a good dinner, '+' '+ first_name +' '+ last_initial
    return(result)
count = 0 
a_greeting = 'yes'
#run the following loop until user doesn't want another greeting
while a_greeting == 'yes': 
    #inputs for first name, last name and time of day
        first_name = input('What is your first name? ')
        last_name = input('What is your last name? ')
        time_of_day = input('What time of day is it (Morining, Afternoon, Evening)? ')
    #calls the greeter function to get the result back
        sentence = greeter(first_name, last_name, time_of_day)
    #prints the results from the greeter function
        print(sentence)
        count=count+1
        a_greeting = input('Would you like another greeting? ')
print('You received' ,count, 'greetings')