# 26). Python Program to find sum of digit of number 


num = int(input("Enter Number : "))

temp = num 
add = 0
while(num > 0):
    temp = num % 10
    add += temp
    num = num// 10

print("Addition of all digits of the number is {}".format(add))
