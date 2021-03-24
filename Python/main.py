#inheritence
class Dog(object):
    def __init__(self, name, age): #constructor, it runs everytime class called, you can define default variables here
        self.name = name
        self.age = age

    def speak(self):
        print("""Hi I am""", self.name, "I am", self.age, "years old")
    def talk(self):
        print("bow")

class Cat(Dog):
    def __init__(self, name, age, color):
        super().__init__(name, age)
        self.color = color
    def speak(self):
        print("""Hi I am""", self.name, "I am", self.age, "years old", "I am of color", self.color)
    def talk(self):
        print("meaw")

#Method overloading
class Integer(object):

    def __init__(self, value=0):
        self._value = int(value)

    # default methods that we can overload on classes
    def __add__(self, other):
        if isinstance(other, Integer):
            return Integer(self._value + other._value)
        return Integer(self._value + other)

    def __iadd__(self, other):
        if isinstance(other, Integer):
            self._value += other._value
        else:
            self._value += other
        return self

    def __sub__(self, other):
        if isinstance(other, Integer):
            return Integer(self._value - other._value)
        return Integer(self._value - other)

    def __isub__(self, other):
        if isinstance(other, Integer):
            self._value -= other._value
        else:
            self._value -= other
        return self

    def __mul__(self, other):
        if isinstance(other, Integer):
            return Integer(self._value * other._value)
        return Integer(self._value * other)

    def __div__(self, other):
        if isinstance(other, Integer):
            return Integer(self._value / other._value)
        return Integer(self._value / other)

    def __str__(self):
        return str(self._value)

    def __int__(self):
        return self._value

    def __float__(self):
        return float(self._value)

    def __repr__(self):
        return 'Integer(%s)' % self._value

#Method overloading
# #2D points

class Point():
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
        self.coordinates = (self.x, self.y)
    #default methods that we can overload on classes
    def __add__(self, p):
        return Point(self.x + p.x, self.y+p.y)
    def __sub__(self, p):
        return Point(self.x - p.x, self.y - p.y)
    def __mul__(self, p):
        return self.x * p.x + self.y * p.y
    # points comparision
    def length(self):
        import math
        return math.sqrt(self.x**2 + self.y**2)
    def __gt__(self, p): #greater than
        return self.length() > p.length()
    def __ge__(self, p): #>=
        return self.length() >= p.length()
    def __lt__(self, p): #<
        return self.length() < p.length()
    def __le__(self, p): #<=
        return self.length() <= p.length()
    def __eq__(self, p): #=
        return self.x == p.x and self.y == p.y
    # to make default output to string from class
    def __str__(self):
        return "{" + str(self.coordinates) + "}"

# class methods, static methods, class variables
class Dogg:
    # class variables instead of initializing at __init__ constructor
    color = "green"
    def __init__(self, name):
        self.name = name
    def talk(self):
        print("Hi, My name is", self.name, ", My color is", self.color)
    @classmethod
    def color_dog(cls):
        return cls.color

    #to create fuctions callable within the class
    @staticmethod
    def bark(n):
        for _ in range(n):
            print("BoW!")

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    k = Cat("nasir", 10, 'red')
    k.speak()
    k.talk()
    j = Dog("kousi", 9)
    j.speak()
    j.talk()
    a = Integer(2)
    print(type(a))
    print(a+2)
    print(a * 22)

    p1 = Point(3,
               4)
    p2 = Point(3,
               2)
    p3 = Point(1,
               3)
    p4 = Point(0,
               1)
    print(p1 + p2)
    print(p1 - p2)
    print(p1 * p2)
    print(p1 + p2 + p3 + p4)

    print(p1 == p2)
    print(p1 > p2)
    print(p4 <= p3)

    k = Dogg("Johnny")
    k.talk()
    #with static metods no need for objects creation for class and class t be called
    print(Dogg.color_dog())
    Dogg.bark(5)






