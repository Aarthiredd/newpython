def palindrome():
    string= input("enter the word ")
    type(string)
    if (string==string[::-1]):
        print("entered word is a palindrome")    
    else:
        print("entered word is not a palindrome")
palindrome()


