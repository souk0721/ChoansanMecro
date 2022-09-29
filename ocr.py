import numpy as np
from pytesseract import Output
import pytesseract
import cv2
from PIL import Image

def ocr_text(file):    
    filename =file
    img1 = np.array(Image.open(filename))
    text = pytesseract.image_to_string(img1)
    # print (text[0:4])
    return(text[0:4])