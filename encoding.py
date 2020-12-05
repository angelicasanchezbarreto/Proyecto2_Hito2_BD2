import os
import re
import cv2
import pickle
import face_recognition

class Encoding:
    files = []
    knownEncodings = []
    knownNames = []

    def __init__(self,imgpath):
        self.get_images_in_folders(imgpath)
        self.get_encodings()
        self.write_encodings()
        
    def get_images_in_folders(self,imgpath):
        cant=0
        print("Leyendo imagenes de",imgpath)
        for root, dirnames, filenames in os.walk(imgpath):
            for filename in filenames:
                if re.search("\.(jpg|jpeg|png|bmp|tiff)$", filename):
                    cant=cant+1
                    filepath = os.path.join(root, filename)
                    self.files.append(filepath)
                    b = "Leyendo..." + str(cant)
                    print (b, end="\r")
        print('Suma Total de archivos en subdirs:',cant)

    def get_encodings(self):
        for i,filepath in enumerate(self.files):
            print("[INFO] processing image {}/{}".format(i + 1,
            len(self.files)))
            # load the input image and convert it from RGB (OpenCV ordering)
            # to dlib ordering (RGB)
            name = filepath.split(os.path.sep)[-2]
            print(name)
            image = cv2.imread(filepath)
            rgb = cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
            # detect the (x, y)-coordinates of the bounding boxes
            # corresponding to each face in the input image  
            boxes = face_recognition.face_locations(rgb,model="cnn")
            # compute the facial embedding for the face
            encodings = face_recognition.face_encodings(rgb,boxes)
            # loop over the encodings
            for encoding in encodings:
            # add each encoding + name to our set of known names and encodings
                self.knownEncodings.append(encoding)
                self.knownNames.append(name)

    def write_encodings(self):
        print("[INFO] serializing encodings...")
        data = {"encodings": self.knownEncodings, "names": self.knownNames}
        f = open("encodings.pickle", "wb")
        f.write(pickle.dumps(data))
        f.close()
