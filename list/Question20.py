# 20). Python Program to print all odd numbers in array.

lst = list(map(int,input("Enter Numbers : ").split()))

lst2 = [num for num in lst if num % 2 != 0]
print("Odd numbers in the list : {}".format(lst2))