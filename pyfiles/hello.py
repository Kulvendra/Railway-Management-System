import datetime 
import calendar
date='2019-09-09'
b = datetime.datetime.strptime(date, '%Y-%M-%d').weekday() 
btf= (calendar.day_name[b]) 
print(btf)