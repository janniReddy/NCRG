
from det_mPb import det_mPb

def multiscalePb(im, rsz = 1.0):
    """compute local contour cues of an image."""
    print ("inside multiscalePb")
    # default feature weights
    if im.shape[2] == 3:
        weights = [0.0146, 0.0145, 0.0163, 0.0210, 0.0243, 0.0287, 0.0166, 0.0185, 0.0204, 0.0101, 0.0111, 0.0141]
    else:
        im[:,:,2]=im[:,:,1]
        im[:,:,3]=im[:,:,1]
        weights = [0.0245, 0.0220, 0.0233, 0, 0, 0, 0, 0, 0, 0.0208, 0.0210, 0.0229]
    print (im)
    print (im.size)
    print (im.shape)
    # get gradients
    [bg1, bg2, bg3, cga1, cga2, cga3, cgb1, cgb2, cgb3, tg1, tg2, tg3, textons] = det_mPb(im)
    # det_mPb(im)

    # [mPb_nmax, mPb_nmax_rsz, bg1, bg2, bg3, cga1, cga2, cga3, cgb1, cgb2, cgb3, tg1, tg2, tg3, textons]
    return [100, 99, 98, 90, 89, 88, 80, 79, 78, 70, 69, 68, 60, 59, 58]