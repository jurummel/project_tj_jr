import json

import sklearn as sk
import pandas as pd
import numpy as np
import django as dj
import json as js

movies = pd.read_csv("/Users/julian/Documents/project_new_TJ/pythonProject/Data/movies_metadata.csv")
movies = movies[movies["status"]=="Released"]
df_name_genre = movies[["title", "genres"]]
df_name_genre = df_name_genre[df_name_genre["genres"].str.len()>2]

genres_id_classification = {}
help_list=[]
idents = []

#pd.json_normalize(df_name_genre["genres"])
#print(genres_id_classification)

for genre_list in df_name_genre["genres"]:
    print(genre_list)
    for char in range(0, len(genre_list)-2):
        if genre_list[char] == "i" and genre_list[char+1] == "d" and genre_list[char+2] == "'":
            char += 5
            while genre_list[char] != ',':
                print(genre_list[char])
                help_list.append(genre_list[char])
                idents.append(' '.join(help_list))
                help_list = []
                char += 1
        else:
           pass

print(idents)

