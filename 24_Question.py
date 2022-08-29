#Q24). Python Program to calculate the power without using POW function.(using for loop)

def POW(num,n):
    res = 1
    for i in range(0,n):
        res *= num
    return res


num = int(input("Enter number : "))
n = int(input("Enter the power : "))
print(POW(num,n))