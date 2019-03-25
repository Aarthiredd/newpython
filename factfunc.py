def fact_cal(f):
    """function calculates factorial of a given number"""
    if f==1:
        return 1
    else :
        return(f*fact_cal(f-1))

number=int(input("enter number to find the factorial "))
print("factorial of given number is", fact_cal(number))
