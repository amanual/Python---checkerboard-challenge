import random
def tossCoin():
    count1 = 0
    count2 = 0
    for i in range(1,20):
        h = random.random()
        h_rounded = round(h)
        if h_rounded == 1:
            count1 += 1
            print "Attempt #",i,": Throwing a coin... It's a head! ... Got", count1 ,"head(s) so far and", count2 , "tail(s) so far."

        elif h_rounded == 0:
            count2 += 1
            print "Attempt #",i,": Throwing a coin... It's a tail! ... Got", count1 ,"heads(s) so far and",count2, "tail(s) so far."

    return "Ending the program, thank you!"
print tossCoin()
