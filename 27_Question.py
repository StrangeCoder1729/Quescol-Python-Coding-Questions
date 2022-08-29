#Q27). Python Program to calculate the cube of a given number

def cube(num):
    res = 1
    for i in range(0,3):
        res *= num 
    return res


num = int(input("Enter number : "))
ans = cube(num)
print(ans)