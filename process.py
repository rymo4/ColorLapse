import cv2
import sys
import numpy as np


class ColorLapse:
  def __init__(self, filename):
    self.filename = filename
    self.color_img = cv2.imread(filename, cv2.CV_LOAD_IMAGE_COLOR)
    self.img = None
    self.window = 'window'

  def greyscale(self):
    return 1

  # spreads the intensities eveny throught the spectrum
  def normalize(self, img):
    return img * 255.0/img.max()

  # turns the  image into pure black and white
  def threshold(self):
    return 1

if __name__ == "__main__":
  cl = ColorLapse(sys.argv[1])
  cv2.namedWindow(cl.window)

  cv2.imshow(cl.window, cl.color_img)

  cv2.waitKey(0)
  cv2.destroyAllWindows()
