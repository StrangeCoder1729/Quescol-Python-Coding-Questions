# Q29). Python program to calculate LCM of given two numbers.

"""LCM of two numbers = (Product of two numbers)/ their HCF"""

def prime(num):

    isprime = True
    for i in range(2,num):
        if(num % i == 0):
            isprime = False
            break
    if(isprime == True):
        # print(num)
        return num

def primenum1(num1):

    lst_prime = []
    for i in range(2,num1):
        if(num1 % i == 0):
            if(prime(i) == None):
                continue
            lst_prime.append(prime(i))
    return lst_prime

def primenum2(num2):
    
    lst_prime = []
    for i in range(2,num2):
        if(num2 % i == 0):
            if(prime(i) == None):
                continue
            lst_prime.append(prime(i))
    return lst_prime

def HCF(num1, num2):
    prime_factores_1 = primenum1(num1)
    # print(prime_factores_1)
    prime_factores_2 = primenum1(num2)
    # print(prime_factores_2)

    len_1 = len(prime_factores_1)
    len_2 = len(prime_factores_2)
    final_len = 0
    ans = 0
    if(len_1 > len_2):
        final_len = len_1
        ans = prime_factores_1
    elif(len_2 > len_1):
        final_len = len_2
        ans = prime_factores_2
    else:
        final_len = len_1
        ans = prime_factores_1
    # print(final_len)
    
    # print(ans)
    print(prime_factores_1)
    print(prime_factores_2)
    res = 0
    for i in range(0,final_len):
        for j in range(0,i):
            # print(ans[i])
             
            if(prime_factores_1[i] == prime_factores_2[j]):
                return ans[i]
                break
    # return res
                
   
     

def LCM(num1,num2):
    hcf = HCF(num1,num2)
  
    print(hcf)
    # lcm = (num1*num2)/hcf
    # return lcm


num1 = int(input("Enter Number 1 : "))
num2 = int(input("Enter Number 2 : "))

LCM(num1,num2)