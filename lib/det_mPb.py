
from pb_parts_final_selected import pb_parts_final_selected

def det_mPb(im):
    """compute image gradients."""
    [textons, bg_r3, bg_r5,  bg_r10,  cga_r5, cga_r10, cga_r20, cgb_r5, cgb_r10, cgb_r20, tg_r5,  tg_r10,  tg_r20] = pb_parts_final_selected(im[:,:,0],im[:,:,1],im[:,:,2])
    # pb_parts_final_selected(im[:,:,0],im[:,:,1],im[:,:,2])
    return [textons, bg_r3, bg_r5,  bg_r10,  cga_r5, cga_r10, cga_r20, cgb_r5, cgb_r10, cgb_r20, tg_r5,  tg_r10,  tg_r20]
