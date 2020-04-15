from cv2 import cv2

import numpy as np

image1 = cv2.imread("1.jpg")
image2 = cv2.imread("2.jpg")

image3 = cv2.imread("PP4A6535_20200301.jpg")
image4 = cv2.imread("PP4A6535_20200316.jpg")

difference1 = cv2.subtract(image1, image2)
result1 = not np.any(difference1)

difference2 = cv2.subtract(image3, image4)
result2 = not np.any(difference2)

if result1 is True:
  print(" ==> 两张图片一样")
else:
  cv2.imwrite("result1.jpg", difference1)
  print (" ==> 两张图片不一样")

if result2 is True:
  print(" ==> 两张图片一样")
else:
  cv2.imwrite("result2.jpg", difference2)
  print(" ==> 两张图片不一样")