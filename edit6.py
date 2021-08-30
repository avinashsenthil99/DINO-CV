import cv2
import numpy as np
import pyautogui
cam=cv2.VideoCapture(0)
while True:
    ret,frame=cam.read()
    centers=[]
    hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    lower_range=np.array([100,100,100])
    upper_range=np.array([120,255,255])
    mask=cv2.inRange(hsv,lower_range,upper_range)

     
    ret,thresh = cv2.threshold(mask,140,255,0)
    image,contours,hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

    for contour in contours:
      area = cv2.contourArea(contour)
      if area>321:
            x,y,w,h = cv2.boundingRect(contour) 
            frame = cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
            cv2.putText(frame,"Object",(x,y),cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255,0,0))
            M = cv2.moments(contour) 
            cx = int(M['m10'] /M['m00'])
            cy = int(M['m01'] /M['m00'])
            centers.append(cx)

    if len(centers)==1:                                             
        pyautogui.press('space')  
    cv2.imshow("video",frame)                            
    if cv2.waitKey(1) & 0xFF==27:
        break
cam.release()
cv2.destroyAllWindows()
h

                                
