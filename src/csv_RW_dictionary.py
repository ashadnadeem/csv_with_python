#Author:Ashad Nadeem
#Date:27-6-2020

# Reading & Writing CSV File with dictionaries
import csv
Shows = [{"name":"Breaking Bad","IMDB":9.5,"Seasons":5},
         {"name":"Prison Break","IMDB":8.3,"Seasons":5},
         {"name":"The Blacklist","IMDB":8,"Seasons":7},
         {"name":"Friends","IMDB":8.9,"Seasons":10}]
keys = ["name","IMDB","Seasons"]

with open("TV_shows.csv","w") as tvs:
    writer = csv.DictWriter(tvs,fieldnames = keys)
    writer.writeheader()
    writer.writerows(Shows)
    
# Write Complete Lets now check it

with open("TV_shows.csv") as tvsreader:
    reader = csv.DictReader(tvsreader)
    for row in reader:
        print("{} has IMDB rating of {} and has {} Seasons".format(row["name"],row["IMDB"],row["Seasons"]))
