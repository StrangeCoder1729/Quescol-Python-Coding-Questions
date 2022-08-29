# Q1). Write a program to reverse an integer in Python

def reverse(num):
    temp = 0
    num1 = num
    rev = 0
    while(num > 0):

        temp = num% 10
        rev = rev*10 + temp
        num = num//10
    return rev


    

num = int(input("Enter number : "))
print(reverse(num))
