import math

def pb_parts_final_selected(L, a, b):
    print ("inside pb_parts_final_selected function")
    # parameters - binning and smoothing
    n_ori = 8                              # number of orientations 
    num_L_bins = 25                        # # bins for bg 
    num_a_bins = 25                        # # bins for cg_a 
    num_b_bins = 25                        # # bins for cg_b 
    bg_smooth_sigma = 0.1                  # bg histogram smoothing sigma 
    cg_smooth_sigma = 0.05                 # cg histogram smoothing sigma 
    border = 30                            # border pixels 
    sigma_tg_filt_sm = 2.0                  # sigma for small tg filters 
    sigma_tg_filt_lg = math.sqrt(2) * 2.0   # sigma for large tg filters 

    # parameters - radii
    n_bg = 3
    n_cg = 3
    n_tg = 3
    r_bg = [ 3, 5, 10 ]
    r_cg = [ 5, 10, 20 ]
    r_tg = [ 5, 10, 20 ]

    # compute bg histogram smoothing kernel
    

    # return [textons, bg_r3, bg_r5,  bg_r10,  cga_r5, cga_r10, cga_r20, cgb_r5, cgb_r10, cgb_r20, tg_r5,  tg_r10,  tg_r20]