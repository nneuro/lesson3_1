from datetime import date, datetime

# Напечатайте в консоль даты: вчера, сегодня, месяц назад

today = date.today()
date_yesterday = today.replace(day = today.day - 1)
date_month_ago = today.replace(month = today.month -1)
print(today)
print(date_yesterday)
print(date_month_ago)

# Превратите строку "01/01/17 12:10:03.234567" в объект datetime

date_string = '01/01/17 12:10:03.234567'
date_task = datetime.strptime(date_string, '%m/%d/%y %H:%M:%S.%f')
print(date_task)

# %H:%M:%S.%f
#  12:10:03.234567


