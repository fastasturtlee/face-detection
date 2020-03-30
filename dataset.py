import cv2
import sqlite3
from tkinter import *
def capture():

    faceDetect = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml");
    cam = cv2.VideoCapture(0);
    #id = input("enter the id : ")
    #name = input( "Enter your name : ")
    root = Tk()
    root.title("User Input Form")
    root.geometry("240x120+100+300")
    label1 = Label(root, text="id")
    label2 = Label(root, text="name")
    label1.grid(row="0", column="0", padx="10", pady="10")
    label2.grid(row="1", column="0", padx="10", pady="10")
    Entry_id = Entry(root, textvariable="id")
    Entry_name = Entry(root, textvariable="name")
    Entry_id.grid(row="0", column="1", padx="10", pady="10")
    Entry_name.grid(row="1", column="1", padx="10", pady="10")
    button1 = Button(root, text="click here", command=root.quit)
    button1.grid(row="2", column="0", padx="10")
    root.mainloop()
    id = str(Entry_id.get())
    name = str(Entry_name.get())
    sampleNum = 0;
    def InsertorUpdate(Id,Name):
        conn = sqlite3.connect('Facebase.db')
        cmd = "SELECT * FROM People WHERE ID=" + str(Id)
        cursor = conn.execute(cmd)
        isRecordExist = 0
        for row in cursor:
            isRecordExist=1
        if(isRecordExist==1):
            cmd = "UPDATE People SET Name=" +str(Name)+"WHERE ID="+str(Id)
        else:
            cmd = "INSERT INTO People(ID,Name) Values(" + str(Id)+","+str(Name)+")"
        conn.execute(cmd)
        conn.commit()
        conn.close()

    InsertorUpdate(id,name)

    while(True):
        ret,img = cam.read();
        gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY);
        faces = faceDetect.detectMultiScale(gray,1.3,5);
        for(x,y,w,h) in faces:
            sampleNum = sampleNum+1;
            cv2.imwrite("dataSet/User"+"."+str(id)+"."+str(sampleNum)+".jpg",gray[y:y+h,x:x+w]);
            cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2);
        cv2.imshow("Face",img);
        cv2.waitKey(100);
        if(sampleNum>20):
            break;
    cam.release();
    cv2.destroyAllWindows();




