#Q3). Write a program in Python to check given number is prime or not.

def prime(num):
    num1 = num 
    isprime = True
    for i in range(2,num):
        if(num % i == 0):
            isprime = False
            break
    if(isprime == True):
        print("It is a Prime number !!!")
    elif(isprime == False):
        print("It is not a prime number !!!")



num = int(input("Enter number : "))
prime(num)