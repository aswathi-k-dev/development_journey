from mysql import connector

class InventoryCreateLListRetrieveUpdateDelete:

    def __init__(self,user = None,password = None):

        if user == None or password == None:
            raise Exception("username and password required")

        self.connection = connector.connect(
            user = user,
            password = password,
            host = "localhost",
            database = "inventory_db"
        )

        self.cursor = self.connection.cursor()

    def post(self,**kwargs):
    
        db_cols = ("name","sku","category","quantity","price","status")
    
        difference = set(db_cols).difference(kwargs.keys())
    
        if difference:
            raise Exception(f"{difference} required")
    
        col_str = ",".join(db_cols)
        query = f"""insert into inventory ({col_str}) values(%s,%s,%s,%s,%s,%s)"""
    
        values = list(kwargs.values())
        self.cursor.execute(query,values)
        self.connection.commit()
        print("record added")


    def get(self):
        query = "select * from inventory"
        self.cursor.execute(query)
        records = self.cursor.fetchall()
        for items in records:
            print(items)

    def retrieve(self,id = None):
        query = "select * from inventory where id = %s"
        values = (id,)
        self.cursor.execute(query,values)
        record = self.cursor.fetchone()
        print(record)

    def put(self,id = None,**kwargs):
        place_holder = ""
        for k in kwargs.keys():
            place_holder+=k+"=%s,"
        place_holder = place_holder.rstrip(",")
    
        query = f"update inventory set {place_holder} where id = %s"
        values = list(kwargs.values())
        values.append(id)
        self.cursor.execute(query,values)
        self.connection.commit()
        print("record updated")

    def filter(self,**kwargs):
            place_holder = ""
            for k in kwargs.keys():
                place_holder +=k+"= %s and"
            place_holder = place_holder.rstrip("and ")
            query = f"select * from inventory where {place_holder} "
            values = list(kwargs.values())
            self.cursor.execute(query,values)
            records = self.cursor.fetchall()
            if records:
                for i in records:
                    print(i)
            else:
                print("no records")


    def summary(self):
    
        query = "select status,count(*) as count from inventory group by status"
    
        self.cursor.execute(query)
    
        response = self.cursor.fetchall()
    
        category_summary_query = "select category,count(*) as count from inventory group by category"
    
        self.cursor.execute(category_summary_query)
    
        category_summary = self.cursor.fetchall()
    
        print("category summary",category_summary)
    
        print(response)

inventory_instance = InventoryCreateLListRetrieveUpdateDelete(user = "root",password = "Password@123")
"""inventory_instance.post(
    name="Keyboard",
    sku="KB001",
    category="Electronics",
    quantity=20,
    price=1200,
    status="Available"
)"""

#inventory_instance.get()

#inventory_instance.retrieve(id = 2)

#inventory_instance.put(id = 2,status = "Low Stock")

#inventory_instance.filter(category = "Electronics")

inventory_instance.summary()