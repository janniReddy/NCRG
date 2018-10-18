import cv2
import math
import numpy as np

from lib_image import *

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
    # sigma_tg_filt_sm = 2.0                  # sigma for small tg filters 
    # sigma_tg_filt_lg = math.sqrt(2) * 2.0   # sigma for large tg filters 

    # parameters - radii
    n_bg = 3
    n_cg = 3
    n_tg = 3
    r_bg = [ 3, 5, 10 ]
    r_cg = [ 5, 10, 20 ]
    r_tg = [ 5, 10, 20 ]

    # convert to grayscale
    g_im = grayscale(L, a, b)

    # mirror border
    L = cv2.copyMakeBorder(L, border, border, border, border, cv2.BORDER_REFLECT)
    a = cv2.copyMakeBorder(a, border, border, border, border, cv2.BORDER_REFLECT)
    b = cv2.copyMakeBorder(b, border, border, border, border, cv2.BORDER_REFLECT)
    
    # gamma correct
    np.power(L, 2.5)
    np.power(a, 2.5)
    np.power(b, 2.5)
    # rgb_im_temp = cv2.merge([L,a,b])
    # print (rgb_im_temp.shape)

    # Convert to Lab color space
    L, a, b = rgb_to_lab(L, a, b)
    L, a, b = lab_normalize(L, a, b)

    # quantize color channels
    Lq = quantize_values(L, num_L_bins)
    aq = quantize_values(a, num_a_bins)
    bq = quantize_values(b, num_b_bins)

    # compute texton filter set
    # filters_large = texton_filters(n_ori, sigma_tg_filt_lg)
    print("before filters")
    filters = texton_filters(n_ori)
    print("after filters")
    print(len(filters))
    
    k = 64

    # compute textons
    print("before compute_textons called")
    print(g_im.shape)
    map, textons = compute_textons(g_im, border, filters, k)
    print("after compute_textons called")
    print(map.shape)
    print(textons.shape)
    print((g_im == map).all())

    # writing map object to a file
    fo = open("testing_map_obj2.txt", "w")
    for i in range(0, map.shape[0]):
        for j in range(0, map.shape[1]):
            fo.write(map[i][j].astype(str))
            if j != map.shape[1] - 1:
                fo.write(",")
        fo.write("\n")
    fo.close()
    print("after writing the map object")

    # compute bg histogram smoothing kernel
    bg_smooth_kernel = gaussian(sigma = bg_smooth_sigma*num_L_bins)
    cga_smooth_kernel = gaussian(cg_smooth_sigma*num_a_bins)
    cgb_smooth_kernel = gaussian(cg_smooth_sigma*num_b_bins)


    return [0, 0, 0,  0,  0, 0, 0, 0, 0, 0, 0,  0,  0]