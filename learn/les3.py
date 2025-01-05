#عرض ابعاد الصوره و البكسلات 

import cv2
img = cv2.imread('imgg/eye-9266169_1280.jpg')
pix = img.size
dim = img.shape
cv2.imshow('eyes', img)
print("number of pixels: ", pix)
print("dimension: ", dim)
cv2.waitKey(0)