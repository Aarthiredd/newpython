#reversing a string using split join ad sep functions
string=input("enter the string to reverse ")


def reversee(string):
    list(string)
    something=list(string)
    something.reverse()
    sep=""
    sep1=sep.join(something)    
    return sep1

sep = reversee(string)
    
def palindrome(sep):
    if sep==string:
        print("palindrome")
    else:
        print("not palindrome")
palindrome(sep)

