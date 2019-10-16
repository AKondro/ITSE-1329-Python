hours = input('enter your hours: ')
rate = input('enter your rate: ')
hours_float = float(hours)
rate_float = float(rate)

if hours_float > 40 :
    oth = hours_float - 40
    otr = oth * (rate_float * 1.5)
    pay = otr + (hours_float * rate_float)

else:
    pay = (hours_float * rate_float)
print("Pay:",pay)