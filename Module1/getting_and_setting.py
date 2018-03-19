#!/usr/bin/env python
import cv2
import argparse

# construct the argument parser and parse the arguments
AP = argparse.ArgumentParser()
AP.add_argument('-i', '--image', required=True, help="Path of the image")
args = vars(AP.parse_args())

# load the image, grab its dimensions, and show it
image = cv2.imread(args['image'])
h,w = image.shape[:2]
cv2.imshow('Original', image)
cv2.waitKey(0)
# images are just NumPy arrays. The top-left pixel can be found at (0, 0)
b,g,r =  image[0,0]
print('Pixel at (0, 0) - Red: {r}, Green: {g}, Blue: {b}'.format(r=r, g=g, b=b))

# now, let's change the value of the pixel at (0, 0) and make it red
image[0, 0] = (0, 0, 255)
(b, g, r) = image[0, 0]
print("Pixel at (0, 0) - Red: {r}, Green: {g}, Blue: {b}".format(r=r, g=g, b=b))\

# compute the center of the image, which is simply the width and height
# divided by two
(cX, cY) = (w // 2, h // 2)
# since we are using NumPy arrays, we can apply slicing and grab large chunks
# of the image -- let's grab all four corners
tl = image[:cY, :cX] 
tr = image[:cY, cX:w]
ll = image[cY:h, :cX]
lr = image[cY:h, cX:w]
#cv2.imshow("Top-Left Corner", tl)
#cv2.imshow("Top-Right Corner", tr)
#cv2.imshow("Bottom-Right Corner", lr)
#cv2.imshow("Bottom-Left Corner", ll)

#make the lower right part blue
image[cY:h,cX:w] = 255, 0, 0
# Show our updated image
cv2.imshow("Updated", image)
cv2.waitKey(0)
