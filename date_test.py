from datetime import datetime, date
from calendar import monthrange


def what_day_is_it(date):
    days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
    day = date.weekday()
    return days[day]

### 현재 년월 일 계산
current_year = datetime.now().year
current_month = datetime.now().month
current_day = datetime.now().day
monthrange = monthrange(current_year,current_month)
start_day = monthrange[0]
end_day = monthrange[1]

for i in range(start_day, end_day+1):
    # print(i)
    if what_day_is_it(date(current_year, current_month, i)) == "Fri" \
        or what_day_is_it(date(current_year, current_month, i))=='Sat'\
        or what_day_is_it(date(current_year, current_month, i))=='Sun':
        print(str(i) + "=holyday")








