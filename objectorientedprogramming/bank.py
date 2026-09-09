class Bank:
    acc_no : int
    balance : float
    acc_type : str
    customer_name : str

    def __init__(self,acc_no,balance,acc_type,customer_name):
        self.acc_no = acc_no
        self.balance = balance
        self.acc_type = acc_type
        self.customer_name = customer_name

        print("your account has been created")

    def deposit(self,amount):
        self.balance +=amount
        print(f"your {self.acc_no} has beeen credited with {amount} available balance is {self.balance}")

    def withdraw(self,amount):
        if self.balance < amount:
            raise Exception ("insufficient balance")
        else:
            self.balance -= amount
        print(f"your {self.acc_no} has beeen debied with {amount} available balance is {self.balance}")
        

    def get_balance(self):
        print("your avail balnce is",self.balance)

bank_instance1 = Bank(3245,3000,"current","yadhu")
bank_instance1.deposit(1000)
bank_instance1.withdraw(2000)
bank_instance1.get_balance()




        
        








