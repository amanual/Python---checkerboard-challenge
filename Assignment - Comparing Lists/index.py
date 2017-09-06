#Comparing Lists
#test inputs:
list_1 = [1,2,5,6,2]
list_2 = [1,2,5,6,2]

list_2 = [1,2,5,6,5]
list_3 = [1,2,5,6,5,3]

list_4 = [1,2,5,6,5,16]
list_5 = [1,2,5,6,5]

list_6 = ['celery','carrots','bread','milk']
list_7 = ['celery','carrots','bread','cream']

x = len(list_4)
y = len (list_5)
length = cmp(x, y)
comp = cmp(list_4, list_5)
if x == y and comp == True:
    print "The lists are the same."

else:
    print "The lists are not the same."
        