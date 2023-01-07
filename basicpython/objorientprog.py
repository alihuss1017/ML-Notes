# ----------------- INTROUDUCTION TO OOP ----------------- #

class PlayerCharacter:
    membership = True #Class object attribute
    def __init__(self,name,age):
        self.name = name #attributes
        self.age = age
    def run(self):
        print('run')
    @classmethod
    def adding_things(num1,num2):
        return num1 + num2

player1 = PlayerCharacter('Ali', 18)
player1.run()
print(player1.name, player1.age)

#  ----------------- EXERCISE ----------------- #

class Cat:
    species = 'mammal'
    def __init__(self,name,age):
        self.name = name
        self.age = age
    
cat1 = Cat("Aizen", 2)
cat2 = Cat('Zazu', 1)
cat3 = Cat("Garfield", 7)

def oldest_cat(*cats):
    return max(cats)

print(f'The oldest cat is {oldest_cat(cat1.age, cat2.age, cat3.age)} years old')

#  ----------------- CLASS AND STATIC METHODS ----------------- #
class PlayerCharacter:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    
    @classmethod
    def adding_things(cls,num1,num2):
        return num1+num2
    @staticmethod
    def adding_things(num1,num2): #no access to class method cls
        return num1+num2
print(PlayerCharacter.adding_things(2,3))

#  ----------------- EXERCISE ----------------- #



