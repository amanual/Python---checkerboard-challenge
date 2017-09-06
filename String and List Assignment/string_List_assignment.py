words = "It's thanksgiving day. It's my birthday,too!"
print words.find('d')
print words[18:21]
m = 'month'
print words[:18] + m + words[21:]
#another way of doing this will be
print words.find('day')
words = words.replace('day', 'month')
print words

#Printing Min & Max
x = [2,54,-2,7,12,98]
minV = min(x)
maxV = max(x)
print minV
print maxV

#Printing First and Last
x = ["hello",2,54,-2,7,12,98,"world"]
first = x[0]
last = x[-1]
new = []
new.append(first)
new.append(last)
print first
print last
print new



#Printing New List
x = [19,2,54,-2,7,12,98,32,10,-3,6]
x.sort()
half =len(x)/2
count = len(x)
print len(x)
print x
num =  x[:half]
newL = []
newL.append(num)

for num in range(half, count):
    newL.append(x[num])
print newL

#another way of doing this will be
y = [19,2,54,-2,7,12,98,32,10,-3,6]
y.sort()
first_list = x[:len(x)/2]
second_list = x[len(x)/2:]
second_list.insert(0, first_list)
print second_list


