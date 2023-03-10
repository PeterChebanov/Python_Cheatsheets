from pprint import pprint

N = 6
# a = [0] * N
#
# for i in range(N):
#     a[i] = i ** 2

"""Commented above could be: """


a = [x ** 2 for x in range(N)]
print(a)
print('=' * 30)


"""[<function or expression to work with each element> for <element> in <iter object> <condition(optional)>]"""


b = [1 for x in range(N)]
print(b)
print('=' * 30)


c = [x for x in range(N)]
print(c)
print('=' * 30)


d = [x % 4 for x in range(N)]
print(d)
print('=' * 30)


print(137 % 138)
print("In case number you want divide to is bigger then base number, reminder of division returns base number")
print('=' * 30)

e = [x % 2 == 0 for x in range(N)]
print(e)
print('=' * 30)


f = [0.5 * x + 1 for x in range(N)]
print(f)
print('=' * 30)
print(f" 0 x 0.5 ={0 * 0.5}")
print(f"0.0 + 1 = {0.0 + 1}")
print('=' * 30)


def plus_one(x):
    return x + 1


g = [plus_one(x) for x in range(N)]
print(g)

# number_input = input("Введите целые числа через пробел: ")
# h = [int(number) for number in number_input.split()]
# print(h)

"""Generator with condition"""
o = [x for x in range(-5, 5) if x < 0]
print(o)
print('=' * 30)


books = ["Lord of the Rings", "Harry Potter", "Friends", "Marketing Wars", "History or Celts", "Legents of the Old Ireland"]
p = [book for book in books if len(book) > 15 and book.startswith("L")]
print(p)
print('=' * 30)

q = [1, -22, 34, 17, 99, 11, 3, 14, 8, -42, 65, 66, -71, 2, 87]
evens_odd = ["чётное" if x % 2 == 0 else "нечётное"
             for x in q
             if x > 0
             ]
print(evens_odd)
print('=' * 30)


"""Nested List comprehensions"""
print("\nNESTED LIST COMPREHENSIONS")

a = [(i, j)
     for i in range(3) if i % 3 == 0
     for j in range(4) if j % 2 == 0
     ]
pprint(a)
print('=' * 30)


print("Multiply table: ")
table = [f"{i} * {j} = {i * j}"
         for i in range(1, 11)
         for j in range(1, 11)
         ]
pprint(table)
print('=' * 30)


print("Matrix Transformation")
matrix = [[0, 1, 2, 3],
          [10, 11, 12, 13],
          [20, 21, 22, 23]
          ]
linear_massive = [x
                  for row in matrix
                  for x in row
                  ]
print(linear_massive)
print('=' * 30)


print("create matrix with nested generator")
M, N = 3, 4
matrix = [[a for a in range(M)] for b in range(N)]
print(matrix)
print('=' * 30)


print("Calculate power of two of each element of the matrix")
A = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
power_of_A = [[x ** 2 for x in elem] for elem in A]
print(power_of_A)
print('=' * 30)

print("Nested power of two")
power_of_two = [u ** 2 for u in [x + 1 for x in range(5)]]
print(power_of_two)
power_of_two_1 = [x ** 2 for x in range(1, 6)]
print(power_of_two_1)
print('=' * 30)

print("Checking range in generator")
reversed_range = [x for x in range(20, 10, -1)] # will start from 20 -> [20, 19, 18, ..., 11]
reversed_range_var_2 = [x for x in reversed(range(10, 20))] # will start with 19 -> [19, 18, 17, ..., 10]
include_zero_reversed = [x for x in range(5, -1, -1)] # returns [5, 4, 3, 2, 1, 0]
include_negative_reversed = [x for x in range(3, -4, -1)] # returns [3, 2, 1, 0, -1, -2, -3]
print(reversed_range)
print(reversed_range_var_2)
print(include_zero_reversed)
print(include_negative_reversed)
print('=' * 30)


print("SET AND DICT COMPREHENSIONS")

"""List to Set"""
print("Converting List to set")
a = [1, 3, '1', '4', -4, 2, 4]
set_of_a = {int(x) for x in a} # works faster than cycle for
print(set_of_a)
print('=' * 30)


"""Dict comprehension"""
print(f"Creating one dict of another")
books_pages = {"Lord of the Rings": '1200', "Harry Potter": '2500', "Marketing wars": "200", "Terminator": "0"}
print(f"Initial dict: {books_pages}")
dict_books_pages = {key.upper(): int(value) for key, value in books_pages.items()}
print(f"Final dict: {dict_books_pages}")
print('=' * 30)

print("Replacing change places key== value, value == key")
dict_replaced = {int(value): key for key, value in books_pages.items()}
print(dict_replaced)
print('=' * 30)


"""Generator expressions"""

a = (x for x in range(1, 22))
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print('=' * 30)

for element in a: # Generator will start from 5 because previously we have taken 4 first elements by method next(a).
    # Remember -> generator could be iterated just once. It remembers the last position was called,
    # anb starts with the next position until Stop Iteration Exception will be raised
    print(element)
print('=' * 30)

# if you need to work with a part of generator sequence or with the all generator, cast gen to list:

b = (x for x in range(1, 22))
c = list(b)

#remember use function list to cast generator, otherwise the list will contain the lint to generator object:
e = [(x for x in range(1, 22))]
print("When use expression [(x for x in range(1, 22))], the list will contain the link to generator expression")
print(f"{e}")
print('=' * 30)

"""Generator function"""

def get_list():
    for x in [1, 2, 3, 4]:
        yield x

a = get_list()
print(next(a))
print(next(a))
print(next(a))
print(next(a))
try:
    print(next(a))
except StopIteration as e:
    print("Generator was iterated up to the final")
finally:
    print('=' * 30)


def get_list_again():
    for i in range(1, 10):
        a = range(i, 11)
        yield sum(a) / len(a)

a = get_list()
print(list(a))
print('=' * 30)

"""open txt file with generator"""

def find_word(f, word):
    g_indx = 0 # index shift according to the reading line -> index per one written line
    for line in f:
        indx = 0
        while(indx != -1):
            indx = line.find(word, indx) #if the word was not found in current line, find() returns -1
            if indx > - 1:
                yield g_indx + indx
                indx += 1
        g_indx += 1

try:
    with open("short_from_news.txt", encoding='utf-8') as file:
        a = find_word(file, "police")
        print(f"The list of indeces of word 'police' in the text file:\n {list(a)}")
except FileNotFoundError:
    print("File was not found")
except:
    print("Unknown error during processing the file")
print('=' * 30)



