# -*- coding: utf-8 -*-
"""
Created on Thu Sep 06 14:50:00 2018

@author: RB. This script captures SIFT features and keypoints in various hand pose
"""

import cv2
import numpy as np
img = cv2.imread('skin3.jpg')
gray= cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
sift = cv2.xfeatures2d.SIFT_create()
kp = sift.detect(gray,None)
#(x1,y1)=kp.pt
i=0
for x in kp: # looping through keypoints
    print kp[i].pt #printing x,y location of the keypoint 
    i=i+1


print kp[0].size
#print points2f
#print y1
img=cv2.drawKeypoints(gray,kp,img)
cv2.imshow("Image",img)
cv2.imwrite('sift_handskin3.jpg',img)
cv2.waitKey(0)

