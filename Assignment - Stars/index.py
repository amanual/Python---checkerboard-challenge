#Stars
#Part 1:
def draw_stars(x):
    for i in range(len(x)):
        x[i] *= '*'
        print x[i]
        # return x

x = [4,6,1,3,5,7,25]
draw_stars(x)
#Another way of doing part 1:
def draw_stars2(y):
    for i in y:
        i *= '*'
        print i
y = [3,4,5,12,16,6,7,9]
draw_stars2(y)

#part 2:
def draw_stars(x):
    for i in x:
        if type(i) == type('str'):
            print i[0] * len(i);
        else:
            print i * '*'
x = [4, "Tom", 1, "Michael", 5, 7, "Jimmy Smith"]
draw_stars(x)
