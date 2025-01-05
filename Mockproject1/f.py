import cv2
# قيم المعنى النموذجي (ارقام ثابته)
Model_Name_Values = (78.4463377603
                     ,87.7689143744
                     ,114.895847746)
#انشاء لسته للاعمار
Age_List = ['(0,2)','(4,6)','(8,12)','(15,20)','(25,32)','(38,43)','(48,53)','(38,43)','(60,100)']
#تحديد الجنس
Gender_List = ['Male','Female']
#استدعاء ملفات التعرف على العمر و الجنس
def filesGet():
    Age_Net = cv2.dnn.readNetFromCaffe(
        'data/deploy_age.prototxt','data/age_net.caffemodel')
    Gender_Net = cv2.dnn.readNetFromCaffe(
        'data/deploy_gender.prototxt','data/gender_net.caffemodel')
    return (Age_Net,Gender_Net)

def read_from_cam(Age_Net,Gender_Net):
    #تحديد نوع الخط و استدعاء الصوره
    font = cv2.FONT_HERSHEY_SIMPLEX
    image = cv2.imread('images\girl1.jpg')
    #ملف تحديد الوجه
    face_cascade=cv2.CascadeClassifier('data\haarcascade_frontalface_alt.xml')
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    #تحديد عدد الاوجه
    faces = face_cascade.detectMultiScale(gray, 1.1, 5)
    
    if (len(faces) > 0):
        print("Found{} faces".format(str(len(faces))))

    for (x, y, w, h )in faces:
     #رسم مستطيل حول الوجه
     cv2.rectangle(image, (x,y),(x+w,y+h),(255,255,0),2)
     #الوصول الى الصوره و نسخها وارسالها الى الخوارزميه
     face_img=image[y:y+h,x:x+w].copy()
     # توقع الجنس و العمر
     blob = cv2.dnn.blobFromImage(face_img, 1, (227, 227), Model_Name_Values, swapRB=False)
     Gender_Net.setInput(blob)
     gender_p=Gender_Net.forward()
     gender = Gender_List[gender_p[0].argmax()]
     print("gender : " +gender)
     Age_Net.setInput(blob)
     age_p=Age_Net.forward()
     age = Age_List[age_p[0].argmax()]
     print("Age : " +age)
     G_A = "%s %s" % (gender , age)
     cv2.putText(image, G_A, (x, y), font, 1, (255, 255, 0), 2, cv2.LINE_AA)
     cv2.imshow('image', image) 
     cv2.waitKey(0)
if __name__ == "__main__":
    Age_Net ,Gender_Net = filesGet()
    read_from_cam(Age_Net,Gender_Net)