import json
import numpy as np

json_data = open("storage/my_movies.json")
d = json.load(json_data)
all_movies = d["movies"]

all_names = []
all_my_ratings = []
all_ratings = []

for m in all_movies:
  try:
    all_names.append(m["movie"]["canonical-title"]["#text"])
    all_my_ratings.append(int(m["my_rating"]))
    all_ratings.append(float(m["movie"]["rating"]["#text"]))
  except KeyError:
    print("key error")

np_my_ratings = np.array(all_my_ratings)
np_ratings = np.array(all_ratings)

print(np.median(np_my_ratings))
print(np.median(np_ratings))

print(len(np_my_ratings))
