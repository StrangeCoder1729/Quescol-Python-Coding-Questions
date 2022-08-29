# Q30). Python Program to find GCD or HCF of two numbers.

def HCF(num1,num2):
    minimum = 0

    if(num1 > num2):
        minimum = num2
    else:
        minimum = num1

    
    for i in range(1,minimum+1):
        if(num1 % i == 0) and (num2 % i == 0):
            print(i)
        


num1 = int(input("Enter number 1 : "))
num2 = int(input("Enter number 2 :" ))

HCF(num1,num2)