dicty = {"2": 2, "3": 3}

dicty_1 = dicty.copy()

print(dicty_1.setdefault("3")) # returns value of key if key exists
print(dicty_1.setdefault("3", 11)) # returns initial value of key if key exists -> ignoring second argument == 11
print(dicty_1.setdefault("4", 4))# creates key-value and returns value if key does not exist
print(dicty_1.setdefault("15")) # creates key 15 if not exists and returns None as second parameter is not passed
print(dicty_1)
print(dicty_1.get(12)) # -> if no key 12 in dicty_1 -> returns None by default
print(dicty_1.get(12, "Cat playing cards")) # -> if no key 12 in dicty_1 -> returns custom value if passed as argument
print(dicty_1.pop("3")) # delete key-value pair and returns value
print(dicty_1.pop("123")) # fails with error KeyError
print(dicty_1.pop("123", "Cat playing piano")) # doesn't fail with KeyError and returns custom value passed as argument

dicty_123 = {False: False, "cat": "Simon", "age": 1.5, 100: 100}
dicty_124 = {True: True, "racoon": "Alvarez", "age": 2, 100500: 100500}

print("Add one dict to another (values in existed keys in both dictionaries will be overriden by the last dictionary")
dicty_123.update(dicty_124) #key age exists in both dictionaries. Value of dicty_124 will be add to "age" of dicty_123

dicty_123 = {False: False, "cat": "Simon", "age": 1.5, 100: 100}
dicty_124 = {True: True, "racoon": "Alvarez", "age": 2, 100500: 100500}

print("Creating new dictionary of the two existing")

dicty_125 = {**dicty_123, **dicty_124} # Value of key 'age' of dicty_123 will be replaced by value of 'age' dicty_124
