"""
polymporphism : more than one form

 method overloading
 method_overriding


  method overloading : same method name diffrent no of parametres

"""

class Calculator:
    def add(self,num1,num2):
        print(num1+num2)
    def add(self,num1,num2,num3):
        print(num1+num2+num3)
    def add(self,num1,num2,num3,num4):
        print(num1+num2+num3+num4)

cal_instance = Calculator()
cal_instance.add(10,20,30,40)
cal_instance.add(12,13)