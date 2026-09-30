import datetime
current_time = datetime.datetime.now()
current_day = current_time.weekday() + 1
print("The current date and time is:", current_time.strftime('%m-%d-%Y %H:%M %p'))
print('Todays day is:', current_time.strftime('%A'), 'which is currently', current_day, 'out of 7 of the days of the week')