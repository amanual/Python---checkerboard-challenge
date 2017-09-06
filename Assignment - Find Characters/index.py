#Find Characters
# input
word_list = ['hello','world','my','name','is','Anna']
char = 'o'
new_list = []
for i in word_list:
    for latters in i:
        if latters == char:
            new_list.append(i)
print new_list  