import cv2
import math
import numpy as np

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


    # mirror border
    L = cv2.copyMakeBorder(L, border, border, border, border, cv2.BORDER_REFLECT)
    a = cv2.copyMakeBorder(a, border, border, border, border, cv2.BORDER_REFLECT)
    b = cv2.copyMakeBorder(b, border, border, border, border, cv2.BORDER_REFLECT)

    # L = makeBorder(L, border)
    # a = makeBorder(a, border)
    # b = makeBorder(b, border)

    # convertto grayscale
    g_im = np.empty(L.shape)
    g_im.dtype = L.dtype
    g_im = (0.29894 * L) + (0.58704 * a) + (0.11402 * b)
    # for i in range(0, L.shape[0]):
    #     for j in range(0, L.shape[1]):
    #         g_im[i][j] = (0.29894 * L[i][j]) + (0.58704 * a[i][j]) + (0.11402 * b[i][j])

    # gamma correct
    np.power(L, 2.5)
    np.power(a, 2.5)
    np.power(b, 2.5)

    print (L.dtype)
    print (a.dtype)
    print (b.dtype)

    # rgb_im_temp = cv2.merge([L,a,b])
    # print (rgb_im_temp.shape)

    # Convert to Lab color space
    # dest_im = cv2.cvtColor(rgb_im_temp, cv2.COLOR_RGB2Lab)
    # L,a,b = cv2.split(rgb_im_temp)
    # print (rgb_im_temp.shape)
    # print (L)
    x_l = (0.412453 * L) +  (0.357580 * a) + (0.180423 * b)
    y_a = (0.212671 * L) +  (0.715160 * a) + (0.072169 * b)
    z_b = (0.019334 * L) +  (0.119193 * a) + (0.950227 * b)
    # D65 white point reference
    x_ref = 0.950456
    y_ref = 1.000000
    z_ref = 1.088754
    # threshold value
    threshold = 0.008856
    # convert XYZ to Lab
    for i in range(0, L.shape[0]):
        for j in range(0, L.shape[1]):
            x = x_l[i][j] / x_ref
            y = y_a[i][j] / y_ref
            z = z_b[i][j] / z_ref
            # compute fx, fy, fz
            if x > threshold:
                fx = math.pow(x,(1.0/3.0))
            else:
                fx = (7.787*x + (16.0/116.0))

            if y > threshold:
                fy = math.pow(y,(1.0/3.0))
            else:
                fy = (7.787*y + (16.0/116.0))
            
            if z > threshold:
                fz = math.pow(z,(1.0/3.0))
            else:
                fz = (7.787*z + (16.0/116.0))

            # compute Lab color value
            if y > threshold:
                x_l[i][j] = (116*math.pow(y,(1.0/3.0)) - 16)
            else:
                x_l[i][j] = 903.3*y
            
            y_a[i][j] = 500 * (fx - fy)
            z_b[i][j] = 200 * (fy - fz)
    L = x_l
    a = y_a
    b = z_b
    
    

    # print (L)
    # print (a)
    # print (b)
    # for i in range(0, L.shape[0]):
    #     for j in range(0, L.shape[1]):
    #         L[i][j] = pow(L[i][j], 2.5)
    #         a[i][j] = pow(a[i][j], 2.5)
    #         b[i][j] = pow(b[i][j], 2.5)

    


    print (L.shape)
    print (a.shape)
    print (b.shape)



    return [0, 0, 0,  0,  0, 0, 0, 0, 0, 0, 0,  0,  0]

# def makeBorder(L, border):
#     pass