import numpy as np
import cv2
import math


def grayscale(L, a, b):
    """Compute a grayscale image from an RGB image."""
    print("inside gray scale function.............")
    g_im = np.empty(L.shape)
    g_im.dtype = L.dtype
    g_im = (0.29894 * L) + (0.58704 * a) + (0.11402 * b)
    return g_im

def rgb_to_lab(L, a, b):
    """Convert from RGB color space to Lab color space."""
    print("inside rgb to lab")
    # convert RGB to XYZ
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
    return [x_l, y_a, z_b]

def lab_normalize(l, a, b):
    """Normalize an Lab image so that values for each channel lie in [0,1]."""
    print("inside lab_normalize")
    # range for a, b channels
    ab_min = -73
    ab_max = 95
    ab_range = ab_max - ab_min
    # normalize Lab image
    for i in range(0, l.shape[0]):
        for j in range(0, l.shape[1]):
            l_val = l[i][j] / 100.0
            a_val = (a[i][j] - ab_min) / ab_range
            b_val = (b[i][j] - ab_min) / ab_range
            if l_val < 0:
                l_val = 0
            elif l_val > 1:
                l_val = 1
            
            if a_val < 0:
                a_val = 0
            elif a_val > 1:
                a_val = 1

            if b_val < 0:
                b_val = 0
            elif b_val > 1:
                b_val = 1
            l[i][j] = l_val
            a[i][j] = a_val
            b[i][j] = b_val
    return [l, a, b]


def quantize_values(src, n_bins):
    if(0 == n_bins):
        print("n_bins must be > 0")
        return
    dest = np.empty(src.shape)
    # dest.dtype = src.dtype
    for i in range(0, src.shape[0]):
        for j in range(0, src.shape[1]):
            d_bin = int(math.floor(src[i][j]*float(n_bins)))
            if d_bin == n_bins:
                d_bin = n_bins - 1
            dest[i][j] = d_bin
    return dest

def texton_filters(parameter_list):
    pass
