__author__ = "Ashad Nadeem"
__date__ = "$Jul 14, 2020 5:57:14 PM$"

import csv
friends = [["Ashad","IBA"],
           ["Ali","GapYear"],
           ["Burhan","LUMS"],
           ["Taha","NED"]
          ]
friends_csv = open("friends.csv","w")
writer = csv.writer(friends_csv)
writer.writerows(friends)
print("Write coplete!")
#Using with function you dont need to close the file
friends_csv.close()