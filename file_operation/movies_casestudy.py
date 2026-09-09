fr = open("file_operation\\movie-v2.csv","r",encoding = "utf-8")
movies = []
for line in fr:
    line = line.rstrip("\n")
    id,title,language,year,run_time,rating,genre = line.split(",")
    movie_dict = {"id:",id,
                  "title:",title,
                  "language:",language,
                  "year:",year,
                  "run_time:",run_time,
                  "rating:",rating,
                  "gemre:",genre
                  }
    movies.append(movie_dict)
print(len(movies))