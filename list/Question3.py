# Q3). Write a program in Python for, How to find all pairs in array of integers whose sum is equal to given number.

num = int(input("Enter : "))

lst = []

sum1 = 0
for i in range(0,num):
    for j in range(1,num):
        if(i + j == num):
            print(f"{i} + {j}")
          




