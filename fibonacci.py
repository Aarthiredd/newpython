#fibonacci
def fibonacci():
    n1=0
    n2=1
    n=int(input("enter the number of terms"))
    for i in n:
        while i<=n:
            n=n+1
    ans=n1+n2
    n2=ans
    print(ans)