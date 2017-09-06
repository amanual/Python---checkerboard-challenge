import random
def scores_grades():
    print "Scores and Grades"
    for data in range(1, 11):
        random_num = random.randint(60,100)
        if random_num >= 60 and random_num <= 69:
            print "Score:%s" % random_num,";","Your grade is D"
        elif random_num >= 70 and random_num <= 79:
            print "Score:%s" % random_num,";","Your grade is C"
        elif random_num >= 80 and random_num <= 89:
            print "Score:%s" % random_num,";","Your grade is B"
        elif random_num >= 90 and random_num <= 100:
            print "Score:%s" % random_num,";","Your grade is A"
    return "End of the program. Bye!"

print scores_grades()
