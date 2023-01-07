#pure functions: same input should always produce same output, no side effects

def multiply_by_2(li):
    new_list=[]
    for item in li:
        new_list.append(item*2)
    return new_list

print(multiply_by_2([1,2,3]))


#map: allows you to execute an action for an iterable

def multiply_by_2(item):
    return item*2
print(list(map(multiply_by_2,[1,2,3])))


#filter: applies a filter function to a given iterable 

def check_odd(item):
    return item%2 == 1

print(list(filter(check_odd,[1,2,3,4,5,6,7,8,9,10])))


#zip: Two iterables can be zipped together

my_list = [1,2,3]
your_list = [10,20,30]
print(list(zip(my_list,your_list)))


#reduce - pass function, iterable, and initial value in said function

from functools import reduce
my_list = [1,2,3]
def accumulator(acc,item):
    print(acc, item)
    return acc + item
print((reduce(accumulator,my_list,0)))


#lambda expressions: one time anonymous 

my_list = [1,2,3]
print(list(map(lambda item: item*2, my_list)))


#square

my_list = [5,4,3]
print(list(map(lambda item: item**2, my_list)))


#list sorting

a=[(0,2), (4,3), (9,9), (10,-1)]
a.sort(key=lambda x:x[1])
print(a)


#list comprehensions

my_list = [char for char in 'hello']
my_list2 = [num**2 for num in range(0,100) if num % 2 == 0]
print(my_list)
print(my_list2)


#set comprenehsions

my_list = {char for char in 'hello'}
print(my_list)


#dictionary comprehensions

simple_dict = {'a': 1, 'b' : 2}
my_dict = {key:value**2 for key,value in simple_dict.items() if value%2==0}
print(my_dict)


#Exercise: Comprehensions

some_list = ['a','b','c','b','d','m','n','n']
duplicates = list(set([n for n in some_list if (some_list.count(n) > 1)]))
print(duplicates)



#Exercise map,filter,reduce,zip
from functools import reduce
my_pets = ['sisi','bibi','titi','carla']
def a(li):
    for i in li:
        i.capitalize()
print(list(map(lambda x: x.capitalize(), my_pets)))


my_strings = ['a','b','c','d','e']
my_numbers = [5,4,3,2,1]
print(list(zip(my_strings, sorted(my_numbers))))


scores = [73,20,65,18,76,100,88]
def check_score(item):
    return item > 50
print(list(filter(check_score, scores)))


def accumulator(acc,item):
    return acc + item
print(reduce(accumulator,my_numbers + scores, 0))
