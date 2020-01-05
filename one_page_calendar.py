from calendar import Calendar, day_abbr, month_abbr
from collections import defaultdict
import time

curr_time = time.localtime(time.time())
year = curr_time.tm_year

# Initialise a bucket mapping
# the day to the month w/ the first
# day
firstday2month = defaultdict(list)

c = Calendar()
# Find the date of any given
for month in range(1, len(month_abbr)):
    for week in c.monthdays2calendar(year, month):
        for day_num, day in week:
            # place the month into the day bucket
            # e.g. if the 1st of Feb falls on a Saturday
            # then place Feb into the Sat bucket
            if day_num == 1:
                firstday2month[day].append(month);
                break
                
                

max_months = max([len(m) for m in firstday2month.values()])
lpad = (3 * max_months) + 2

# print out year number
print(str(year).center(39))

# print out day numbers
for i in range(1, 32):
    print(f"{''.ljust(lpad+1, ' ')}", end=' ') if i % 7 == 1 else None
    print(f"{str(i).rjust(3, ' ')}", end=' ')
    print() if i % 7 == 0 else None
print()

vsep = ''.join([' '.ljust(lpad+1), '┌', '-'*28])
print(vsep)

# print out months | days
for i in range(len(day_abbr)):
    mx = ' '.join([month_abbr[m] for m in firstday2month[i]])
    print(f"{mx.rjust(lpad, ' ')}", end=' | ')
    for j in range(len(day_abbr)):
        idx = (i+j) % len(day_abbr)
        print(day_abbr[idx], end=' ')
    print()
