#Q20). Python program to print first n Prime Number with explanation.

def prime(n):
    isprime = True
    for i in range(2,n):
        if(n % i == 0):
            isprime = False
            break

    if(isprime == True):
        return n
            


n = int(input("Enter range : "))

for i in range(2,n):
    if(prime(i) == None):
        continue
    print(prime(i))