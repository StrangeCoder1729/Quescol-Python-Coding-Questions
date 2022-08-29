#Q2). Write a program in Python to check whether an integer is Armstrong number or not.

def armstrong(num,num_digits):
    num1 = num 
    temp = 0
    arm = 0

    while(num > 0):

        temp = num % 10
        arm += pow(temp,num_digits)
        num = num //10
    if(arm == num1):
        print("It is an Armstrong number !!!")
    else:
        print("It is not an Armstrong number !!!")




num = int(input("Enter number : "))

num_of_digits = len(str(num))

armstrong(num,num_of_digits)
