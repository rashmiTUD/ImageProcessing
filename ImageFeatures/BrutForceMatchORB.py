# -*- coding: utf-8 -*-
"""
Created on Thu Aug 30 17:02:12 2018

@author: Administrator
compute and match keypoints for two similar images by finding the ratio test. 
""" 

import numpy as np
import cv2
import matplotlib.pyplot as plt
img1 = cv2.imread('skin1.jpg')          # queryImage
img2 = cv2.imread('skin1Side.jpg') # trainImage
#cv2.imshow('im',img1)

#cv2.waitKey(0)
#cv2.imshow('im2',img2)
#cv2.waitKey(0)


# Initiate ORB detector

orb = cv2.ORB_create()
# find the keypoints and descriptors with ORB
kp1, des1 = orb.detectAndCompute(img1,None)
kp2, des2 = orb.detectAndCompute(img2,None)
print len(kp1)
print len(kp2)

#cv2.imshow('im',img1)
#cv2.imshow('im2',img2)
# create BFMatcher object
bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
# Match descriptors.
matches = bf.match(des1,des2)
# Sort them in the order of their distance.
matches = sorted(matches, key = lambda x:x.distance)

good = []
print len(matches)
for m in matches:
    if m.distance < 0.7:
        good.append([m])

print len(good)
if len(good) > 10:
   print "similar image"
else:
    print "not similar"
# Draw first 10 matches.
img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10],None,flags=2)
plt.imshow(img3),plt.show()
#cv2.imwrite('result3ORB.jpg',img3)
cv2.waitKey(0)
