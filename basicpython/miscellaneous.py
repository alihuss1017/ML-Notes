"""
from functools import partial
def multiply (x,y,z):
    return x*y*z                                    partial functions

partial_funct = partial(multiply,2)
print(partial_funct(5,6))



def transmit_to_space(message):
    def data_transmitter():
        print(message)
                                                    closures
    return data_transmitter


x = transmit_to_space("Test message")
x()


shikai = ['zangetsu', 'wabisuke', 'kazeshini', 'tobirume', 'haineko']
users = ['Ichigo', 'Kira', 'Hisagi', 'Hinamori', 'Rangiku']                     
uppered_shikai = list(map(str.upper, shikai))                   map
print(uppered_shikai)

combo = list(zip(users, shikai))                                zip
print(combo)

scores = [50,60,70,80,90,100]
def passing(score):
    return score > 70 or score == 70                            filter
passing_grade = list(filter(passing,scores))
print(passing_grade)

from functools import reduce
hado = [4,5,6,234,234,34,4]
def custom_sum(firstNum, secondNum):                            reduce
    return firstNum+secondNum
kido = reduce(custom_sum, hado,)
print(kido)
"""