from mysql import connector 

class PatientsCreateLListRetrieveUpdateDelete:

    def __init__(self,user = None,password = None):

        if user == None or password == None:
            raise Exception("username and password required")

        self.connection = connector.connect(
            user = user,
            password = password,
            host = "localhost",
            database = "hospital_db"
        )

        self.cursor = self.connection.cursor()


    def post(self,**kwargs):
    
        db_cols = ("patient_name","phone_number","assigned_doctor","department","appointment_date","status","consultation_fee")
    
        difference = set(db_cols).difference(kwargs.keys())
    
        if difference:
            raise Exception(f"{difference} required")
    
        col_str = ",".join(db_cols)
        query = f"""insert into patients ({col_str}) values(%s,%s,%s,%s,%s,%s,%s)"""
    
        values = list(kwargs.values())
        self.cursor.execute(query,values)
        self.connection.commit()
        print("record added")

    def get(self):
        query = "select * from patients"
        self.cursor.execute(query)
        records = self.cursor.fetchall()
        for patients in records:
            print(patients)

    def retrieve(self,patient_id = None):
           query = "select * from patients where patient_id = %s"
           values = (patient_id,)
           self.cursor.execute(query,values)
           record = self.cursor.fetchone()
           print(record)

    def put(self,patient_id = None,**kwargs):
        place_holder = ""
        for k in kwargs.keys():
            place_holder+=k+"=%s,"
        place_holder = place_holder.rstrip(",")
    
        query = f"update patients set {place_holder} where patient_id = %s"
        values = list(kwargs.values())
        values.append(patient_id)
        self.cursor.execute(query,values)
        self.connection.commit()
        print("record updated")

    def filter(self,**kwargs):
        place_holder = ""
        for k in kwargs.keys():
            place_holder +=k+"= %s and"
        place_holder = place_holder.rstrip("and ")
        query = f"select * from patients where {place_holder} "
        values = list(kwargs.values())
        self.cursor.execute(query,values)
        records = self.cursor.fetchall()
        if records:
            for p in records:
                print(p)
        else:
            print("no records")
  

patient_instance = PatientsCreateLListRetrieveUpdateDelete(user = "root",password = "Password@123")
""" patient_instance.post(
    patient_name = "arun",
    phone_number = 9846789012,
    assigned_doctor = "Dr.jhon",
    department = "ENT",
    appointment_date = "2026-08-20",
    status = "completed",
    consultation_fee = 250
) """
#patient_instance.get()
#patient_instance.retrieve(patient_id = 1)
#patient_instance.put(patient_id=1,status = "pending")
#patient_instance.filter(patient_name = "arun")


