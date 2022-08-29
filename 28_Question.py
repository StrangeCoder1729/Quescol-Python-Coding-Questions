#Q28). Python Program to calculate the square root of a given number.

def sqroot(num):
    res = num **(0.5)
    return res


num = int(input("Enter number : "))
ans = sqroot(num)
print(round(ans,3))