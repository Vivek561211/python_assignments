#program for calculating age
from datetime import date

today = date.today()
print(today)

def calculate_age(bdate):
    age=today.year-bdate.year-((today.month,today.day)<(bdate.month,bdate.day))
    return age
print(calculate_age(date(2004,8,26)))

