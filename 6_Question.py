#Q6). Write a program in Python to check whether a number is palindrome or not using iterative method

def reverse(num):
    temp = 0
    rev = 0
    while(num > 0):
        temp = num % 10
        rev = rev* 10 + temp
        num = num// 10
    return rev

def checkpalindrome(num1,num2):
    if(num1 == num2):
        print("It is a Palindrome !!")
    else:
        print("It is not a palindrome !!!")
    

num = int(input("Enter number : "))
res1 = reverse(num)
checkpalindrome(num,res1)