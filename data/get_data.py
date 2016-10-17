from imdb import IMDb
ia = IMDb()

import xmltodict, json

movies = open("storage/my_movies.txt", "r").read().split('\n')
all_movies = []

json_to_create = open("storage/my_movies.json", "w")

x = 0

for m in movies:
  try:
    int(m[2:9])
    ia_movie = ia.get_movie(m[2:9]).asXML()
    o = xmltodict.parse(ia_movie)
    o["my_rating"] = m[15:16]
    all_movies.append(o)
    x = x + 1
    print(x)
  except ValueError:
    print("Oops! That was no valid number. Try again!")

print(len(all_movies))

obj = {
  "movies": all_movies
}
json_to_create.write(json.dumps(obj))
