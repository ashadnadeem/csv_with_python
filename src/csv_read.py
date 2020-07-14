#Author:Ashad Nadeem
#Date:27-6-2020

# Reading existing CSV File
import csv
f = open("friends.csv")
csv_f = csv.reader(f)
for row in csv_f:
    name,institute = row
    print("{} studies in {}".format(name,institute))
f.close()
