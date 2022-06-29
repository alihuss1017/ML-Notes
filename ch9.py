"""class Dog:
    kind = 'canine'
  
    def __init__ (self, name):
        self.name = name
        self.tricks = []
    def add_trick(self, trick):
        self.tricks.append(trick)



d = Dog("fido")                                                     // OOP shit
e = Dog('buddy')

print(d.kind)
print(e.kind)
print(d.name)
print(e.name)
d.add_trick("Kyoka Suigetsu!")
d.add_trick("Rikujokoro!")
d.add_trick("Hado No. Kyujun: Goryu Tenmetsu!")
print(d.tricks)


import random

def lottery():
    for i in range(6):
        yield random.randint(1,40)
    yield random.randint(1,15)                                      generators

for random_number in lottery():
    print("And the next number is... %d!" % random_number)

"""