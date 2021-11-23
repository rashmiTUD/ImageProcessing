# -*- coding: utf-8 -*-
"""
Created on Wed Sep 26 16:54:46 2018

@author: Rashmi 
"""
"""im extracting skin pixels from the image.. converting rgb image to ycrcb color space
applying a mask , and Gaussian blur to remove extra noise.
"""
import numpy as np
import cv2
im=cv2.imread('Palm-29.jpg')   ## it works on all the images thumb2Latest; rect; 
im=cv2.resize(im,(400,300))


min_YCrCb = np.array([0,133,77],dtype="uint8")
max_YCrCb = np.array([255,179,127],dtype="uint8")

b=im[:,:,0]
g=im[:,:,1]
r=im[:,:,2]

avgR = np.mean(np.mean(b));
avgG = np.mean(np.mean(g));
avgB = np.mean(np.mean(r));
avgRGB = [avgR,avgG,avgB];
    
    #Calculate the Avg value of R,G,B as gray value
grayValue = (avgR + avgG + avgB)/3;
    
    #Calculate the scaling factors
scale=np.divide(grayValue,avgRGB);
    
    
    #Scale the values
newI=im
newI[:,:,0] = scale[0] * b;
newI[:,:,1] = scale[1] * g;
newI[:,:,2] = scale[2] * r;
    #cv2.imshow("images 1",newI)
converted = cv2.cvtColor(newI, cv2.COLOR_BGR2YCR_CB)
mask=cv2.inRange(converted,min_YCrCb,max_YCrCb)
    #gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    #gray = cv2.GaussianBlur(gray, (5, 5), 0)
#cv2.imshow('im2',gray)
    #ret, threshold= cv2.threshold(gray,50,255,cv2.THRESH_BINARY)
#cv2.imshow('im3',threshold)

skinMask = cv2.GaussianBlur(mask, (3, 3), 0)
skinMask = cv2.bitwise_and(im, im, mask = mask)
 
# show the skin in the image along with the mask
cv2.imshow("images", np.hstack([im, skinMask]))
cv2.imwrite('skin4.jpg',skinMask)
 
# if the 'q' key is pressed, stop the loop
k = cv2.waitKey(0)
    
cv2.destroyAllWindows()
