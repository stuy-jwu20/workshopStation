#Jonathan Wu
#SoftDev
#K01 -- printingNames/Python/The goal was to print a SoftDev student name from period1 and period2 written in Python.
#2021-09-22

import random
#Lists of period 1 and 2
pd1 = ['Owen Yaggy', 'Haotain Gan', 'Ishraq Mahid', 'Julia Nelson', 'Ivan Lam',
       'Michelle Lo', 'Christopher Liu', 'Michael Borzuk', 'Ivan Mijacika',
       'Lucas Lee', 'Rayat Roy', 'Emma Buller', 'Andrew Juang',
       'Renggeng Zheng', 'Angela Zhang', 'Alejandro Alonso', 'Deven Mahehwari',
       'Hebe Huang', 'Aryaman Goenka', 'Oscar Wang', 'Tami Takada', 'Yusuf Elsharawy',
       'Ella Krechmer', 'Tomas Acuna', 'Tina Nguyen', 'Sadid Ethun', 'Shyne Choi',
       'Shriya Anand', 'Lucas Tom-Wong', 'Theo Fahey', 'Sean Ging', 'Gavin']
pd2 = ['Patrick Ging', 'Raymond Yeung', 'Josephine Lee', 'Alif Abdullah',
       'William Chen', 'Justin Zou', 'Andy Lin', 'Rachel Xiao', 'Yuqing Wu',
       'Shadman Rakib', 'Liesel Wong', 'Daniel Sooknanan', 'Cameron Nelson',
       'Austin Ngan', 'Thomas Yu', 'Yaying Liang Li', 'Jesse Xie', 'Eric Guo',
       'Jonathan Wu', 'Zhaoyu Lin', 'Joshua Kloepfer', 'Noakai Aronesty',
       'Yoonah Chang', 'David', 'Wen Hao Dong', 'Mark Zhu', 'Qina Liu',
       'Kevin Cao', 'Sophie Liu', 'Annabel Zhang', 'Roshani Shrestha', 'Han Zhang']

#Random function to pick a random person in the class
a = random.randint(0,32)
b = random.randint(0,32)

#Prints the list indices corresponding to the random number 
print("pd1: " + pd1[a])
print("pd2: " + pd2[b])
