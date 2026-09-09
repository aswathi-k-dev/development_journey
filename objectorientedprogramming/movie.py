class Movie:
    def __init__(self,title,language,year,director,genre):
        self.title = title
        self.language = language
        self.year = year
        self.director = director
        self.genre = genre
    def get_movie(self):
        print(self.title,self.language,self.year,self.director,self.genre)

saiyara_instance = Movie("saiyara","hindi",2025,"mohit","romantic")
saiyara_instance.get_movie()