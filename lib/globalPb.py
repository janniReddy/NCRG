import numpy as np
from scipy import ndimage
import cv2
from multiscalePb import multiscalePb
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
	im = im/255
	[tx, ty, nchan] = im.shape
	orig_sz = [tx, ty]
	if 3==nchan:
		weights = [0, 0, 0.0039, 0.0050, 0.0058, 0.0069, 0.0040, 0.0044, 0.0049, 0.0024, 0.0027, 0.0170, 0.0074]
	else:
		weights = [0, 0, 0.0054, 0, 0, 0, 0, 0, 0, 0.0048, 0.0049, 0.0264, 0.0090]
	# mPb
	[mPb, mPb_rsz, bg1, bg2, bg3, cga1, cga2, cga3, cgb1, cgb2, cgb3, tg1, tg2, tg3, textons] = multiscalePb(im, rsz)


globalPb('data/101087.jpg')