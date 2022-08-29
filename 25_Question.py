#Q25). Python Program to calculate the power without using POW function.(using while loop).

def POW(num,power):
    i = 0
    res = 1
    while(i < power):
        res *= num
        i+=1
    return res




num = int(input("Enter number : "))
power = int(input("Enter power : "))
print(POW(num,power))