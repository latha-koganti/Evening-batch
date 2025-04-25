#not operator
battery_percentage = int(input('Enter your battery percentage: '))

if not battery_percentage>20:
    #not False=>True
    print('Low battery')
