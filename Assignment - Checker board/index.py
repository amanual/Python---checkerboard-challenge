#Checkerboard
char_1 = '*'+' '
char_2 = ' '+'*'
for star in range(1, 8):
    print (char_1 * 4)
    print (char_2 * 4)
#Anotherway:
def checkerboard():
    for i in range(0, 8):
        if i%2 == 0:
            print "* " * 4
        else:
            print " *" * 4
