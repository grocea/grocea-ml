import cv2 as cv
import pytesseract
from matplotlib import pyplot as plt

image_path = "../data/images/tesseract-image.png"

image = cv.imread(image_path)

image_rgb = cv.cvtColor(image, cv.COLOR_BGR2RGB)

