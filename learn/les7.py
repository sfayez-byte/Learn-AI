import cv2
import numpy as np 
img = cv2.imread('imgg/eye-2681783_1280.jpg')
# line - rectangle - text كلها علشان اقدر احدد الصور و اخليه يتعرف عليها 
# cv2.line(img,(10,10),(200,10),(0,0,255),2)
cv2.rectangle(img, (300,20),(600,300),(0,0,255),4)
cv2.putText(img, "samars eye",(300,50),cv2.FONT_HERSHEY_SIMPLEX,1,(255,0,0),2)
cv2.imshow('samars eye',img)
cv2.waitKey(0)
