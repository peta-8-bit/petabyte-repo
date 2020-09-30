'''#chapter-4:Picture grid problem
grid = [['.', '.', '.', '.', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['.', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]

for i in range(6):
    row=''
    for j in range(9):
        row+=str(grid[j][i])
    print(row)

'''
'''
#Chapter-4:Coin flip problem

import random
numberOfStreaks = 0
s=''
y=0
x=[]
for experimentNumber in range(10000):
    for i in range(100):
        s+=(str(random.randint(0,1)))
    x.append(s)
    x[experimentNumber]=x[experimentNumber].replace('000000','h')
    x[experimentNumber]=x[experimentNumber].replace('111111','t')
    y+=x[experimentNumber].count('h')+x[experimentNumber].count('t')
print("Chance of streak: ",y/100)   
'''

'''
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
'''