#Error Handling
'''
while True:
    try:
        age = int(input('what is your age? '))
        print(age)
        10/age
    except ValueError:
        print("Please enter a number")
    except ZeroDivisionError:
        print("Please enter age higher than 0")
    else:
        print('Thank you!')
        break
'''

#Error Handling 2
'''
def sum(num1, num2):
    try:
        return num1 + num2
    except TypeError as err:
        print(f'Please enter numbers: {err}')

print((sum('1',2)))
'''

