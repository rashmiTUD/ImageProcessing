'''
This piece of code detects the largest contour of the hand and
finds the convexhull of the detected contour. Convexhull is one of the property/feature
of a Contour

'''
import cv2 as cv
import numpy as np

# read an image
hand=cv.imread("01.jpg")

#resize an image
hand=cv.resize(hand,(400,300))
#convert to grayscale
gray = cv.cvtColor(hand, cv.COLOR_BGR2GRAY)
gray = cv.GaussianBlur(gray, (5, 5), 0)
# threshold an image
ret,threshold= cv.threshold(gray,70,255,cv.THRESH_BINARY)
# use Canny Edge detection
canny_output = cv.Canny(gray, 400,300)

#find contours
im,contours,hierarchy=cv.findContours(threshold,cv.RETR_EXTERNAL,cv.CHAIN_APPROX_SIMPLE)
    

# Find the convex hull object for each contour
hull_list = []
for i in range(len(contours)):
    hull = cv.convexHull(contours[i])
    hull_list.append(hull)
# Draw contours + hull results
drawing = np.zeros((canny_output.shape[0], canny_output.shape[1], 3), dtype=np.uint8)
print(np.shape(contours))
for i in range(len(contours)):
    
    cv.drawContours(drawing,contours, i, (0,255,0),3)
    cv.drawContours(drawing,hull_list, i, (0,0,255),3)
# Show in a window
cv.imshow('Contours', drawing)
cv.imwrite('01contours.jpg',drawing)

cv.waitKey()
