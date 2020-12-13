from encoding import Encoding
from recognition import Recognition
import os
import re


class Console:
    def __init__(self,input_path):
        recognition = Recognition(input_path)
        


#solo se ejecuta una vez
""" dirname = os.path.join(os.getcwd(), 'prueba6400')
imgpath = dirname + os.sep 
encode = Encoding(imgpath) """

dirname2 = os.path.join(os.getcwd(), 'pruebaInputs')
imgpath2 = dirname2 + os.sep 
console = Console(imgpath2)
