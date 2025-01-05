import cv2
img = cv2.imread('images\elephant.jpg')
class_names = [] # list or an array
class_file= 'files/thing.names'
with open(class_file, 'rt') as f:
    class_names =f.read().rstrip('\n').split('\n')
    #print(class_names)
    p = 'files/frozen_inference_graph.pb'
    v = 'files/ssd_mobilenet_v3_large_coco_2020_01_14.pbtxt'

    net = cv2.dnn_DetectionModel(p, v) # detect and discover
    net.setInputSize(320, 230)  # hight and width
    net.setInputScale(1.0/127.5) # scale
    net.setInputMean((127.5,127.5,127.5)) # قيمه ثابته ما تتغير
    net.setInputSwapRB(True) # color

    class_ids, confs, bbox = net.detect(img, confThreshold=0.5)
   # print(class_ids, bbox)
    for class_id, confidence, box in zip(class_ids.flatten(), confs.flatten(), bbox):
        cv2.rectangle(img, box, color=(0,255,0), thickness=3)
        cv2.putText(img, class_names[class_id-1], (box[0]+10, box[1]+20), cv2.FONT_HERSHEY_COMPLEX, 1, (0,255,0), thickness=2)
    cv2.imshow('program', img)
    cv2.waitKey(0)