class Song:
    def __init__(self,id,movie_name,title,track_no,singer,duration):
        self.id = id
        self.movie_name = movie_name
        self.title = title
        self.track_no = track_no
        self.singer = singer
        self.duration = duration
    def get_song(self):
        print(self.id,self.movie_name,self.title,self.track_no,self.singer,self.duration)

song1_instance = Song(1,"saiyara","saiyara",1,"faheem",4)
song2_instance = Song(2,"aashiqui 2","tum hi ho",4,"arjith singh",5)
song1_instance.get_song()
song2_instance.get_song()