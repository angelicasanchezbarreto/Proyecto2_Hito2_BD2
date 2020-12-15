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
    def __init__(self,option):
        if option == '100':
            self.data = json.loads(open("files/encodings100.json", "r").read())
        elif option == '200':
            self.data = json.loads(open("files/encodings200.json", "r").read())
        elif option == '400':
            self.data = json.loads(open("files/encodings400.json", "r").read())
        elif option == '800':
            self.data = json.loads(open("files/encodings800.json", "r").read())
        elif option == '1600':
            self.data = json.loads(open("files/encodings1600.json", "r").read())
        elif option == '3200':
            self.data = json.loads(open("files/encodings3200.json", "r").read())
        elif option == '6400':
            self.data = json.loads(open("files/encodings6400.json", "r").read())
        elif option == '12800':
            self.data = json.loads(open("files/encodings12800.json", "r").read())


    def load_encodings(self,input_path,option):
        print("Leyendo imagenes de",input_path)
        self.image_paths = dict()
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
                        self.read_image(result,option)
                        
                    #start_time = time()
                        
                    #end_time = time()
                    #final_time = round(1000*(end_time - start_time),4)
                    #print(final_time)
        return self.image_paths

    def read_image(self,result,option):
        images = []
        key_name = result[0][1].replace('_0',' ')
        key_tokens = nltk.word_tokenize(key_name)
        key_name = key_tokens[0]
        
        path = self.choose_path(option)
        for i in result:
            dirname = os.path.join(os.getcwd(), path)
            imgpath = dirname + os.sep + i[1]
            images.append(imgpath)
            # for image in os.listdir(imgpath):
            #     img_in_result = i[1]
            #     if image == img_in_result:
            #         img = cv2.imread(os.path.join(imgpath,image))
            #         print(image)
            
        self.image_paths[key_name] = images
            
    def choose_algorithm(self,encoding,option):
        result = []
        if option == '1':
            result = knnSequential(encoding,8,self.data)
        elif option == '2':
            result = knnRtree(encoding,8,self.data)
        elif option == '3':
            result = rangeSearch(encoding,0.6,self.data)
        return result

    def choose_path(self,option):
        path = str()
        if option == '100':
            path = 'images/prueba100'
        elif option == '200':
            path = 'images/prueba200'
        elif option == '400':
            path = 'images/prueba400'
        elif option == '800':
            path = 'images/prueba800'
        elif option == '1600':
            path = 'images/prueba1600'
        elif option == '3200':
            path = 'images/prueba3200'
        elif option == '6400':
            path = 'images/prueba6400'
        elif option == '12800':
            path = 'images/prueba12800'
        return path