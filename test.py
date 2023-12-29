from matplotlib import pyplot as plt
import numpy as np
import cv2 as cv

gotham_image = cv.imread("./gotham.jpg")

scale = cv.resize(gotham_image, None, fx=1.2, fy=1.2, interpolation=cv.INTER_LINEAR)
cv.imshow('Scaling - Linear Interpolation', scale)
cv.waitKey(0)