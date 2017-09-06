#Odd/Even:
def odd_even(x, y):
    for count in range(x,y):
        # print count
        if count % 2 == 1:
            print "Number is %s." % count,"This is an odd number."
        else:
            print "Number is %s." % count,"This is an even number."
    return x,y
print odd_even(1,20)

#Multiply:
def multiply(arr, num):
    for i in range(len(arr)):
        arr[i] *= num
    return arr
a = [2,4,10,16]
b = multiply(a, 5)
print b

#Hacker Challenge:
def layered_multiples(arr):
    new_array = []
    for i in range(len(arr)):
        temp = []
        for y in range(arr[i]):
            temp.append(1)
        new_array.append(temp)
    return new_array
print layered_multiples(multiply([2,4,5],3))
