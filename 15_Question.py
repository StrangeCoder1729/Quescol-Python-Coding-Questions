#Q15). Write a program in Python to find given number is perfect or not?


def perfect(num):
    add = 0
    for i in range(1,num):
        if(num % i == 0):
            add += i
    if(add == num):
        print("It is a perfect number !!!")
    else:
        print("It is not a perfect number !!!")


num = int(input("Enter number : "))
perfect(num)