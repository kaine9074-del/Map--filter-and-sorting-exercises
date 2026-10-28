movies = [ 

    ("The Matrix", 1999), 

    ("Avatar", 2009), 

    ("Jurassic Park", 1993), 

    ("Avengers: Endgame", 2019), 

    ("Inception", 2010), 

    ("Titanic", 1997) 

]

movies.sort(key=lambda movies: movies[1], reverse=True)

print("Movies from newest to Oldest: ")
for name, year in movies:
    print(f"{name} - {year}")