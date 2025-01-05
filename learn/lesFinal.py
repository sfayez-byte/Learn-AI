import cv2
cam = cv2.VideoCapture(0)
while True:
    ret , video  =cam.read()
    new_cam=cv2.resize(video,(300,200))
    cv2.imshow('samar',video)
    if cv2.waitKey(1) & 0xff == ord('q'):
        break
