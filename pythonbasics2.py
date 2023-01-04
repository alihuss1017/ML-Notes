#ternary operator

is_friend = False
can_message = "message allowed" if is_friend else "not allowed to message"
print(can_message)


#short circuiting conditional statements can be short circuited when the program knows the expression will eval to true early
#if True or False
#if False and True

#exercise: logical operators

is_magician = False
is_expert = True

if is_magician and is_expert:
    print("You are a master magician")
elif(is_magician and not is_expert):
    print("At least you're getting there")
else:
    print("You need magic powers")


# is vs ==

x=[]
y=[]
print (x == y)
print(x is y)


#iterable - list,dictionary, tuple, set, string, any object/collection that can be iterated over.

#exercise: tricky counter

my_list = [1,2,3,4,5,6,7,8,9,10]
sum = 0
for i in my_list:
    sum+=i
print(sum)


#enumerate - returns index and value at that index

for i, val in enumerate(range(100)):
    print(i,val)


### GUI exercise

picture = [
    [0,0,0,1,0,0,0],
    [0,0,1,1,1,0,0],
    [0,1,1,1,1,1,0],
    [1,1,1,1,1,1,1],
    [0,0,0,1,0,0,0],
    [0,0,0,1,0,0,0]
]
for i in picture:
    for n in i:
        if n == 0:
            print(' ', end='')
        else:
            print('*',end='')
    print(end='\n')
         

#Duplicate Check Exercise

some_list = ['a','b','c','b','d','m','n','n']
duplicates = []
for val in some_list:
    if some_list.count(val) > 1:
        if val not in duplicates:
            duplicates.append(val)
print(duplicates)

#functions

def sum (x,y=2):
    return x+y
print(sum(3))

#tesla exercise

def checkDriverAge(age):
    if age < 18:
        print("Sorry you are too young to drive this car. Powering off")
    elif age > 18:
        print("Powering On. Enjoy the ride!")
    elif age == 18:
        print("Congratulations on your first year of driving. Enjoy the ride!")

checkDriverAge(18)


#docstrings (NEEDS TO BE FIXED)

def test(a):
    #This function prints a
    print(a)

test(3)


# *args **kwargs
#rule: params, *args, default parameters, **kwargs

def super_func(name,*args, i = 'hi', **kwargs):
    total = 0
    for items in kwargs.values():
        total += items
    return sum(args) + total
print(super_func('Andy', 1,2,3,4,5, num1=5,num2=10))


#Exercise: Functions

def highest_even(li):
    max_even = 0
    for n in li:
        if n%2 == 0 and n > max_even:
            max_even = n
    return max_even
print(highest_even([10,1,2,3,4,8,11]))


#Walrus Operator assigns a value as part of a larger expression

a = 'helloooooooooooo'
if (len(a) > 10):
    print(f'too long {len(a)} elements')
if ((n:=len(a)) > 10):
    print(f'too long {n} elements')


#global variables

total = 0
def count():
    global total
    total += 1
    return total
count()
count()
print(count())


#nonlocal keyword is used to refer to parent local variable

def outer():
    x = 'local'
    def inner():
        nonlocal x
        x = 'nonlocal'
        print('inner: ', x)

    inner()
    print('outer: ', x)
outer()
