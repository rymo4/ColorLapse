import cv2
import sys
import numpy as np

class ColorLapse:
  def __init__(self, filename):
    self.filename = filename
    self.color_img = cv2.imread(filename, cv2.CV_LOAD_IMAGE_COLOR)
    self.img = None
    self.window = 'window'
    self.greyscale()
    self.normalize()
    self.threshold()

  # spreads the intensities eveny throught the spectrum
  def normalize(self):
    self.img *= 255.0/self.img.max()

  def greyscale(self):
    self.img = cv2.cvtColor(self.color_img, cv2.COLOR_BGR2GRAY)

  # turns the  image into pure black and white
  def threshold(self):
    thresh_val = 20
    cols, rows = self.img.shape
    for col in range(cols):
      for row in range(rows):
        if self.img[col][row] < thresh_val:
          self.img[col][row] = 0
        else:
          self.img[col][row] = 255

if __name__ == "__main__":
  cl = ColorLapse(sys.argv[1])
  cv2.namedWindow(cl.window)

  cv2.imshow(cl.window, cl.img)

  cv2.waitKey(0)
  cv2.destroyAllWindows()
