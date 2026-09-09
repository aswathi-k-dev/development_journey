movies = [["kgf","kannada",150,2007,8],
          ["balan","malayalam",146,2026,8],
          ["aanandam","malayalam",130,2007,8],
          ["bigb","malayalam",150,2004,8],
          [3,"tamil",145,2005,8]
          ]
          
    

# dispaly runtime,year,rating of bigb

print(movies[3][2:])


#display all movie titles

all_movies = [m[0] for m in movies]
print(all_movies)

#display all movie years

all_years = {m[3] for m in movies}
print(all_years)

# display all languages

all_languages = {m[1] for m in movies}
print(all_languages)