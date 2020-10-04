# # Takes in a directory path filled with images. 
# # Makes a sub directory called "small" and fills it with small square versions of the imgs
# # spits out the html code to be added to the site

# import os

# # path = input("Enter path to folder")

# path = '/Users/mitch/Documents/ep-lug/collaborations/Secret_Santa_2018'

# # stuff = os.walk(path)

# for root, dirs, files in os.walk(path, topdown=False):
#    for name in files:
#       print(os.path.join(root, name))
#    for name in dirs:
#       print(os.path.join(root, name))

# Go to the eplug flickr group and click on first photo
# Download Large and Small versions of each photo until it lands on a url it has already downloaded
# Keep track of images already downloaded in a csv.

FIRST_PHOTO_URL = "https://www.flickr.com/photos/134183198@N05/50310500902/in/pool-14665180@N23/"

# <a class="navigate-target navigate-next" href="/photos/_czq_/50284628786/in/pool-14665180@N23/" title="Heavy Duty | by _CZQ_" data-track="nextPhotoButtonClick" data-action="ad" style="height: 591px;"><span class="hide-text">→</span></a>

from bs4 import BeautifulSoup

