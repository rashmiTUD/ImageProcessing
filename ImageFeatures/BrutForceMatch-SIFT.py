# -*- coding: utf-8 -*-
"""
Created on Tue Sep 11 18:18:02 2018

@author: Administrator
"""

# -*- coding: utf-8 -*-
"""
Created on Thu Aug 30 17:02:12 2018

@author: Administrator
"""
#this is SIFT descriptor with ratio test 
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

#sift = cv2.SIFT()
sift = cv2.xfeatures2d.SIFT_create()
# find the keypoints and descriptors with ORB
kp1, des1 = sift.detectAndCompute(img1,None)
kp2, des2 = sift.detectAndCompute(img2,None)

print len(kp1)
print len(kp2)
#cv2.imshow('im',img1)
#cv2.imshow('im2',img2)
# create BFMatcher object
bf = cv2.BFMatcher()
# Match descriptors.

matches = bf.knnMatch(des1,des2, k=2)

print len(matches)

# Apply ratio test
good = []
for m,n in matches:
    if m.distance < 0.75*n.distance:
        good.append([m])
if len(good)>20:
    print "Similar"
else:
    print "Not similar"

print len(good)
# cv2.drawMatchesKnn expects list of lists as matches.
img3 = cv2.drawMatchesKnn(img1,kp1,img2,kp2,good[:10],None,flags=2)

plt.imshow(img3),plt.show()

#cv2.imwrite('result6SIFT.jpg',img3)
cv2.waitKey(0)
