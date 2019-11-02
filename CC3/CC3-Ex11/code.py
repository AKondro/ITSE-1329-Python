def first_two(string):
    if (len(string) < 2) :
        new_string('String is too short')
    else:
        new_string(string[0:2])
    return(new_string)