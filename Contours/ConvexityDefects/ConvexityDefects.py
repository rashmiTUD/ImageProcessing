# This piece of code find contours,
#maximum contour area and then finds convex hull and convexity defects for an
#open hand..
# opencv documentation
#Author: rashmi 


import cv2
import numpy as np

img = cv2.imread('handFront-ex3.jpg')
img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(img_gray, 127, 255,0)
contours,hierarchy = cv2.findContours(thresh,2,1)[-2:]
c = max(contours, key=cv2.contourArea)
#print len(contours)
#cnt = contours[0]

cv2.drawContours(img_gray, [c], -1, (0, 255, 255), 2)

hull = cv2.convexHull(c,returnPoints = False)
defects = cv2.convexityDefects(c,hull)


for i in range(defects.shape[0]):
    s,e,f,d = defects[i,0]
    start = tuple(c[s][0])
    end = tuple(c[e][0])
    far = tuple(c[f][0])
    cv2.line(img,start,end,[0,255,0],2)
    cv2.circle(img,far,5,[0,0,255],-1)

cv2.imshow('img',img)
cv2.imwrite('HullDefects5.png',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
