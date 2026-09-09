class Employee:
    def __init__(self,id,name,salary,phone,department):
        self.id = id
        self.name = name
        self.salary = salary
        self.phone = phone
        self.department = department
    def get_employee(self):
        print(self.id,self.name,self.salary,self.phone,self.department)


employee1_instance = Employee(1,"abhi",25000,98463267,"it")
employee2_instance = Employee(2,"yadhu",30000,567421345,"cs")


employee1_instance.get_employee()
employee2_instance.get_employee()