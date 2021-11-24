# -*- coding: utf-8 -*-
"""
Created on Thu Aug 30 17:02:12 2018

@author: Administrator
"""

import numpy as np
import cv2
import matplotlib.pyplot as plt
img1 = cv2.imread('skin1.jpg')   #hand1new.jpg   #processedThumb1.png      # queryImage
img2 = cv2.imread('skin1Side.jpg')   #hand2new.jpg   #processedThumb2.png                         # trainImage
#cv2.imshow('im',img1)

#cv2.waitKey(0)
#cv2.imshow('im2',img2)
#cv2.waitKey(0)


# Initiate SURF detector

surf = cv2.xfeatures2d.SURF_create()
# find the keypoints and descriptors with ORB
kp1, des1 = surf.detectAndCompute(img1,None)
kp2, des2 = surf.detectAndCompute(img2,None)
print len(kp1)
print len(kp2)
#print des1
#cv2.imshow('im',img1)
#cv2.imshow('im2',img2)
# create BFMatcher object
bf = cv2.BFMatcher()
# Match descriptors.
matches = bf.match(des1,des2)
# Sort them in the order of their distance.
matches = sorted(matches, key = lambda x:x.distance)
print len(matches)
# ratio test
good = []
for m in matches:
    if m.distance < 0.7:
        good.append([m])

print len(good)

# Draw first 10 matches.
img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10],None,flags=2)

plt.imshow(img3),plt.show()
#cv2.imwrite('result1SURF6.jpg',img3)

cv2.waitKey(0)
