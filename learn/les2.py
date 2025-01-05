#عرض الصوره مع بقاء النافذه شغاله
import cv2
img = cv2.imread('imgg/eye-1173863_1280.jpg')
cv2.imshow('eye', img)
cv2.waitKey(0) # لو كان فيديو نحط القيمه 1
