import cv2
import sys
import numpy as np

expansion_width = 2;

class ColorLapse:
  def __init__(self, filename, pen_color):
    self.filename = filename
    self.pen_color = pen_color
    self.color_img = cv2.imread(filename, cv2.CV_LOAD_IMAGE_COLOR)
    self.img = None
    self.window = 'window'
    self.threshold_ink()
    #self.color_ink(pen_color)

  # turns the  image into pure black and white
  def threshold_ink(self):
    self.img = np.zeros((self.color_img.shape[0],self.color_img.shape[1], self.color_img.shape[2]), dtype=self.color_img.dtype)
    thresh_val = 50
    rows, cols, temp = self.color_img.shape
    for row in range(rows):
      for col in range(cols):
        if self.color_img[row][col][2] > 140 and not (self.color_img[row][col][1] > 50 or self.color_img[row][col][0] > 50):
          self.color_and_expand_pixel(row, col, expansion_width)
        else:
          self.img[row][col] = np.array([255, 255, 255])

  def color_and_expand_pixel(self, row, col, n=1):
    width, height, t = self.color_img.shape
    if not (row <= n or row >= (width - n) or col <= n or col >= (height -n)):
      for i in range (-n,n+1):
        for j in range(-n,n+1):
          self.img[row+i][col+j] = np.array(self.pen_color)
     

if __name__ == "__main__":
  cl = ColorLapse(sys.argv[1], map(int, sys.argv[2:5]))
  cv2.namedWindow(cl.window)
  cv2.imshow(cl.window, cl.img)
  cv2.waitKey(0)
  cv2.destroyAllWindows()
