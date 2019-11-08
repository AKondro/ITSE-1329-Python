#chatbot-phase2-amykondro.py

#set counter of number of greetings to 0
#set the variable to yes to run the while statement
count = 0 
a_greeting = 'yes' 

#loop through the inputs until the users answer is no longer yes, which stops the loop
while a_greeting == 'yes': 
        first_name = input('What is your first name? ')
        last_name = input('What is your last name? ')
        last_initial = last_name[0:1]
        #Asks the user time of day
        time_of_day = input('What time of day is it (Morining,Afternoon,Evening)? ')
        if time_of_day == 'Morning':
            print('Have a good breakfast,',first_name,last_initial)
        elif time_of_day == 'Afternoon':
            print('Have a good lunch,',first_name,last_initial)
        elif time_of_day == 'Evening':
            print('Have a good dinner, ',first_name,last_initial)
        else:
            #user types a different time of day than ones listed it prints this output
            print('Have a good one',first_name,last_initial)
        count=count+1
        #if user responds with yes, it goes through the loop again, if answered no the loop stops
        a_greeting = input('Would you like another greeting? ')
    #prints number of times the greeting ran
print('Total number of greetings:' , count)