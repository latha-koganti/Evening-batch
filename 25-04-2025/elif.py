# write a program that print
#speed<40 -safespeed 
#speed<60 - caution
#speed<80 - over speed
#otherwise - speed limit exceed
speed = 20
if speed < 40:
    print('Safe Speed')
elif speed<60:
    print('Caution')
elif speed<80:
    print('Over Speed')
else:
    print('Speed Limit Exceeded')
