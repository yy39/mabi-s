import cv2
import pytesseract

pytesseract.pytesseract.tesseract_cmd = 'C:\Program Files\Tesseract-OCR\tesseract.exe'

img = cv2.imread('test.png')
grayImg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

ret, thresh = cv2.threshold(img, 220, 255, cv2.THRESH_BINARY) 

cv2.imshow('test.png', img)
cv2.imshow('testGrayscale.png', grayImg)
cv2.imshow('threshold', thresh)
cv2.waitKey(0)
cv2.destroyAllWindows()