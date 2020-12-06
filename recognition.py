import face_recognition
import pickle
import cv2
import re
import os
import nltk 
from knnSearch import knnRtree, knnSequential
from rangeSearch import rangeSearch

class Recognition:
    def __init__(self,input_path):
        self.load_encodings(input_path)
    
    def load_encodings(self,input_path):
        # load the known faces and embeddings
        print("[INFO] loading encodings...")
        data = pickle.loads(open("encodings.pickle", "rb").read())

        print("Leyendo imagenes de",input_path)
        for root, dirnames, filenames in os.walk(input_path):
            for filename in filenames:
                if re.search("\.(jpg|jpeg|png|bmp|tiff)$", filename):
                    image_path = os.path.join(root, filename)

                    # load the input image and convert it from BGR to RGB
                    image = cv2.imread(image_path)
                    rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
                    
                    # detect the (x, y)-coordinates of the bounding boxes corresponding
                    # to each face in the input image, then compute the facial embeddings
                    # for each face
                    print("[INFO] recognizing faces...")
                    boxes = face_recognition.face_locations(rgb,model="cnn")
                    encodings = face_recognition.face_encodings(rgb, boxes)
                    #result = knnRtree(encodings,8,data)
                    for encoding in encodings:
                        #result = knnSequential(encoding,8,data)
                        result = rangeSearch(encoding,0.6,data)
                        self.read_image(result)
                    
                    # initialize the list of names for each face detected
                    """ names = []
                    self.loop_encodings(encodings,names,data)
                    for name in names:
                        print(name) """

    def read_image(self,result):
        for i in result:
            name = i[1].replace('_0',' ')
            tokens = nltk.word_tokenize(name)
            name = tokens[0]
            dirname = os.path.join(os.getcwd(), 'prueba')
            imgpath = dirname + os.sep + name
            for image in os.listdir(imgpath):
                if image == i[1]:
                    img = cv2.imread(os.path.join(imgpath,image))
                    print(image)
            

    def loop_encodings(self,encodings,names,data):
        # loop over the facial embeddings
        for encoding in encodings:
            # attempt to match each face in the input image to our known
            # encodings
            matches = face_recognition.compare_faces(data["encodings"],
                encoding)
            name = "Unknown"

            # check to see if we have found a match
            if True in matches:
                # find the indexes of all matched faces then initialize a
                # dictionary to count the total number of times each face
                # was matched
                matchedIdxs = [i for (i, b) in enumerate(matches) if b]
                counts = {}

                # loop over the matched indexes and maintain a count for
                # each recognized face face
                for i in matchedIdxs:
                    name = data["names"][i]
                    counts[name] = counts.get(name, 0) + 1

                # determine the recognized face with the largest number of
                # votes (note: in the event of an unlikely tie Python will
                # select first entry in the dictionary)
                name = max(counts, key=counts.get)
            
            # update the list of names
            names.append(name)