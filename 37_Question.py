# Q37). Python program to calculate Simple Interest with explanation.


def si(pi,rt,ty):
    SI = (pi*rt*ty)/100
    return SI


principal = int(input("Enter Principal Amount : "))
rate = float(input("Enter Rate : "))
time = float(input("Number of years : "))

print(si(principal,rate,time))