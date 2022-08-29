#Q26). Python Program to calculate the square of a given number.

def square(num):
    res = 1
    for i in range(0, 2):
        res *= num
    return res


num = int(input("Enter number : "))
print(square(num))