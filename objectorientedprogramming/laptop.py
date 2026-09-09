class Laptop:
    name : str
    brand : str
    price : int
    def open(self):
        print("laptop is open")
    def game(self):
        print("laptop have games")
    def close(self):
        print("laptop is closed")

lenovo_instance = Laptop()
hp_instance = Laptop()
hp_instance.open()
lenovo_instance.game()