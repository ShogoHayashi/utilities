import numpy as np

def do_normalization(src_img, src_range, dst_range):
    dst_img = np.copy(src_img)

    slope = (float(dst_range[1]) - float(dst_range[0]))\
            / (float(src_range[1]) - float(src_range[0]))

    dst_img = (dst_img.astype(np.float64) - float(src_range[0])) * slope\
              + float(dst_range[0])

    dst_img[dst_img < dst_range[0]] = dst_range[0]
    dst_img[dst_img > dst_range[1]] = dst_range[1]

    return dst_img.astype(np.uint8)