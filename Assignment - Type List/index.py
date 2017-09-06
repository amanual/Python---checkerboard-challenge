#Type List
#inputs:
list2 = ['magical unicorns',19,'hello',98.98,'world']
list1 = [2,3,1,7,4,12]
list3 = ['magical','unicorns']

addS = ''
addN = 0
for num in list1: 
    result = isinstance(num, int)
    result2 = isinstance(num, str)
    if result2 == True:
        print "The list you entered is of string type"
        print "String: " + num       
        continue
         
    elif result == True:
        addN += num 
        print "The list you entered is of integer type"
        print "Sum: ", addN
        continue
        
    else:
        # addN += num
        print "The list you entere is of mixed type"
        print "String: " + num
        print "Sum: ", addN



