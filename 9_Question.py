#Q9). Write a program in Python to check if a number is binary?

def binary(num):
    num = int(num)
    temp = 0
    isbinary = True
    while(num > 0):
        temp = num % 10

        if (temp !=1 and temp != 0):
            isbinary = False
            break

        num = num//10
    if(isbinary== True):
        print("The number is binary")
    else:
        print("The number is not binary")




n = input("Enter : ")
res = binary(n)