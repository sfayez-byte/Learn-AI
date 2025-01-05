# التعامل مع نظام الالوان في الصور
import cv2
img =cv2.imread('imgg/eye-9266169_1280.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow('eyes', gray)
cv2.waitKey(0)
