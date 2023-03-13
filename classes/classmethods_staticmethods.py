class Vector:
    MIN_COORD = 0
    MAX_COORD = 100

    @classmethod #Use when we need to work with fields of the class directly
    def validate(cls, arg):
        return cls.MAX_COORD <= arg <= cls.MAX_COORD

    def __int__(self, x, y):
        self.x = self.y = 0
        if self.validate(x) and self.validate(y):
            self.x = x
            self.y = y

    def get_coord(self):
        return self.x, self.y

    @staticmethod
    def sum_of_power(x, y): #Use when we need to work with separated(abstract) parameters of the func which
        return x*x + y*y    #are not a part of the class or object -->> Service Function


