# Q10). Python program to print array in reverse Order.

lst = []
n = int(input("Enter n : "))

for i in range(0,n):
    user_input = int(input("Enter Number {}: ".format(i+1)))
    lst.append(user_input)

print("Original List is {}".format(lst))

lst_reverse = []
for i in range(len(lst),0,-1):
    lst_reverse.append(lst[i-1])

print("Reversed of the List is {}".format(lst_reverse))