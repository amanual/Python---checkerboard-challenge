#Multiples
#Part 1:
for num in range(1, 1000):    
    if num % 2 == 1:
        print num
#Part 2:
for num2 in range(1, 1000000):
    if num2 % 5 == 0:
        print num2
Sum List
a = [1, 2, 5, 10, 255, 3]
sumN = 0
for i in a:
    sumN = sumN + i
print sumN

# Average List
a = [1, 2, 5, 10, 255, 3]
ave = 0
sumN = 0
for num in a:
    sumN = sumN + num 
    ave = sumN / 2.0
print ave 