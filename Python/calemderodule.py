import calendar
date=input().split()
yy=int(date[2])
dd=int(date[1])
mm=int(date[0])
ans=calendar.weekday(yy, mm, dd)
day=['MONDAY','TUESDAY','WEDNESDAY','THURSDAY','FRIDAY','SATURDAY','SUNDAY']
print(day[ans])


