#Integer:
#shown in two ways, using loop and using only if-statement:
    #using loop:
for num in range(1, 200):
    if num >= 100:
        print "That's a big number!"
    else:
        print "That's a small number!"
    #Using only if-statement
num = raw_input()
if num >= 100:
    print "That's a big number!"
else:
    print "That's a small number!"

#String:
string = 'Rubber baby buggy bumpers'
if len(string) >= 50:
    print "Long sentence."
else:
    print "Short sentence."

#List:
list1 = [1,2,3,4,77,98,34,33,345,12]
if len(list1) >= 10:
    print "Big list!"
else:
    print "Short list."

