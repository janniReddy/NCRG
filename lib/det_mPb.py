import numpy as np
from pb_parts_final_selected import pb_parts_final_selected

def det_mPb(im):
    """compute image gradients."""
    [textons, bg_r3, bg_r5,  bg_r10,  cga_r5, cga_r10, cga_r20, cgb_r5, cgb_r10, cgb_r20, tg_r5,  tg_r10,  tg_r20] = pb_parts_final_selected(im[:,:,0],im[:,:,1],im[:,:,2])
    # pb_parts_final_selected(im[:,:,0],im[:,:,1],im[:,:,2])
    [sx, sy, sz] = im.shape
    temp = np.zeros((sx, sy, 8))
    for ori in range(0, 8):
        temp[:, :, ori] = bg_r3[ori]
    bg_r3 = temp

    for ori in range(0, 8):
        temp[:, :, ori] = bg_r5[ori]
    bg_r5 = temp

    for ori in range(0, 8):
        temp[:, :, ori] = bg_r10[ori]
    bg_r10 = temp

    bg1 = bg_r3
    bg2 = bg_r5
    bg3 = bg_r10
    



    return [bg1, bg2, bg3, cga1, cga2, cga3, cgb1, cgb2, cgb3, tg1, tg2, tg3, textons]
