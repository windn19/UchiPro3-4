import datetime

MONTHS = {1: 'Январь',
          2: 'Февраль',
          3: 'Март',
          4: 'Апрель',
          5: 'Май',
          6: 'Июнь',
          7: 'Июль',
          8: 'Август',
          9: 'Сентябрь',
          10: 'Октябрь',
          11: 'Ноябрь',
          12: 'Декабрь'}

year = int(input())
now_date = datetime.date(year, 1, 1)
result = {}
while now_date.year == year:
    if now_date.day == 13 and now_date.isoweekday() == 5:
        result[now_date.month] = now_date.strftime('%d.%m.%Y')
    now_date += datetime.timedelta(days=1)
for month in range(1, 13):
    if month in result:
        print(f'{MONTHS[month]}: {result[month]}')
    else:
        print(f'{MONTHS[month]}: нет дней выпадающих на пятницу 13-е')
