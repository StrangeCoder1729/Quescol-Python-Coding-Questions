#Q21). Python Program to print Prime Number in a given range

def prime(n):
    isprime = True
    for i in range(2, n):
        if(n % i == 0):
            isprime = False
            break
    if(isprime == True):
        return n


n1 = int(input("Enter n1 : "))
n2 = int(input("Enter n2 : "))
for i in range(2, n2):
    if(prime(i) == None):
        continue
    print(prime(i))