#Chapter-7:Project: Date Detection
import re

date_e=input("enter a string :")
date_t= re.compile(r'([0-2][0-9]|3[0-1]/[0-1][0-2]/[1-2][0-9][0-9][0-9])')
date=date_t.findall(date_e)
month=[]
day=[]
year=[]
flag=0
for i in date:
    month.append(int(i[3:5]))
    day.append(int(i[0:2]))
    year.append(int(i[6:10]))
for i,j in zip(month,day):
    if i==4|6|9|11 and j==31:
        print("Invalid date")
        flag=1
    if i==2 and j>29:
        print("Invalid date")
        flag=1
for i,j in zip(year,day):
    if i%4!=0 and j==29:
        print("Invalid date")
        flag=1
print("\nYou entered : ",date)
if flag==0:
    print("\nValid Date")
