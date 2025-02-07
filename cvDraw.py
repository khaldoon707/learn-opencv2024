import numpy as np
import cv2 as cv
 
# Create a black image
img = np.zeros((512,512,3), np.uint8)
 
# Draw a diagonal blue line with thickness of 5 px
cv.line(img,(0,0),(511,511),(255,0,0),5)



cv.rectangle(img,(384,0),(510,128),(0,255,0),3)
 ##draw a circle, you need its center coordinates and radius. We will draw a circle inside the rectangle drawn above.

cv.circle(img,(447,63), 63, (0,0,255), -1)

##
pts = np.array([[10,5],[20,30],[70,20],[50,10]], np.int32)
pts = pts.reshape((-1,1,2))
cv.polylines(img,[pts],True,(0,255,255))

cv.imshow("Display window", img)

k = cv.waitKey(0)
 
if k == ord("s"):
    cv.imwrite("./image/starry_night.png", img)
