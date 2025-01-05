#تغيير حجم الصوره و النافذه 
import cv2
img = cv2.imread('imgg/eye-1173863_1280.jpg')
new_img=cv2.resize(img,(200,200))
cv2.imshow('size image', new_img)
cv2.waitKey(0)