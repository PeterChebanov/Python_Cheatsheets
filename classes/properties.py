from string import ascii_letters

class Person:
    def __init__(self, full_name, age, citizen_id, role):
        self.verify_full_name(full_name)
        self.verify_age(age)
        self.verify_citizen_id(citizen_id)

        self.__full_name = full_name.split()
        self.__age = age
        self.__citizen_id = citizen_id
        self.__role = role

    @property
    def full_name(self):
        return self.__full_name

    @full_name.setter
    def full_name(self, full_name):
        self.__full_name = full_name

    @property
    def role(self):
        return self.__role

    @role.setter
    def role(self, role):
        self.verify_role(role) #validates received string
        self.__role = role

    @classmethod
    def verify_full_name(cls, full_name):
        if type(full_name) != str:
            raise TypeError("The name has to be String type")

        f = full_name.split()
        if len(f) == 0:
            raise TypeError("Incorrect format of the name")

        letter = ascii_letters
        for word in f:
            if len(word.strip(letter)) != 0: #if all the symbols are correct, strip func will delete all of them from the string and return string of length == 0
                raise TypeError("There are symbols different of ascii allowed for the name")

    @classmethod
    def verify_age(cls, age):
        if type(age) != int or 14 > age > 120:
            raise TypeError("Age has to be int number between 14 and 120 years")

    @classmethod
    def verify_citizen_id(cls, id):
        if type(id) != str:
            raise TypeError("ID has to be numbers and letters in range 4 and 10 symbols")

        symbols = "1234567890 "
        splitted_id = id.split()

        for word in splitted_id:
            if len(word.strip(symbols)) != 0:
                raise TypeError("Not allowed symbols in ID")

        if len(splitted_id) != 2 or len(splitted_id[0]) != 4 or len(splitted_id[1]) != 6: #Check string of Id has format "xxxx xxxxxx"
            raise TypeError("Wrong format of the ID")

    @classmethod
    def verify_role(cls, role):
        if type(role) != str or 2 > len(role) > 150:
            raise TypeError("Role has to be string in range 2 and 150 symbols")





correct_name = Person("Petr Che", 37, '1234 543212', 'Automation QA')
#incorrect_name = Person("Petr Ch3", 36, "1234", "Manager") # fails with error: "There are symbols different of ascii allowed for the name"