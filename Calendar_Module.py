import calendar
udate = raw_input().rsplit(' ')
print(list(calendar.day_name)[calendar.weekday(int(udate[2]), int(udate[0]),int(udate[1]))].upper())
