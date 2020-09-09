# Takes in a directory path filled with images. 
# Makes a sub directory called "small" and fills it with small square versions of the imgs
# spits out the html code to be added to the site

import os

# path = input("Enter path to folder")

path = '/Users/mitch/Documents/ep-lug/collaborations/Secret_Santa_2018'

# stuff = os.walk(path)

for root, dirs, files in os.walk(path, topdown=False):
   for name in files:
      print(os.path.join(root, name))
   for name in dirs:
      print(os.path.join(root, name))