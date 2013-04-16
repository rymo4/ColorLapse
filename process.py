import cv2
import sys
import numpy as np

if len(sys.argv) != 2:
  print "Usage : python process.py <image_file>"
else:
  img = cv2.imread(sys.argv[1], cv2.CV_LOAD_IMAGE_COLOR)
  if (img == None):
    print "Could not open or find the image"
  else:
    window = 'window'
    cv2.namedWindow(window)
    cv2.imshow(window, img)
    print "size of image: ", img.shape
    cv2.waitKey(0)
    cv2.destroyAllWindows()
