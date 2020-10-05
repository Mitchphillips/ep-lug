# PATH = input("Enter the path to your images")
PATH = "../collaborations/Secret_Santa_2019/images/"
import os 

# Check to make sure the path exists and is writeable
# if os.access(PATH, os.W_OK):
#     print("Path is ok")
# else:

# Get list of images in DIR with os walk

from PIL import Image

images = []

for root, dirs, files in os.walk(PATH):
    for file in files:
    	if file[-3:] == 'jpg' and file[-9:-4] != 'thumb':
    		images.append(file)
        # print(len(path) * '---', file)


# Make a thumbnail size image with _thumb at end of name
for image_path in images :
	img = Image.open(PATH + image_path)

	img.thumbnail((2000, 400))
	img.save(PATH + image_path[:-4] + '_thumb.jpg')
	print("<a href='images/" + image_path + "' data-lightbox='mygallery'><img src='images/"+image_path[:-4] + '_thumb.jpg' +"'></a>")


# todo pass in a flickr gallery url and get all the images from it