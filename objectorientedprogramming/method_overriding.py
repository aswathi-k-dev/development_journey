""" 
method overriding : child class redefine the method that is already defined in the parent class

"""

class Parent:
    def mobile(self):
        print("redmi")

class Child(Parent):
    def mobile(self):
        print("iphone 17")

child_instance = Child()
child_instance.mobile()



