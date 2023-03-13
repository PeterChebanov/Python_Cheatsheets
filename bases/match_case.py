"""Match case with tuples and lists with conditions"""

# book = ("Lord of the rings", "John R.R. Tolkien", 1200, "65$", 117647)
#
# match book:
#     case [str() as title, str() as author, int() as amount_of_pages, str() as price, *_ ] if len(book) >= 4 and len(author) <= 100:
#         print('-' * 200)
#         print("We have checked types of the each of the first 4 elements of the tuple , and have used '*_' syntax for unpacicng the rest of elements in the tuple we are not interested in at the moment")
#         print("We also have checked if the len of the TITLE <= 100 and len of the AUTHOR name >= 4 satisfy condition to execute case in match")
#         print('-' * 200)
#     case other:
#         print("Nothing happens")


"""Joining two different checks in one case"""

#In case we can expect 2 different types:

#books = ("Lord of the rings", "John R.R. Tolkien", 1200, "65$")
books = (117647, "Lord of the rings", "John R.R. Tolkien", 1200, "65$", "3 parts in 3 different books")


match books:
    case list(): #Checking to the correct data format
        print("Tuple expected, DataFormat Error")
    case [book_title, author, book_price] | [_, book_title, author, book_price, *_]: # second condition of second case will work because in the first one we strictly expect only 3 elements, and receiving 6 elements
        print(f"Title: {book_title}, author: {author}, price: {book_price} ")
    case _: #wildecard
        print("Непонятно...")
