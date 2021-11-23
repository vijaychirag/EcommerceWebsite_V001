''' # self is keyword : self is a object reference, who is calling you
    # instance and class variables have a whole different concepts
    # Constructors is a methods, which is automatically called or created, when we creats objects for any classes
    # syntax for constructors: __init__(self)
    # class variables are attached with class name while calling in object creation
    #  similarly instance variables are attached with self keywords, it is mandatory'''

class Calculator():

    num = 99

    def __init__(self, c, d):
        self.first = c
        self.second = d
        print( self.first + self.second + Calculator.num)
        print("I will creat automatically ")

    def getdata(self):
        print(" excuting the getdata method in the calculator classes")

    def summation(self, a, b):
        self.firstnum = a
        self.secondnum = b
        return self.firstnum + self.secondnum + Calculator.num


obj = Calculator(2, 5)
obj.getdata()
print(obj.num)

obj1 = Calculator(5,9)
obj1.summation()
print(obj1.summation)