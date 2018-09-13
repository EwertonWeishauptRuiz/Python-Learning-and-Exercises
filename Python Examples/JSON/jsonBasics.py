import json
# Prints all methods from json
print(dir(json))
# Uses UTF-8 as enconding, since the file can contain non ASCII characters and that can create
# an problem while reading the data.
json_file = open("movie_1.txt", "r", encoding="utf-8")
movie = json.load(json_file)
print("\nType of object json_object" + str(type(movie)) + "\n")
json_file.close()
print(movie)

#Since this is a dictionary, you can access the value by key:
print("\nThe title of the movie is " + movie["title"])

# To convert the dictionary into a valid JSON string
# Will concerth the non ASCII characters to unicode
json.dumps(movie)
# To preserve the non ASCII characters intact
json.dump(movie, ensure_ascii=False)