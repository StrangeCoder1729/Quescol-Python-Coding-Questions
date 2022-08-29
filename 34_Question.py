# Q34). Python Program to check the given year is a leap year or not.

"""
A year is a leap year if the following conditions are satisfied: 

The year is multiple of 400.
The year is multiple of 4 and not multiple of 100.

"""

def year(yr):
    if(yr % 400 == 0):
        if(yr % 100 == 0):
            if(yr % 4 == 0):
                print("It is a leap year !!!")
            else:
                print("It is not a leap year !!!")
        else:
            print("It is a leap year !!!")
    else:
        print("It is not a leap year !!!")
yr = int(input("Enter year : "))
year(yr)