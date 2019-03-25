#list of numbers to be checked

a=[21,44,89,68,22,21,2,11]
#comparing numbers
def check(a):
    for com in a:
        if (com%2) == 0:
            print('Even number in given array: ', com)

check(a)