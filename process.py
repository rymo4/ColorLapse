import cv2
import sys
import numpy as np

if len(sys.argv) != 2:
  print "Usage : python process.py <image_file>"
else:
  color_img = cv2.imread(sys.argv[1], cv2.CV_LOAD_IMAGE_COLOR)
  img = cv2.cvtColor(color_img, cv2.COLOR_BGR2GRAY)

  if (img == None):
    print "Could not open or find the image"
  else:
    window = 'window'
    cv2.namedWindow(window)
    cv2.imshow(window, img)
    print "size of image: ", img.shape
    cv2.waitKey(0)
    cv2.destroyAllWindows()

class ColorLapse
  def __init__(self, filename):
    self.filename = filename

  def greyscale(self):
    self.image = cv2.cvtColor(self.color_image, cv2.COLOR_BGR2GRAY)

  def normalize(self):
    return None

  def threshold(self):
    thresh_val = 20
    cols, rows = self.image.shape()
    for row in range(cols):
      for cols in range(rows):
        if self.image[col][row] < thresh_val:
          self.image[col][row] = 0
        else:
          self.image[col][row] = 255

if __name__ == "__main__":
  