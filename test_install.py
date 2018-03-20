#!/usr/bin/env python
import cv2
"""
A simplest script testing whether the OpenCV library
has been installed successfully or not 
"""
def test():
    Img = cv2.imread("pyimagesearch_gurus_logo.png")
    cv2.imshow("Test Image", Img)
    cv2.waitKey(0)
test()
