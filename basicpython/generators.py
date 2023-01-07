#generators #conserves memory by iterating one-by-one without creating a list in memory
'''
def generator_function(num):
    for i in range(num):
        yield i*2

for item in generator_function(1000):
    print(item)


#fibonacci exercise

def fib(number):
    a = 0
    b = 1
    for i in range(number):
        yield a
        temp = a
        a = b
        b += temp

for x in fib(20):
    print(x)
'''

