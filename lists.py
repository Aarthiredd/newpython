learnlist=['aarthika',1,'learning','python','23']
learnlist2=['Reddy','2','python','Awesome','24']
learnlist3=['Karumudi','3','isgreat','thinkso','25']
learnlist4=['join me with something else']
print(learnlist)
#appending the list
learnlist.append('forgot to add')
learnlist4.append(learnlist3)
print(learnlist4)
print("updated list is ", learnlist)
#extending the list
learnlist.extend(learnlist2)
print("extended list", learnlist)
#indexing a value in the list
learnlist2.insert(3,'added you in between')
print("after adding a value in between", learnlist2)
count= learnlist2.count('a')
print("count of a is ",count)
#poping an element
learnlist.pop(1)
print(learnlist)
learnlist2.pop(5)
print(learnlist2)
learnlist5=[ x ** x for x in range(10)]
print(learnlist5)