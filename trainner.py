import  os
import cv2
from PIL import Image
import numpy as np
def update():
    recognizer = cv2.face.LBPHFaceRecognizer_create()
    path = 'dataSet'

    def getImagesWithID(path):
        imagePaths = [os.path.join(path,f) for f in os.listdir(path)];
        faces = []
        IDs = []
        for imagePath in imagePaths:
            faceImg = Image.open(imagePath).convert('L')
            faceUp = np.array(faceImg,'uint8')
            ID = int(os.path.split(imagePath)[-1].split('.')[1])
            print(ID)
            faces.append(faceUp)
            IDs.append(ID)
            cv2.imshow("trainer",faceUp)
            cv2.waitKey(100)
        return faces,np.array(IDs)
    faces,IDs = getImagesWithID(path)
    recognizer.train(faces,np.array(IDs))
    recognizer.save('recognizer/trainningData.yml')
    cv2.destroyAllWindows()
    cv2.destroyAllWindows()