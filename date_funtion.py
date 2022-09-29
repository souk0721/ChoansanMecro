from datetime import datetime, date
from calendar import monthrange

### 현재 년월 일 계산
current_year = datetime.now().year
current_month = datetime.now().month
current_day = datetime.now().day
monthrange = monthrange(current_year,current_month)
start_day = monthrange[0]
end_day = monthrange[1]

def what_day_is_it(date):
    days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
    day = date.weekday()
    return days[day]


def holyday_retrun(month):
    date_retrun = []
    for i in range(start_day-1, end_day+1):
        # print(i)
        if what_day_is_it(date(current_year, month, i)) == "Sat" \
            or what_day_is_it(date(current_year, month, i))=='Sun':
            # or what_day_is_it(date(current_year, month, i))=='Fri'\
            # or what_day_is_it(date(current_year, month, i))=='Sun':
            # print(str(date(current_year, month, i)))
            date_retrun.append(str(date(current_year, month, i)))
    return(date_retrun)
    # print(date_retrun)








