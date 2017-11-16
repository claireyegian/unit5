#Claire Yegian
#11/15/17
#displayDate.py - displays current date

from datetime import date

today = date.today()
day = today.day
month = today.month
year = today.year
week = today.weekday()

months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
weekDays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

monthToday = months[month-1]
weekDay = weekDays[week]

print('Today is '+weekDay+', '+monthToday+' '+str(day)+' '+str(year))
