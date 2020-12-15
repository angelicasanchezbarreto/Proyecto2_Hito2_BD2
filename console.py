from encoding import Encoding
from recognition import Recognition
import os
import re

class Console:
    def base(self,input_path, algorithm, n):
        recognition = Recognition(n)
        result = recognition.load_encodings(input_path, algorithm)
        return result


"""   def options(self):
        print("Which method do you want to use:")
        print("1. KNN Sequential Search")
        print("2. KNN Rtree Search")
        print("3. Range Search")
        number = input()
        print("How many images do you want:")
        size = input()
        return number,size"""


#solo se ejecuta una vez
""" dirname = os.path.join(os.getcwd(), 'images/prueba6400')
imgpath = dirname + os.sep 
encode = Encoding(imgpath) """

#dirname2 = os.path.join(os.getcwd(), 'pruebaInputs')
#imgpath2 = dirname2 + os.sep 
#console = Console(imgpath2)

#console = Console()
#print(console.base(imgpath2,'1','100'))