def return_tuple(*args):  # returns Tuple of passed in *args elements
    print(args)


# '*' in python is operator of packing of arguments

return_tuple("D:\\Python", "\\bases", "\\base_1\\lession-1.txt")


def os_path(*args):
    path = "\\".join(args)
    return path


path_2 = os_path("F:\\Python_basics", "basic_1", "work_with_sets", "sets.txt")
print(path_2)  # returns F:\Python_basics\basic_1\work_with_sets\sets.txt


def os_path_improved(*args, separator='\\'):
    path = separator.join(args)
    return path


path_3 = os_path_improved("F:\\Python_basics", "basic_1", "work_with_sets", "sets.txt")
print(path_3)  # returns F:\Python_basics\basic_1\work_with_sets\sets.txt

"""Collection of named arguments as a dict"""


def os_path_with_kwargs(*args, **kwargs):
    print("These are *args: ", args)
    print("These are **kwargs: ", kwargs)


os_path_with_kwargs("F:\\Python_basics", "basic_1", "work_with_sets", "sets.txt", sep="/", trim=True)


def os_path_with_tricks(*args, sep="\\", **kwargs):
    print("These are *args: ", args)
    print("This is sep", sep)
    print("These are **kwargs: ", kwargs)
    print(f"This is element of **kwargs: { kwargs['loshadka']} ##"
          f"(if not passed to function as named parameter, all falls)")


os_path_with_tricks("F:\\Python_basics",
                    "basic_1",
                    "work_with_sets",
                    "sets.txt",
                    sep="/",
                    trim=True,
                    loshadka="IGOGO"
                    )


"""Packing unpacking"""

x, *y = [1, "a", True, 4]
print(f"This is x: {x} and this is y: {y}") # x: 1, y: ["a", True, 4]
print("*"*50)

*x, y = 1, 2, 3
print(x, y) # [1, 2] 3
print("*"*50)

*x, y, z = "Hello IGOGO!"
print(x) # ['H', 'e', 'l', 'l', 'o', ' ', 'I', 'G', 'O', 'G']
print(y) # O
print(z) # !
print("*"*50)

a = [1, 3, 4]
a = (a,) # ([1, 3, 4],)
print(a)
print("*"*50)

cortege = -5, 5
print(cortege) #(-5, 5)

for i in range(*cortege): # will print sequence from - 5 to 4 (the same is for i in range(-5, 5))
    print(i)

list_of_cortege = list(range(*cortege))
print(list_of_cortege) # [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4]
print("*"*50)

unpack_range = [*range(*cortege)] # [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4]
print(unpack_range)
print("*"*50)

u = [1, 2, 3, 5, 6]
p = True, False, True
o = "World", "not", "hello"

new_generator = [*u, *p, *o]
print(new_generator)
print("*"*50)

"""Dictionaries"""

dicty = {0: "No hope",
         1: "Still no hope",
         2: "At least human",
         3: "Know how to read in motherlanguage",
         4: "Will not die in socium",
         5: "Will rule the future",
         6: "Alien"
         }

dicty_keys = {*dicty} #{0, 1, 2, 3, 4, 5, 6}
print(dicty_keys)

dicty_values = {*dicty.items()} #{(5, 'Will rule the future'), (6, 'Alien'), (1, 'Still no hope'), (3, 'Know how to read in motherlanguage'), (4, 'Will not die in socium'), (0, 'No hope'), (2, 'At least human')}
print(dicty_values)

dicty_to_join = {
    11: "Last class of the school in Eastern Europe",
    12: "Goes after 11"
}

joined = {**dicty_to_join, **dicty} #joines 2 dicts to one
print(joined)










