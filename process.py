import cv2
import sys
import numpy as np

class ColorLapse:
  def __init__(self, filename):
    self.filename = filename
    self.color_img = cv2.imread(filename, cv2.CV_LOAD_IMAGE_COLOR)
    self.img = None
    self.window = 'window'
    #self.greyscale()
    #self.normalize()
    self.threshold()

  # spreads the intensities eveny throught the spectrum
  def normalize(self):
    self.img *= 255.0/self.img.max()

  def greyscale(self):
    self.img = np.zeros((self.color_img.shape[0],self.color_img.shape[1]), dtype=self.color_img.dtype)
    self.img [:,:] = self.color_img[:,:,0]

  # turns the  image into pure black and white
  def threshold(self):
    self.img = np.zeros((self.color_img.shape[0],self.color_img.shape[1]), dtype=self.color_img.dtype)
    thresh_val = 50
    rows, cols, temp = self.color_img.shape
    for row in range(rows):
      for col in range(cols):
        #print self.color_img[row][col]
        if self.color_img[row][col][2] > 140 and not (self.color_img[row][col][1] > 50 or self.color_img[row][col][0] > 50):
          self.img[row][col] = 0
        else:
          self.img[row][col] = 255

  # goes through the pixel and expands those that are colored 
  def expand_pixels(self):
    return -1

if __name__ == "__main__":
  cl = ColorLapse(sys.argv[1])
  cv2.namedWindow(cl.window)
  cv2.imshow(cl.window, cl.img)
  cv2.waitKey(0)
  cv2.destroyAllWindows()
