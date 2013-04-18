import cv2
import cv2.cv as cv
import os
import sys
import numpy as np

expansion_width = 2;

class ColorLapse:
  def __init__(self, image, pen_color):
    self.color_img = image#cv2.imread(filename, cv2.CV_LOAD_IMAGE_COLOR)
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
          self.expand_pixel(row, col, expansion_width)
        else:
          self.img[row][col] = 255

  def expand_pixel(self, row, col, n=1):
    width, height, t = self.color_img.shape
    if not (row <= n or row >= (width - n) or col <= n or col >= (height -n)):
      for i in range (-n,n+1):
        for j in range(-n,n+1):
          self.img[row+i][col+j] = 0

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


if __name__ == "__main__":
  vid = cv.CaptureFromFile('vid2.mov')
  img = cv.QueryFrame(vid)
  while img:
    print 'loopin!'
    tmp = cv.CreateImage(cv.GetSize(img),8,3)
    cv.CvtColor(img, tmp, cv.CV_BGR2RGB)
    img = np.asarray(cv.GetMat(tmp))
    print 'got the image as a numpy array'

    cl = ColorLapse(img, [50, 200, 50])
    cv2.namedWindow(cl.window)
    cv2.imshow(cl.window, cl.color_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    img = cv.QueryFrame(vid)

  #cl = ColorLapse(sys.argv[1], map(int, sys.argv[2:5]))
