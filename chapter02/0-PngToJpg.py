import cv2
import sys

image = cv2.imread("MyPic.png", cv2.IMREAD_UNCHANGED)
print(image.shape)
if image is None:
    print('Failed to read image from file')
    sys.exit(1)

success = cv2.imwrite('MyPic.jpg', image)
if not success:
    print('Failed to write image to file')
    sys.exit(1)
