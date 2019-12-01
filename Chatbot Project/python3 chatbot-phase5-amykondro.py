#chatbot-phase5-amykondro.py

def greeter(first_name, last_name) :
    """Returns a sentence containing first name, last name and the time of day, that randomly generates"""
    last_initial = last_name[0:1]
    #imports the random module
    import random
    #randomly selects a number between 1 and 24
    time_of_day = random.randint(1, 25)
    print('The current hour is', time_of_day )
    #based on the time of day generated message and returns the correct greeting
    if time_of_day < 5:
        result = 'Have a good night, '+' '+ first_name +' '+ last_initial
    elif time_of_day < 11:
        result = 'Have a good breakfast, '+' '+ first_name +' '+ last_initial
    elif time_of_day < 16:
        result = 'Have a good lunch, '+' '+ first_name +' '+ last_initial
    elif time_of_day < 21:
        result = 'Have a good dinner, '+' '+ first_name +' '+ last_initial
    elif time_of_day < 24:
        result = 'Have a good night, '+' '+ first_name +' '+ last_initial
    return(result)
count = 0 
a_greeting = 'yes'
#creates a dictionary
counts = dict()
#run the following loop until user doesn't want another greeting
while a_greeting == 'yes': 
    #inputs for first name, last name
        first_name = input('What is your first name? ')
        last_name = input('What is your last name? ')
    #calls the greeter function to get the result back
        sentence = greeter(first_name, last_name)
    #prints the results from the greeter function
        print(sentence)
        #to separate each word
        split_time = sentence.split()
        #removes comma at the end of the 4th word
        time = split_time[3].rstrip(',')
        #adds the time of day and counter into the dictionary
        counts[time] = counts.get(time, 0) + 1
        count=count+1
        a_greeting = input('Would you like another greeting? ')
#loop through the dictionary to print the time of day and count
for time, cnt in counts.items():
    print(time, cnt)