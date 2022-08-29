# Q2). Write a program in Python for, In a array 1-100 multiple numbers are duplicates, how do you find it.

lst = []

n = int(input("Enter n : "))

for i in range(0,n):
    user_input = int(input("Enter number {} : ".format(i+1)))
    lst.append(user_input)

counting = 0
lst_dup = []
for i in range(0,len(lst)) :
    counting = lst.count(lst[i]) 
    # print(counting)
    if counting > 1:
        lst_dup.append(lst[i])

print(list(set(lst_dup)))