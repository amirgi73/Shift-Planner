from khayyam import JalaliDate
from datetime import timedelta
import csv


def __return_jalali(date: str):
    return JalaliDate(*date.split('-'))


def daycounter(start, end):
    holidays = []
    with open('f.csv') as f:
        reader = csv.reader(f)
        next(reader)
        for line in reader:
            date = __return_jalali(line[4])
            if start <= date <= end:
                if line[2] == '1':
                    holidays.append(date)
            elif date > end:
                break

    now = start
    while now <= end:
        if now.strftime('%a') == 'ج':
            if now not in holidays:
                holidays.append(now)
        now += timedelta(days=1)
    pre_holidays = []
    for day in holidays:
        yesterday = day - timedelta(days=1)
        if yesterday >= start and yesterday not in holidays:
            pre_holidays.append(yesterday)
    # using set to remove duplicates and then sorting them again:
    return {'holidays': sorted(set(holidays)), 'pre holidays': sorted(set(pre_holidays))}


