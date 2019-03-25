#finding the smallest in given numbers

n=6
i=5
a=[4,7,8,9,2]

while i<=a[n]:
    min=a[i]
    i+=1
    if min<a[i+1]:
        continue
    print("smallest number is", a[i])


    
