# file = open('episode_1.txt', encoding='utf-8')
# print(file.read())
# file.close()
# print('==='*50)
# file = open('episode_1.txt', encoding='utf-8')
# print(file.read(5)) #read first 5 symbols
# print(file.read(4)) #read next 4 symbols
# print(file.read()) #read the rest of the symbols
# print(file.seek(0)) # return caret to the set position, if set to 0 -> return to the beginning symbol
# print(file.read(10))
# print(file.tell()) # return current position of the caret (in bytes -> fe (1 russian letter takes 2 bytes, so if 4 symbols were red, the number of the position will be 8)
# print(file.seek(0))
# print(file.readline()) #read first line of the file -> will put \n at the end of each line
# print(file.readline(), end="") # end="" will delete \n at the end of the line
# file.close()
#

try:
    file_1 = open('episode_3.txt', encoding='utf-8')
    text = file_1.readlines()
    print(text)
    file_1.close()
except FileNotFoundError as e:
    print(e.strerror)

try:
    with open("my_file.txt", encoding="utf-8") as file:
        s = file.readlines()
        print()
except FileNotFoundError as e:
    print(e.strerror)

try:
    with open("written.txt", "w") as writer: #when we open file on write only ('w') we delete all previous info in the file
        writer.write("New episode of Star Wars is coming soon, have a look to the afisha")
        writer.write("1234") #will display 1234 sticked to the first line, to avoid it use '\n' in the end of each string
        writer.write("\nThis line will on the new line of the previous 2 lines and the next one will be on the new line\n")
except FileNotFoundError as e:
    print(e.strerror)

try:
    with open("written.txt", "a") as appender: #append text to existed file or create new file if it was not exist
        appender.write("The tickets for the new episode should not be very expensive")
except FileExistsError as e:
    print(e.strerror)

try:
    with open("written.txt", "a+") as appender: #gives opportunity to read and write to file simultaneously
        appender.seek(0)#position only for read file from the begining, next line will be written to the end of the file
        appender.write("The tickets for the new episode should not be very expensive")
        s = appender.readlines()
        print(s)
        w = appender.writelines(["Ticket for first week will cost 15.99$\n",
                                 "Ticket for second week will cost 11.99$\n"])#write a number of lines in one time
except FileExistsError as e:
    print(e.strerror)


books = [
    ("Lord of the Rings", "Tolkien", 1200),
    ("Marketing Wars", "HZkto", 150),
    ("Harry Potter", "Rowling", 2500),
]

import pickle

try:
    with open("books.bin", "wb") as file:
        pickle.dump(books, file)
except FileNotFoundError as e:
   print(e.strerror)

try:
    with open("books.bin", "rb") as file:
        library = pickle.load(file)
        print(library)
except FileNotFoundError as e:
    print(e.strerror)