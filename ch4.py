"""
x = int(input("Enter a number:"))
if x < 0:
    print("your number is negative")
else:
    print("Your number is positive")                                        
    
  
users = {"Ali": 'active', "Talha": 'inactive', "Qasim": 'active'}
for user, status in users.copy().items():                                           removing shit from collections
    if status == 'inactive':
        del users[user]
print(users)


def error(status):
    match status:
        case 400:
            return "Bad request"
        case 404:
            return "Not found"                                                      matches and cases
        case 418:       
            return "I'm a teapot"
        case _:
            return "Something's wrong with the Internet"
print(error(405))



def players(kind, *arguments, **keywords):
    print("Do you have a favorite", kind, " player?")
    print("I actually do! He's considered the",arguments[1],"!")                    args and keywords
    for kw, ks in keywords.items():
        if ks == kind:
            print("My favorite player is ", kw)


players("Soccer", "great", "best", "worst", LeBron = "Basketball", Messi = "Soccer", Brady = "Football")



def calculator(x):
    return lambda n:x+n                             lambda shit

f = calculator(2)
print(f(3))
"""
