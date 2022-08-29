# Q19). Python Program to check a given number is even or odd.

def detect (num):
    if(num % 2 == 0):
        print("The Number is even !!")
    else:
        print("The Number is odd !!")


num =int(input("Enter number : "))
detect(num)