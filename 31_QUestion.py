# Q31). Python Program to find GCD of two numbers without using recursion.


def prime(num):
    isprime = True

    for i in range(2,num):
        if(num % i == 0):
            isprime = False
            break
    if(isprime == True):
        return num

def prime_factors(num):
    ans = prime(num)
    lst_prime = []
    for i in range(2,num):
        if(prime(i) == None):
            continue
        lst_prime.append(prime(i))
    
    return lst_prime
def GCD(num1,num2):
    res1 = prime_factors(num1)
    res2 = prime_factors(num2)
    print(res1)
    print(res2)

    lst_max_factor = []
    if(len(res1)> len(res2)):
        for i in range(0,len(res2)):
            # print(f"{i}:- ")
            for j in range(0,i+1):
                # print(res1[i], res2[j])
                if(res1[i] == res2[j]):
                    lst_max_factor.append(res1[i])
                    lst_max_factor.append(res2[j])
                    # print(f"{res1[i]} {res2[j]}")

    if(len(res1) <  len(res2)):
        for i in range(0,len(res1)):
            for j in range(0,i+1):
                if(res1[j] == res2[i]):
                    lst_max_factor.append(res1[j])
                    lst_max_factor.append(res2[i])
                    # print(f"{res1[i]} {res2[j]}")

    elif(len(res1) ==  len(res2)):
        for i in range(0,len(res1)):
            for j in range(0,i+1):
                if(res1[j] == res2[i]):
                    lst_max_factor.append(res1[j])
                    lst_max_factor.append(res2[i])

    lst_max_factor = set(lst_max_factor)
    lst_max_factor = list(lst_max_factor)
    print(lst_max_factor)
     
    

num1 = int(input("Enter number 1 : "))
num2 = int(input("Enter number 2 : "))
GCD(num1,num2)