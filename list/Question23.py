# 23). Python Program to merge two arrays.

lst1 = list(map(int,input("Enter Numbers for list 1 : ").split()))
lst2 = list(map(int,input("Enter Numbers for list 2 : ").split()))

lst3 = lst1 + lst2
print("List 1 and List 2 is combined : {}".format(lst3))
