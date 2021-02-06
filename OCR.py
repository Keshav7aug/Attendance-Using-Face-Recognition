#from PIL import Image
#import pytesseract
#import inspect
import cv2
import os
print(os.getcwd())
img=cv2.imread("Icard.jpg")
cv2.imshow("img",img)
cv2.waitKey(0)
cv2.destroyAllWindows()