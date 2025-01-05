# عرض الفيديوهات في البرنامج
import cv2
cam = cv2.VideoCapture('Videos/45144-441301057_medium.mp4')
while True:
    ret , frame =cam.read() #هنا بيقسم الفيديو و بيعرضها
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY) # بيحول الفيديو الى رمادي
    size = cv2.resize(frame,(400,300))
    cv2.imshow('Video',gray) # بيجمع الفيديوهات و يخليها تشتغل سوا
    if cv2.waitKey(1) & 0xff == ord('q'):
        break
