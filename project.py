import cv2
import numpy as np


cones_original= cv2.imread('/Users/jenil/Downloads/OPENCV/Computer-Vision-with-Python/DATA/red.png')
cones=cv2.cvtColor(cones_original,cv2.COLOR_BGR2RGB)
lower_bound= np.array([150,0,0],dtype = "uint8")
upper_bound= np.array([245,40,40],dtype = "uint8")

mask= cv2.inRange(cones,lower_bound,upper_bound)
mask.astype
detected_output = cv2.bitwise_and(cones, cones, mask =  mask) 



detected_output= cv2.cvtColor(detected_output,cv2.COLOR_RGB2GRAY)
roi= detected_output[0:2420,0:981]


blur = cv2.GaussianBlur(roi, (5, 5),cv2.BORDER_DEFAULT)

ret, thresh = cv2.threshold(blur, 0, 255,
                           cv2.THRESH_BINARY)

image, contours, hierarchy=cv2.findContours(thresh,cv2.RETR_CCOMP,cv2.CHAIN_APPROX_SIMPLE)


points=[]
for i in contours:
    if cv2.contourArea(i)>200:
        M = cv2.moments(i)
        if M['m00'] != 0:
            cx = int(M['m10']/M['m00'])
            cy = int(M['m01']/M['m00'])
            points.append((cx,cy))
points= np.array(points)           
points= points.astype(np.float32)

vx, vy, x, y = cv2.fitLine(points, cv2.DIST_L2, 0, 0.01, 0.01)

cols = cones.shape[1]
lefty = int((-x*vy/vx) + y)
righty = int(((cols-x)*vy/vx)+y)

cv2.line(cones, (cols-1, righty), (0, lefty), (255, 0, 0), 3)

roi=detected_output[0:2420, 981:1817]
blur = cv2.GaussianBlur(roi, (5, 5),cv2.BORDER_DEFAULT)

ret, thresh = cv2.threshold(blur, 0, 255,
                           cv2.THRESH_BINARY)


image, contours1, hierarchy=cv2.findContours(thresh,cv2.RETR_CCOMP,cv2.CHAIN_APPROX_SIMPLE)

points2=[]
for i in contours1:
    if cv2.contourArea(i)>200:
        M = cv2.moments(i)
        if M['m00'] != 0:
            cx = int(M['m10']/M['m00'])+980
            cy = int(M['m01']/M['m00'])
            
            points2.append((cx,cy))
points2= np.array(points2)           
points2= points2.astype(np.float32)

vx, vy, x, y = cv2.fitLine(points2, cv2.DIST_L2, 0, 0.01, 0.01)

cols = cones.shape[1]
lefty = int((-x*vy/vx) + y)
righty = int(((cols-x)*vy/vx)+y)

cv2.line(cones, (cols-1, righty), (0, lefty), (255, 0, 0), 3)

cones=cv2.cvtColor(cones,cv2.COLOR_RGB2BGR)

cv2.imwrite('/Users/jenil/Downloads/OPENCV/Computer-Vision-with-Python/DATA/answer.png',cones)


while True:
    cv2.imshow('red detected', cones)
    
    #if we have waite  at leat 1 ms and we have pressed the ESC 
    if cv2.waitKey(1)& 0xFF==27: 
        break
cv2.destroyAllWindows()