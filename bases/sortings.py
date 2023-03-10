a = [12, 3, 144, 81, 0, 54, 111, 36, 17, 2020, 1104, 5]

# a.sort() -> function for sorting only of lists

# sorted(a) -> function for sorting any iteration object. In case of sorting unmutable objects(f.e. tiples), func will return sorted list with elements of initial tuple

"""Custom function to sort"""


def is_odd(number):
    return number % 2  # returns 0 or 1


b = sorted(a, key=is_odd) # creates another sorted list by rule of "key=" and does not mutate the initial func
print(b)
print("="*50)
c = sorted(a, key=lambda x: x % 2) # another form to write the same sorting by odd
print(c)
print("="*50)

a.sort(key=lambda x: x % 2) # sort initial list mutating it
print(a)
print("="*50)


cities = ["Tokio", "Vancouver", "Seattle", "London", "Barcelona", "Reykjavik"]
sorted_cities_by_len = sorted(cities, key=len)
print(sorted_cities_by_len)
print("="*50)

"""Sorting by values in difficult structures"""

books = (
    ("Lord of the Rings", "Tolkien R.R.", 1200),
    ("Marketing wars", "El Rise, Jack Traut", 230),
    ("Ghost in the Shell", "Japan Classics", 301),
    ("SCIP", "USA University", 678)
)

# to sort 'books' tuple by last parameter (represents pages):

b = sorted(books, key=lambda x: x[-1]) #sort ASC by last param
print(b)


