# Q17). Python Program to calculate factorial using iterative method.

def fact(num):
    mul = 1
    for i in range(1,num+1):
        mul = mul * i
    return mul


num = int(input("Enter number : "))
print(fact(num))