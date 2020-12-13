import face_recognition
import pickle
import cv2
import re
import os
import nltk 
from time import time
from knnSearch import knnRtree, knnSequential
from rangeSearch import rangeSearch

class Recognition:
    def __init__(self,input_path,option):
        print("[INFO] loading encodings...")
        self.data = pickle.loads(open("encodings3200.pickle", "rb").read())
        self.load_encodings(input_path,option)
    
    def load_encodings(self,input_path,option):
        print("Leyendo imagenes de",input_path)
        for root, dirnames, filenames in os.walk(input_path):
            for filename in filenames:
                if re.search("\.(jpg|jpeg|png|bmp|tiff)$", filename):
                    image_path = os.path.join(root, filename)

                    image = cv2.imread(image_path)
                    rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
                    
                    print("[INFO] recognizing faces...")
                    boxes = face_recognition.face_locations(rgb,model="cnn")
                    encodings = face_recognition.face_encodings(rgb, boxes)
                    #start_time = time()
                    for encoding in encodings:
                        result = self.choose_algorithm(encoding,option)
                        self.read_image(result)
                    #end_time = time()
                    #final_time = round(1000*(end_time - start_time),4)
                    #print(final_time)

    def read_image(self,result):
        for i in result:
            name = i[1].replace('_0',' ')
            tokens = nltk.word_tokenize(name)
            name = tokens[0]
            dirname = os.path.join(os.getcwd(), 'images/prueba100')
            imgpath = dirname + os.sep + name
            for image in os.listdir(imgpath):
                img_in_result = i[1]
                if image == img_in_result:
                    img = cv2.imread(os.path.join(imgpath,image))
                    print(image)
            
    def choose_algorithm(self,encoding,option):
        result = []
        if option == '1':
            result = knnSequential(encoding,8,self.data)
        elif option == '2':
            result = knnRtree(encoding,8,self.data)
        elif option == '3':
            result = rangeSearch(encoding,0.6,self.data)
        return result
