# USAGE
# python extreme_points.py

# import the necessary packages
import imutils
import cv2
import matplotlib.pyplot as plt
import math

# load the image, convert it to grayscale, and blur it slightly
image = cv2.imread("p2-ex.jpg") #handFront-ex3.jpg  
image=cv2.resize(image,(400,400))
h,w,c=image.shape
#print h,w,c
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
#cv2.imshow('Gray',gray)
gray = cv2.GaussianBlur(gray, (5, 5), 0)
cv2.imshow('Gray',gray)

# find contours in thresholded image, then grab the largest
# one
cnts = cv2.findContours(gray.copy(), cv2.RETR_EXTERNAL,
	cv2.CHAIN_APPROX_SIMPLE)
cnts = cnts[0] if imutils.is_cv2() else cnts[1]
c = max(cnts, key=cv2.contourArea)
M=cv2.moments(c)
cX = int(M["m10"] / M["m00"])
cY = int(M["m01"] / M["m00"])
 
# put text and highlight the center
cv2.circle(image, (cX, cY), 5, (255, 255, 255), -1)
cv2.putText(image, "centroid", (cX - 25, cY - 25),cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)


# determine the most extreme points along the contour
extLeft = tuple(c[c[:, :, 0].argmin()][0])
extRight = tuple(c[c[:, :, 0].argmax()][0])
extTop = tuple(c[c[:, :, 1].argmin()][0])
extBot = tuple(c[c[:, :, 1].argmax()][0])

print(extTop[0])
print(extTop[1])
print(cX)
print(cY)

distance=math.sqrt( ((cX-extTop[0])**2)+((cY-extTop[1])**2) )
print distance
if distance<150:
    print "Closed hand"
else:
    print "Open hand"
# draw the outline of the object, then draw each of the
# extreme points, where the left-most is red, right-most
# is green, top-most is blue, and bottom-most is teal
cv2.drawContours(image, [c], -1, (0, 255, 255), 2)
cv2.circle(image, extLeft, 6, (0, 0, 255), -1)
cv2.circle(image, extRight, 6, (0, 255, 0), -1)
cv2.circle(image, extTop, 6, (255, 0, 0), -1)
cv2.putText(image, "Far Top", (extTop[0], extTop[1] ),cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)
cv2.circle(image, extBot, 6, (255, 255, 0), -1)

# show the output image
cv2.imshow("Image", image)
#cv2.imwrite("myhandEx6.jpg", image)
cv2.waitKey(0)
