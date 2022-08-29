# Q35). Python Program to convert Celsius to Fahrenheit.

def farh(C):
    F = ((9*C)/5) + 32
    return F

num = int(input("Enter Celsius : "))
print(farh(num))