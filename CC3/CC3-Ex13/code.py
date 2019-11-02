def not_string(string):
    if string[:3] == 'not' :
        new = string
    else :
        new = ('not ' + string)
    return(new)