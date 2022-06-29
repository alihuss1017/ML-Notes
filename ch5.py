"""
bankai = [1,2,3,4,5,6]
bankai.append(8)
bankai.extend(range(7,11))                          list functions and shit
bankai.remove(8)
bankai.pop(2)
print(bankai)


from collections import deque
queue = deque(["ali", "talha", "qasim"])
queue.append("Aizen")
queue.append("Byakuya")                             queues and shit
queue.popleft()
print(queue)



squares = [x for x in range(5) if x !=3]            list comprehensions 
print(squares)


basket = {'senbonzakura', 'kyoka suigetsu', 'ryujin jakka', 'senbonzakura', 'kokujo tengen my-oh', 'Shinso', 'ryujin jakka'}
bucket = {"Katen Kyokotsu", "Hyorinmaru", "Shinso", "Zangetsu", "Shinso", 'kyoka suigetsu', "Nozarashi"}                        sets
print(bucket-basket) #words in bucket but not basket
print(bucket|basket) # words in bucket or basket or both
print(bucket^basket) #words in bucket or basket but not both 


zanpakuto = {"Aizen":1, "Ichibei": 2, "Yama": 3, "Zaraki":4, "Shunsui": 5, "Toshiro": 6, "Byakuya":7}
del zanpakuto['Byakuya']
print(list(zanpakuto))
print(sorted(zanpakuto))
"""

