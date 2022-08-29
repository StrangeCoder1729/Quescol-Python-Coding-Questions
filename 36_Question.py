# Q36). Python Program to convert Fahrenheit to Celsius.

def Celsius(F):
    C = (5*(F - 32))/9
    return C


num = int(input("Enter Fahrenheit : "))
print(Celsius(num))