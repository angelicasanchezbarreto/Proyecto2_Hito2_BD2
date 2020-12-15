from encoding import Encoding
from recognition import Recognition
import os
import re

class Console:
    def __init__(self,input_path):
        option = self.options()
        recognition = Recognition(input_path,option)

    def options(self):
        print("Which method do you want to use:")
        print("1. KNN Sequential Search")
        print("2. KNN Rtree Search")
        print("3. Range Search")
        number = input()
        return number


#solo se ejecuta una vez
""" dirname = os.path.join(os.getcwd(), 'images/prueba6400')
imgpath = dirname + os.sep 
encode = Encoding(imgpath) """

dirname2 = os.path.join(os.getcwd(), 'pruebaInputs')
imgpath2 = dirname2 + os.sep 
console = Console(imgpath2)