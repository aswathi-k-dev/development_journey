# multilevel inheritance

class GrandParent:
    def properties(self):
        print("2 acres land...")

class Parent(GrandParent):
    def home(self):
        print("1500 sqft house")

class Child(Parent):
    def social_media_account(self):
        print("social media account")

child_instance = Child()
child_instance.social_media_account()
child_instance.home()
child_instance.properties()