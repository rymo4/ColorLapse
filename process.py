import cv2
import sys
import numpy as np

class ColorLapse:
  def __init__(self, filename, pen_color):
    self.filename = filename
    self.color_img = cv2.imread(filename, cv2.CV_LOAD_IMAGE_COLOR)
    self.img = None
    self.window = 'window'
    self.threshold_ink()
    self.color_ink(pen_color)

  # turns the  image into pure black and white
  def threshold_ink(self):
    self.img = np.zeros((self.color_img.shape[0],self.color_img.shape[1]), dtype=self.color_img.dtype)
    thresh_val = 50
    rows, cols, temp = self.color_img.shape
    for row in range(rows):
      for col in range(cols):
        #print self.color_img[row][col]
        if self.color_img[row][col][2] > 140 and not (self.color_img[row][col][1] > 50 or self.color_img[row][col][0] > 50):
          self.img[row][col] = 0
          self.expand_pixel(row, col)
        else:
          self.img[row][col] = 255

  def color_ink(self, color):
    self.img = abs(self.img - 255)
    for i in range(3):
      self.color_img[:,:,i] = self.img * color[i]
    rows, cols, temp = self.color_img.shape
    for row in range(rows):
      for col in range(cols):
        rgb = self.color_img[row][col]
        if rgb[0] == 0 and rgb[1] == 0 and rgb[2] == 0:
          self.color_img[row][col]= np.array([255, 255, 255])


  def expand_pixel(self, row, col):
    width, height, t = self.color_img.shape
    if row <= 1 or row >= (width - 1) or col <= 1 or col >= (height -1):
      return
    self.img[row-1][col] = 0
    self.img[row+1][col] = 0
    self.img[row-1][col-1] = 0
    self.img[row-1][col+1] = 0
    self.img[row+1][col-1] = 0
    self.img[row+1][col+1] = 0
    self.img[row][col-1] = 0
    self.img[row][col+1] = 0

if __name__ == "__main__":
  cl = ColorLapse(sys.argv[1], map(int, sys.argv[2:5]))
  cv2.namedWindow(cl.window)
  cv2.imshow(cl.window, cl.color_img)
  cv2.waitKey(0)
  cv2.destroyAllWindows()
