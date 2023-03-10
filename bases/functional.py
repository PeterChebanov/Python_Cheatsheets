""""map"""
print("MAP")
b = map(int, ['1', '2', '3', '4', '5'])
c = (int(x) for x in ['1', '2', '3', '4', '5'])  # the same as with using map function above
print(b)  # will show the link to the map object
print(list(b))  # show the converted list by func map
print(list(c))
print('*' * 50)

c = (int(x) for x in ['1', '2', '3', '4', '5'])
print(sum(list(c)))  # returns sum of all elements of generator c
print('*' * 50)

cities = ["Tokio", "Toronto", "Seatle", "Barcelona", "Amsterdam"]
cities_len = map(len, cities)  # crates generator of each len of each element of cities list
print(list(cities_len))  # cast generator to list
print('*' * 50)

cities_upper = map(str.upper, cities)
print(list(cities_upper))  # change elements of cities to upper case
print('*' * 50)


def clear_first_T(title):
    if title.startswith("T"):
        return None
    return title


cities_not_started_with_T = map(clear_first_T, cities)
print(list(cities_not_started_with_T))

f = map(lambda x: list(x), cities)
print(list(f))

reversed_cities_names = map(lambda x: x[::-1], cities)
print(list(reversed_cities_names))
print('*' * 50)

"""filter"""

print("FILTERS")
a = [1, 2, 3, 4, 8, 5, 6, 12, 13, 14, 15, 21, 22, 26]
b = filter(lambda x: x % 2 == 0, a)
lst = tuple(b)
print(lst)
print('*' * 50)

"""ZIP - joins pairs of indexes of  different lists to new list -> if len of one list > then len of another, zip will 
ignore the rest of list which does not have pair index in another list"""

a = [1, 2, 3, 4, 5]
b = [12, 14, 15, 16, 17, 18]
z = zip(a, b)  # generator of tuples of 2 elements with the same index of different lists
for x in z:
    print(x)
print('*' * 50)

a = [1, 2, 3, 4, 5]
b = [12, 14, 15, 16, 17, 18]
c = "Python"

z = zip(a, b, c)
for x in z:
    print(x)
print('*' * 50)     # (1, 12, 'P')
                    # (2, 14, 'y')
                    # (3, 15, 't')
                    # (4, 16, 'h')
                    # (5, 17, 'o') -> no 'n' will be included because len(a) < len(b) and len(c)
