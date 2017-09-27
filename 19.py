# Strategy: store the remainder of the months under various conditions
days = {0:31, 1:28, 2:31, 3:30, 4:31, 5:30, 6:31, 7:31, 8:30, 9:31, 10:30, 11:31}

sunday_bloody_sundays = 0

# Get the day of the week on Jan 1 1901
day_of_week = 1
for month in range(12):
    day_of_week += days[month]
    day_of_week = day_of_week % 7

for year in range(1901,2001):
    for month in range(12):
        if day_of_week == 0:
            sunday_bloody_sundays += 1
            print(str(month + 1) + "/" + str(year))
        if month == 1 and ((year % 100 != 0 and year % 4 == 0) or year % 400 == 0):
            day_of_week += 1
        day_of_week += days[month]
        day_of_week = day_of_week % 7
print(sunday_bloody_sundays)
