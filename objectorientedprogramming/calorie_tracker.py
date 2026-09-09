"""user foodlogs

create|add = post
list:all = get
update = put
detail = retrieve
remove = delete

"""

class DietLens:
    def __init__(self):
        self.food_logs=[
            {"id":1,"name":"dosa","calorie":170,"owner":"hari"},
            {"id":1,"name":"dosa","calorie":170,"owner":"hari"},
            {"id":1,"name":"dosa","calorie":170,"owner":"hari"},
            {"id":1,"name":"dosa","calorie":170,"owner":"hari"}
        ]
    def post(self,**kwargs):
        required_fields = {"id","name","calorie","owner"}
        missing_fields = required_fields.difference(kwargs.keys())
        if missing_fields:
            raise ValueError(missing_fields,"are missing")
        else:
            self.food_logs.append(kwargs)
            print("record has been added")

    def get(self):
        if len(self.food_logs) == 0:
            print("no records found")
        else:
            for log in self.food_logs:
                print(log)

    def retrieve(self,id = None):
        if not id:
            raise ValueError("id missing")
        else:
            return[log for log in self.food_logs if log.get("id")==id]

    def put(self,id = None,**kwargs):
        log = [log for log in self.food_logs if log.get("id")== id][0]
        log.update(kwargs)
        print("record has been added")
        print(log)

    def delete(self,id = None):
        log = [log for log in self.food_logs if log.get("id")== id][0]
        self.food_logs.remove(log)
        print("food record deleted")
        self.get()



        

diet_instance = DietLens()
diet_instance.post(id=2,name="idly",calorie = 180,owner = "yadhu")
diet_instance.post(id=3,name = "appam",calorie = 150,owner = "vismya")
print(diet_instance.retrieve(id=4))
print(diet_instance.put(id=1,name = "biryani"))
diet_instance.delete(id = 1)
