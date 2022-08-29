# 24). Python Program to find highest frequency element in array.

lst = list(map(int,input("Enter numbers : ").split()))

print(lst)
lst2 = []
for i in range(0,len(lst)):
    counting = lst.count(lst[i])
    lst2.append(counting)

maxi = max(lst2)
inde = lst2.index(maxi)
print(f"Maximum frquency of the element in the list : {lst[inde]}")
