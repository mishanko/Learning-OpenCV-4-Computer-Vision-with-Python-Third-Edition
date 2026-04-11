import cv2
import numpy as np

img = cv2.imread("MyPic.jpg")
cv2.imshow("Image", img)
cv2.waitKey()
cv2.destroyAllWindows()