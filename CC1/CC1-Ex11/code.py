# DO NOT TOUCH ====================================================================
def random_joke():
    from random import randint
    jokes = [
       'Did you hear about the restaurant on the moon?  Great food, no atmosphere',
       'What do you call a fake noodle? An Impasta!',
       'Want to hear a joke about paper? Nevermind, its tearable',
       'How does a penguin build its house? Igloos it together.'
   ]
    joke = jokes[randint(0, 3)]
    return joke
# DO NOT TOUCH ====================================================================

response = input('Would you like to hear a joke?')
   
# Fill out vvvvvvvvvvvvvvvvvvvvv

if response[0] == 'y': # fill in blank to get first letter of the response variable

# Fill out ^^^^^^^^^^^^^^^^^^^^^

    print(random_joke())
else:
    print('Thank you, have a nice day!')