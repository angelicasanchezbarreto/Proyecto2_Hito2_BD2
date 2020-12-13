import os
import re
import cv2
import pickle
import face_recognition

class Encoding:
    files = []
    knownEncodings = []

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
            name = filepath.split(os.path.sep)[-2]
            print(filepath)
            
            image = face_recognition.load_image_file(filepath)
            vector = face_recognition.face_encodings(image)[0]
            pic_name = filepath.split(os.path.sep)[-1]
            self.knownEncodings.append((pic_name,vector))

    def write_encodings(self):
        print("[INFO] serializing encodings...")
        f = open("encodings6400.pickle", "wb")
        f.write(pickle.dumps(self.knownEncodings))
        f.close()
