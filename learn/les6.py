#نظام حفظ و فتح الصوره و تخصيص زر لحفظ البرنامج و زر لغلاق الصوره 

import cv2
img = cv2.imread('imgg/eye-2681783_1280.jpg',0)
cv2.imshow('eyes', img)
k=cv2.waitKey(0)
if k==27: 
    cv2.destroyAllWindows()
elif k == ord('s'):
    cv2.imwrite('C://grayeyes.png',img) #ما ضبط بس الزر حق الاغلاق ضبط
    cv2.destroyAllWindows()



