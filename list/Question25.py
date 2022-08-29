# 25). Python Program to add two number.


def add (n1,n2):
    if(n1 == 0 and n2 == 0):
        return 0
    elif((n1 == 0 and n2 == 1) or (n1 == 1 and n2 == 0)):
        return 1
    else:
        return n1 + n2


n1 = int(input("Enter Number 1 : "))
n2 = int(input("Enter Number 2 : "))

print(add(n1,n2))