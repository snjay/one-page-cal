from calendar import Calendar, day_abbr, month_abbr, weekday
from collections import defaultdict
import time
import sys

# Read command-line arguments
try:
    year = int(sys.argv[1])
except IndexError:
    # No year specified.
    # Default to current year
    curr_time = time.localtime(time.time())
    year = curr_time.tm_year
except ValueError:
    sys.stderr.write(f"Error! {sys.argv[1]} is not a valid year.\n")
    sys.stderr.write(f"Usage:\tpython {sys.argv[0]} [YEAR]\n")
    sys.exit(1)

# Init a bucket which maps day to 
# the month w/ the first day
firstday2month = defaultdict(list)
# Find the day of every month's 1st.
c = Calendar()
for month in range(1, len(month_abbr)):
    # Place the month into the day bucket
    # e.g. if the Feb 1st falls on a Saturday
    # then place Feb into the Sat bucket
    day = weekday(year, month, 1)
    firstday2month[day].append(month)
             
# Calculate the left padding
# for printing the day grid below
max_months = max([len(m) for m in firstday2month.values()])
lpad = (3 * max_months) + 2

# Print out year number
print(str(year).center(39))

# Print out day numbers
for i in range(1, 32):
    print(f"{''.ljust(lpad+1, ' ')}", end=' ') if i % 7 == 1 else None
    print(f"{str(i).rjust(3, ' ')}", end=' ')
    print() if i % 7 == 0 else None
print()

# Print horizontal sep of dashes
print(''.join([' '.ljust(lpad+1), '┌', '-'*28]))

# Print out months | days
for i in range(len(day_abbr)):
    mx = ' '.join([month_abbr[m] for m in firstday2month[i]])
    print(f"{mx.rjust(lpad, ' ')}", end=' | ')
    for j in range(len(day_abbr)):
        idx = (i+j) % len(day_abbr)
        print(day_abbr[idx], end=' ')
    print()
