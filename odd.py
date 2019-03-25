#odd numbers in given array

odds=[22,11,13,14,15,23,28,27,2345,1]

temp = []
def abc(odds):
    for comp in odds:
        if (comp%2) != 0:
            temp.append(comp)

abc(odds)
print('Odd numbers in given array: ', temp)
