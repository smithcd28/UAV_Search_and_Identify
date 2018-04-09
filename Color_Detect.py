
import numpy as np
import argparse
import imutils
import time
import cv2


#input image
#construct the argument parse and parse the arguments 
ap = argparse.ArgumentParser()
ap.add_argument("-i","--image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])

#resize the image for faster processing time
image = imutils.resize(image, width=600)

cv2.imshow("Image",image)
#blur input image
blur = cv2.blur(image,(50,50),0)
#subtract blur from input image
sub = cv2.subtract(image,blur)
cv2.imshow("Result",sub)
#thresholding
ret, mask = cv2.threshold(sub,80,255,cv2.THRESH_BINARY)
gray = cv2.cvtColor(mask,cv2.COLOR_BGR2GRAY)
thresh = cv2.inRange(gray,1,255)

cv2.imshow("Thresh",thresh)

gray2 = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

#evaluate contours
_,contour, hier = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
if len(contour) != 0:
    for cnt in contour:
        x,y,w,h = cv2.boundingRect(cnt)
        cv2.rectangle(image,(x,y),(x+w,y+h),(0,0,255),1)

cv2.imshow("Image",image)
cv2.waitKey(0)

         
