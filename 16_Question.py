#Q16). Python Program to find the Average of numbers with explanations.


def sum_num(lst):
    add = 0
    for i in range(0,len(lst)):
        add += lst[i]
    return add

def avg(lst):
    summing = sum_num(lst)
    average = summing/len(lst)
    return average


lst = []
n = int(input("Enter range : "))
for i in range(0,n):
    user_input = int(input(f"Enter number {i + 1} : "))
    lst.append(user_input)

res = avg(lst)
print(res)

