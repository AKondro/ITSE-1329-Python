try:
    hours = input('enter your hours: ')
    rate = input('enter your rate: ')
    hours_float = float(hours)
    rate_float = float(rate)

    if hours_float > 40 :
        oth = hours_float - 40
        otr = oth * (rate_float * 1.5)
        pay = otr + (40 * rate_float)

    else:
        pay = (hours_float * rate_float)
    print('Pay:',pay)
except:
    print('Error, pleaase enter numeric input')
    quit()