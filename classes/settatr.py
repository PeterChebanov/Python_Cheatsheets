class Point:
    color = 'red'
    circle = 2


Point.color = 'black'
print(Point.color)
print(Point.circle)

print(Point.__dict__)
print(hasattr(Point, 'prop'))  # False
print(hasattr(Point, 'circle'))  # True

Point.type_pt = 'prop'
print(Point.type_pt)  # prop

setattr(Point, 'type_ptt', 'square')  # the same as Point.type_ptt = square
print(Point.__dict__)

delattr(Point, 'type_pt')  # Delete atr

getattr(Point, 'type_pt',
        False)  # we can set what we receive in case the attribute does not exist -> False in this case

a = Point()
print(a.color)


# del a.color


# print(a.color) #Attribute Error

class ClassWithDoc(Point):
    """This class heritages class Point and contains doc"""


doc_a = ClassWithDoc()
print(doc_a.__doc__)
print(doc_a.color)  # black
doc_a.cat_name = "Vasiliy"
print(doc_a.__dict__)  # {'cat_name': 'Vasiliy'}
print("-" * 150)


class Vector:
    MIN_COORD = 0
    MAX_COORD = 100

    def __init__(self, x=0, y= 100):
        self.x = x
        self.y = y

    @classmethod
    def set_min(cls):
        cls.MIN_COORD = 10

    def __getattribute__(self, item):
        if item == 'x': # we can forbid access to exact attribute by this __getattribute__ method
            raise ValueError("Access is forbidden")
        else:
            print("executing __getattribute__")
            return object.__getattribute__(self, item)

    def __setattr__(self, key, value):
        if key == 'z':
            raise AttributeError("Forbidden name of the attribute")
        else:
            print("executing __setattribute__")
            return object.__setattr__(self, key, value)

    def __getattr__(self):#Define the behaviour of the program in case we appeal to non existing class/object attribute
        print("executing __getattr__")
        return False #Returns False in stead of AttrubuteError by default

    def __delattr__(self, item):
        print("executing __delattr__")
        object.__delattr__(self, item)



vec_1 = Vector()
vec_2 = Vector(y=101)

print(vec_2.y) # 101
print(vec_1.x) # access is forbidden

