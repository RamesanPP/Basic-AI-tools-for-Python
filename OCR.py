from PIL import Image
import pytesseract
import numpy as np
# import cv2


def read_image(file):
    img = np.array(Image.open(file))
    text = pytesseract.image_to_string(img)
    print(text)
    return text

from transformers import pipeline

def qa(file_path):
    nlp = pipeline(
    "document-question-answering",
    model="impira/layoutlm-document-qa")

    answer = nlp(
    file_path,
    "**Your Question Here**")

    response = {
        "Answer": answer[0]["answer"],}
    
    return response