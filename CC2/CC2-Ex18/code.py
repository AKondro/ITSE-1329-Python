rain = [.25, .76, 1.2, 1.1, .03, .97, 2.3]

rain_total = 0.0

# Your code here
for amount in rain:
    rain_total = amount + rain_total
print('The total amount of rain was:', rain_total)
