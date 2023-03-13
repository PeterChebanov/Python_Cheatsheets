class Point:
    color = "red"
    circle = 2

    def set_cords(self, x, y):  # self - is a link to the concrete object
        self.x = x
        self.y = y

    def get_cords(self):
        return (self.x, self.y)


class ThreeD_point():
    """class represents 3D point"""

    def __new__(cls, *args, **kwargs):  # cls -> links to the class, not to the object
        """Example of use of this method - working with singleton pattern, when we have to check if the object of the
        class is already created. IF created, we can forbid to create the second object of the class"""
        print(f"This method is called right before the object of the class is going to be created")
        print(f"Calling __new__ для {str(cls)}")
        return super().__new__(cls)  # return super from Base class to have a link of the current class

    def __init__(self):
        print("This method is called right after the object of class was created")
        print(f"Calling init для {str(self)}")
        self.x = 0
        self.y = 0
        self.z = 0

    def __del__(self):
        print("Happens before the object of the class will be deleted")
        print(f"Deleting the object of the class {str(self)}")

    def set_cords(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def get_coords(self):
        return self.x, self.y


point_1 = ThreeD_point()
print(point_1)  # None => if there is no return super()__new__(cls) in def __new__. Overwise returns results of


# 3 methods work => __new__, __init__, __delete__ (in case the link will not be in use after)


class DataBase:  # Example of SINGLETON =>

    __instance = None  # if no object of class created == None, else == link to the created object

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)  # creates new object and assigns the link to __instance

        return cls.__instance  # returns current instance or created instance if new was created

    def __del__(self):
        __instance = None  # set instance to None if object of class will be deleted

    def __init__(self, user, psw, port):
        self.user = user
        self.psw = psw
        self.port = port

    def connect(self):
        print(f"Connecting to BD")

    def close(self):
        print(f"Closing connection with BD")

    def read(self):
        return "Data from BD"

    def write(self, data):
        print(f"write to DB {data}")
