# classes are user defined blueprints or prototype:
'''class contains methods, self keywords, class variables, instance variables, inheritance
 abstractions, encapsulations, polymorphism
 objects creations for classes
 functions and methods are same: when we declare methodlogy into the class it is called as methods
  and without the class, we are calling a methods it is called as function
  # '''


class Calculator():

    num = 99

    def getdata(self):
        print(" excuting the getdata method in the calculator classes")

obj = Calculator()
obj.getdata()
print(obj.num)



