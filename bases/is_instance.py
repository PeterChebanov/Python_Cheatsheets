"""Not strict checking"""

a, b, c = 1, True, "igogo"

print(type(a))
print(type(b))
print(type(c))
print("*"*50)

print(isinstance(a, float)) # False
print(isinstance(a, int)) # True
print(isinstance(b, bool)) # True

print(isinstance(b, int)) # True ->> because of the inheritance of the types in python this NOT strict checking returns True

print(isinstance(b, str)) # False
print(isinstance(c, str)) # True
# isinstance uses in OOP to know if the element is the instance of exact object of the class, while strict checking compares types between each other in atom way

"""Strict checking"""

print(type(b) == bool) # True
print(type(b) is bool) # True

print(type(b) == int) # False
print(type(b) is int) # False

print(type(a) == bool) # False
print(type(a) is bool) # False

print(type(a) == int) # True
print(type(a) is int) # True
print("*"*50)

print(type(b) in (bool, float, str)) # True => type of b contains in cortege
print("*"*50)

types = (4.5, 8.7, True, 'book', 8, 10, -11, [True, False])



"""example of non strict checking"""


#we want to calculate sum of floats in 'types'

s = 0
for elem in types:
    if (isinstance(elem, float)):
        s += elem
print(s)# 13.2

#another way to calculate sum of floats in 'types'

s = sum(filter(lambda x: isinstance(x, float), types)) # 13.2
print("*"*50)

"""example of strict checking"""
f = sum(filter(lambda x: type(x) == float, types)) # 13.2
print(f)
print("*"*50)


"""example of FAIL of non strict checking"""
# we want to calculate sum of all int in 'types'

types = (4.5, 8.7, True, 'book', 8, 10, -11, [True, False])

fs = sum(filter(lambda x: isinstance(x, int), types)) # expected == 7, actual == 8  #--> because isinstance(elem[2]) also == 1, as returned for True. To have prescise result we have to use strict checking
print("*"*50)
print(f"Result with non strict check: {fs}")

"""the same with strict checking"""

sc = sum(filter(lambda x: type(x) is int, types)) # expected == 7, actual == 7
print("*"*50)
print(f"Result with strict check: {sc}")



"""Сheck if element is instance of one of the listed"""

j = 135
print(isinstance(j, (int, float))) #True