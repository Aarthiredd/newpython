#prime numbers
p=int(input("enter a number"))
if p>1:
    for i in range(2,p):
        if (p%i)==0:
            print(p, " is not a prime number")
            break
        else:
            print(p, " is a prime number")
            break