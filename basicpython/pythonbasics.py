# 8 / 2 is a float
# 8 // 2 is an int
# bin() prints binary rep of an int
# priv variables start with an underscore
# const variables are in all caps

name = "Ali"
age = "20"
print(f'Hi {name}! Happy {age}th birthday!')

#strings are immutable: you cannot change the values of a string once created: for example: selfish[0] = '9' is invalid

quincy = 'Yhwach'
print(len(quincy))
print(quincy.upper())
print(quincy.capitalize())
print(quincy.replace("Yhwach", "Ichigo"))
print(quincy) #this will print yhwach still because strings are immutable

birth_year = input("What year were you born? ")
age = 2022 - int(birth_year)
print(f'Oh, so you\'re {age} years old!')

username = input("Enter username: ")
password = input("Enter password: ")
password_length = len(password)
encrypted_password = '*' * password_length
print(f'{username}, your password {encrypted_password} is {password_length} characters long.')

#list ordered sequence of objects of any type, and unlike strings, they are mutable 
x = [1,2,3,4,5]
z = x[:] # list slicing creates a new copy of the list: if you simply pass the list, any changes to z will change x
z[4] = 6
print(x)
print(z)

z.extend([6,7,8,9,10])
z.append(11)
z.pop()
z.pop(1)
print(z)
print(z.index(9))

basket = ['a','b', 'x', 'w','e','f']
print(sorted(basket))
basket.reverse()
print(basket)
print(' '.join(basket))


#list unpacking

a,b,c, *other, d = [1,2,3,4,5,6,7,8,9,10]
print(a)
print(b)
print(c)
print(other)
print(d)


#dictionaries: unordered key-value pairs. A dictionary's keys must be immutable: having a key of type list is an error

dictionary = {'name': 'Ali Hussain', 'age': 20, 'occupation': 'EE student'}
print(dictionary)
print(dictionary.get('age',55)) #checks if age exists and if not, then it uses 55 for age.
dictionary.update({'occupation':'Top G'})
dictionary.pop('age')
print(dictionary)


#tuples are like lists but immutable; they cannot be changed.

my_tuple = (1,2,3,4,5)
print(my_tuple.count(1))
print(my_tuple.index(3))

#set: an unordered collection of unique objects

my_set = {1,2,3,4,5,5}
your_set = {4,5,6,7,8,9,10}
print(my_set) #will only print 5 once
my_set.add(100)
print(my_set)
print(my_set.difference(your_set))
