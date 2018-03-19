#!/usr/bin/env python
import numpy as np 
import cv2

canvas = np.zeros((300,300,3),dtype="uint8")

#draw a green line from top left to bottem right 
green = 0,255,0
cv2.line(canvas, (0,0),(300,300),green,5)
cv2.imshow("Canvas",canvas)
cv2.waitKey(0)

# now, draw a 3 pixel thick red line from the top-right corner to the
# bottom-left
red = (0, 0, 255)
cv2.line(canvas, (300, 0), (0, 300), red, 5)
cv2.imshow("Canvas", canvas)
cv2.waitKey(0)

# draw a green 50x50 pixel square, starting at 10x10 and ending at 60x60
my_blue = (255,100,25)
cv2.rectangle(canvas, (10, 10), (60, 60), (255,100,25),5)
cv2.imshow("Canvas", canvas)
cv2.waitKey(0)
# let's draw one last rectangle: blue and filled in
blue = (255, 0, 0)
cv2.rectangle(canvas, (200, 50), (225, 125), my_blue, -1)
cv2.imshow("Canvas", canvas)
cv2.waitKey(0)

# reset our canvas and draw a white circle at the center of the canvas with
# increasing radii - from 25 pixels to 150 pixels
canvas = np.zeros((1000, 1000, 3), dtype="uint8")
center = canvas.shape[1]//2, canvas.shape[0]//2
white = (255,255,255)

for r in range(0,175,25):
    cv2.circle(canvas,center,r,white,3)
cv2.imshow('Canvas',canvas)
cv2.waitKey(0)
# let's go crazy and draw 25 random circles
for i in range(25):
	# randomly generate a radius size between 5 and 200, generate a random
	# color, and then pick a random point on our canvas where the circle
	# will be drawn
    radius = np.random.randint(5,200)
    color = np.random.randint(0,256,(3,)).tolist()
    pt = np.random.randint(0, high=300, size = (2,))

    # draw random circle
    cv2.circle(canvas, tuple(pt), radius, color, -1)
    # Show our work
cv2.imshow("Canvas", canvas)
cv2.waitKey(0)

# load the image of Adrian in Florida
image = cv2.imread("florida_trip.jpg")
 
# draw a circle around my face, two filled in circles covering my eyes, and
# a rectangle surrounding my mouth
cv2.circle(image, (168, 188), 90, (0, 0, 255), 2)
cv2.circle(image, (150, 164), 10, (0, 0, 255), -1)
cv2.circle(image, (192, 174), 10, (0, 0, 255), -1)
cv2.rectangle(image, (134, 200), (186, 218), (0, 0, 255), -1)
 
# show the output image
cv2.imshow("Output", image)
cv2.waitKey(0)