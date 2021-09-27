#Jonathan Wu 
#SoftDev
#K05 -- amalgamation/Python/The goal was to take a piece from our groupmates to refactor and make an efficient code.
#2021-09-26

#Pow-Wow: I reached out to my partners Andy Lin & Wen Hao Dong and we talked about trying to amalgamate our code together.
#Discoveries: A few of the names in the list were wrong so we had to swap them around to they were accurate.
#Questions: Would it be more efficient to use lists to store the names or reading it from a text file?
#Comments: Figuring out who's code to amalgamate was rather fun, I suppose. Everyone has different ways to approach problems.

#Start of Code
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
       'Yoonah Chang', 'David Chong', 'Wen Hao Dong', 'Mark Zhu', 'Qina Liu',
       'Kevin Cao', 'Sophie Liu', 'Annabel Zhang', 'Roshani Shrestha', 'Han Zhang']

#Either gets an index for a student or prints a random one.
inputVal = input("Input a number (0-31 inclusive) for a student, or enter/anything else for a random ")
if inputVal.isnumeric() and int(inputVal) >= 0 and int(inputVal) <= 31:
    print("pd1: " + pd1[int(inputVal)])
    print("pd2: " + pd2[int(inputVal)])
else:
#If no input, then it generates a number from [0-32) and prints a student from that random index.
    a = random.randint(0,32)
    b = random.randint(0,32)
    print("pd1: " + pd1[a])
    print("pd2: " + pd2[b])
