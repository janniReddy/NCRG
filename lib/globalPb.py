import cv2
import numpy as np
from scipy import ndimage
# from PIL import Image

def globalPb(imgFile, outFile = '', rsz = 1.0):
	"""compute Globalized Probability of Boundary of an image."""
	print ('inside globalPb')
	if (rsz <=0 or rsz > 1):
		print ('resizing factor rsz out of range (0,1]')
		return
	# im = Image.open(imgFile)
	# im.load()
	# data = np.asarray(im, dtype= "int64")
	im = cv2.imread(imgFile)
	# print (type(data))
	print (im)
	print (type(im))
	print (im.shape)
	print (im.size)
	print (im.dtype)
	im = im/255
	print (im.shape)
	print (im.size)
	print (im)
	print (im.dtype)
	[tx, ty, nchan] = im.shape
	orig_sz = [tx, ty]
	if 3==nchan:
		weights = [0  0  0.0039  0.0050  0.0058  0.0069  0.0040  0.0044  0.0049  0.0024  0.0027  0.0170  0.0074]
	else:
		weights = [ 0   0    0.0054         0         0         0         0         0         0    0.0048    0.0049    0.0264    0.0090]
	
globalPb('data/101087.jpg')