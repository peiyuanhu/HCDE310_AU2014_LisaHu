## Exercises
## ---
import json

#hw5example.json
# used http://www.deanclatworthy.com/imdb/?q=movie+title+here to generate data

print "--- 1 ---"
##1. load the JSON file 'hw5example.json' and print its contents. it's a list of metadata about movies.
## after you are done, comment out the print statement (so it no longer prints)
f = json.load(open("hw5example.json"))
print f

print "--- 2 ---"
##2. print the first element of the JSON file. it's metadata about a movie.
## after you are done, comment out this exercise (so it no longer prints)
print f[0].keys()

print "--- 3 ---"
##3. print the keys and values in the format key: value of the first element of the json file 
#   (so the attributes of the first movie get printed).
#e.g., Title: Little Miss Sunshine
element = f[0]

for item in element.keys():
    print item + ": " + f[0][item] + "\n"

print "--- 4 ---"
##4. write a *function* to print only the title, genres, and IMDB rating, and Metascore for a movie
def getinfo(movie):
    l = ["Title", "Genre", "imdbRating", "Metascore"]
    
    for item in l:
        print item + ": " + movie[item]
    print "\n"
    
    

print "--- 5 ---"
##5. use the function from (4) to print the data for each movie
for item in f:
    getinfo(item)
