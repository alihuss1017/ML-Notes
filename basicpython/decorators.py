#Decorator
'''
def my_decorator(func):

    def wrap_func():
        print('*************')
        func()
        print('*************')
    return wrap_func

@my_decorator
def hello():
    print('hellllooooooo')
@my_decorator
def bye():
    print('byyyyeeeeeeee')
hello()
bye()
'''

#Decorator pt2
'''
from time import time
def performance(fn):
    def wrapper(*args,**kwargs):
        t1 = time()
        result = fn(*args,**kwargs)
        t2 = time()
        print(f'took {t2-t1} s')
        return result
    return wrapper

@performance
def long_time():
    for i in range(100000000):
        i*5
long_time()
'''

#Decorators Exercise
'''
user1 = {
    'name':'Sorna',
    'valid': True
}

def authenticated(fn):
    def wrapper_fn(*args,**kwargs):
        if args[0]['valid'] == True:
            return fn(*args,**kwargs)
        else:
            return 1
    return wrapper_fn

@authenticated
def message_friends(user):
    print('message has been sent')

message_friends(user1)
'''
