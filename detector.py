import cv2
import  sqlite3
def monitor():
    faceDetect = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml");
    cam = cv2.VideoCapture(0);
    rec = cv2.face.LBPHFaceRecognizer_create();
    rec.read('recognizer/trainningData.yml')
    font = cv2.FONT_HERSHEY_COMPLEX_SMALL
    def getProfile(id):
        conn = sqlite3.connect("faceBase.db")
        cmd = "SELECT * FROM People WHERE ID="+str(id)
        cursor = conn.execute(cmd)
        profile = None
        for row in cursor:
            profile = row
        conn.close()
        return profile
    while(True):
        ret,img = cam.read();
        gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY);
        faces = faceDetect.detectMultiScale(gray,1.3,5);
        for(x,y,w,h) in faces:
            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
            id,conf = rec.predict(gray[y:y+h,x:x+w])
            profile = getProfile(id)
            if(profile!=None):
                cv2.putText(img, profile[1], (x, y + h), font, 1, (0, 255, 0), 2)
        cv2.imshow("Face",img);
        if(cv2.waitKey(1)== ord('q')):
            break;
    cam.release();
    cv2.destroyAllWindows();




