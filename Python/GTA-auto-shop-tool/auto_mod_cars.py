from PIL import Image
from pytesseract import pytesseract
import cv2
import numpy as np

#Define path to tessaract.exe
path_to_tesseract = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

#Define path to image
path_to_image = 'output.png'

#Point tessaract_cmd to tessaract.exe
pytesseract.tesseract_cmd = path_to_tesseract

img = cv2.imread('textimage.png')

# creating mask using thresholding over `red` channel (use better use histogram to get threshoding value)
# I have used 200 as thershoding value it can be different for different images
ret, mask = cv2.threshold(img[:, :,2], 225, 225, cv2.THRESH_BINARY)

mask3 = np.zeros_like(img)
mask3[:, :, 0] = mask
mask3[:, :, 1] = mask
mask3[:, :, 2] = mask

# extracting `orange` region using `biteise_and`
orange = cv2.bitwise_and(img, mask3)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img  = cv2.cvtColor(gray, cv2.COLOR_GRAY2BGR)

# extracting non-orange region
gray = cv2.bitwise_and(img, 255 - mask3)

# orange masked output
out = gray + orange

cv2.imwrite('output.png', orange)

#Open image with PIL
img = Image.open('output.png').convert('LA')

#Extract text from image
text = pytesseract.image_to_string(img)

print(text)