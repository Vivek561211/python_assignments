from datetime import date
from datetime import datetime
import csv
def calculate_age(bdate):
    today = date.today()
    age=today.year-bdate.year-((today.month,today.day)<(bdate.month,bdate.day))
    return age


f1=open("sal.csv","r")

emp = list(csv.reader(f1))
bdate=[]
age=[]
dollar=[]

for i in range(len(emp)):
    print(emp[i][2])
    bdate.append(datetime.strptime(emp[i][2],'%m/%d/%Y').date())



