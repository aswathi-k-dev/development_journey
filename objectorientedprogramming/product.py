class Product:
    def __init__(self,id,name,category,price,quantity):
        self.id = id
        self.name = name
        self.category = category
        self.price = price
        self.quantity = quantity
    def get_product(self):
        print(self.id,self.name,self.category,self.price,self.quantity)

product_1 = Product(131,"phone","gadgets",25000,2)
product_2 = Product(122,"watch","accessories",2300,1)
product_2.get_product()
product_1.get_product()