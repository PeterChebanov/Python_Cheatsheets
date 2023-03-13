class Point():
    def __init__(self, x=0, y=0):
        self._x = x  # _x is protected field
        self._y = y  # _y is protected field


class ThreeDPoint():
    def __init__(self, x=0, y=0):
        if self.__check_value(x) and self.__check_value(y):
            self.__x = x
            self.__y = y

    @classmethod
    def __check_value(cls, x):
        return type(x) in (int, float)

    def set_coord(self, x, y):
        if self.__check_value(x) and self.__check_value(y):
            self.__x = x
            self.__y = y
        else:
            raise ValueError("Coordinates have to be numbers")

    def get_cord(self):
        return self.__x, self.__y


point_1 = ThreeDPoint()
point_1.set_coord(22, 11.5)
print(point_1.get_cord())  # (22, 11.5)

#To access to protected methods of fields it is enough to do:
print(point_1._ThreeDPoint__x) #by this line we ignore double underscore of private field and get access to it


"""Another way to protect data --> more strict way"""

from accessify import private, protected

class JustPoint():
    def __init__(self):
        self.x = self.y = 0

    @private
    def set_x_to_five(self):
        self.x = 5


point_2 = JustPoint()

try:
    point_2.set_x_to_five()
except:
    print("No permissions")


try:
    point_2._JustPoint__x # will not be executed also
except:
    print("No permissions")



