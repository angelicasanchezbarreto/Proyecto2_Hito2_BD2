import face_recognition
import pickle
import cv2
import re
import os
import nltk 
import json
from time import time
from knnSearch import knnRtree, knnSequential
from rangeSearch import rangeSearch

class Recognition:
    def __init__(self,input_path,option):
        print("[INFO] loading encodings...")
        self.data = json.loads(open("files/encodings100.json", "r").read())
        self.load_encodings(input_path,option)
    
    def load_encodings(self,input_path,option):
        print("Leyendo imagenes de",input_path)
        for root, dirnames, filenames in os.walk(input_path):
            for filename in filenames:
                if re.search("\.(jpg|jpeg|png|bmp|tiff)$", filename):
                    image_path = os.path.join(root, filename)

                    print("[INFO] recognizing faces...")
                    
                    image = face_recognition.load_image_file(image_path)
                    locations = face_recognition.face_locations(image)

                    coordinate = dict()
                    for i in locations:
                        top, right, bottom, left = i
                        coordinate = image[top:bottom,left:right]
                        vector = face_recognition.face_encodings(coordinate)[0]
                        result = self.choose_algorithm(vector,option)
                        self.read_image(result)
                        
                    #start_time = time()
                        
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
