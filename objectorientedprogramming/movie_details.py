class Movie:
    def __init__(self):
        self.movie_details=[
            {"id":1,"title":"premam","year":2015,"genre":"romance","rating":9,"run_time":150,"director":"alphonse"},
            {"id":2,"title":"drisym","year":2026,"genre":"thrillr","rating":8,"run_time":160,"director":"jeethu joseph"},
            {"id":3,"title":"bigb","year":2007,"genre":"action","rating":7,"run_time":146,"director":"amal"},
            {"id":4,"title":"premalu","year":2025,"genre":"romance","rating":8,"run_time":157,"director":"girish"}       
        ]

    def post(self,**kwargs):
        self.movie_details.append(kwargs)
        print("record has been added")

    def get(self):
        if len(self.movie_details)==0:
            print("no records")
        else:
            for m in self.movie_details:
                print(m)

    def retrieve(self,id = None):
        movies = [movies for movies in self.movie_details if movies.get("id")==id][0]
        print(movies)

    def put(self,id = None,**kwargs):
        movies = [movies for movies in self.movie_details if movies.get("id")==id][0]
        movies.update(kwargs)
        print("record has been added")
        print(movies)

    def delete(self,id = None):
        movies = [movies for movies in self.movie_details if movies.get("id")==id][0]
        self.movie_details.remove(movies)
        print("record deleted")
        self.get()

movie_instance = Movie()
movie_instance.post(id =5,title = "aaveshm",year = 2025,genre = "action",rating = 7,run_time = 160,director = "jithu")
movie_instance.get()
movie_instance.retrieve(id=4)
movie_instance.put(id =3,year = 2008,rating = 8)
movie_instance.delete(id = 4)




