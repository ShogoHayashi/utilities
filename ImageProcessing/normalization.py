import argparse
import cv2
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


def read_image(image_data_path, save_file_name='sample.png'):
    img = cv2.imread(image_data_path)
    img = do_normalization(img, [-150, 250], [0, 255])
    cv2.imwrite(save_file_name, img)


if __name__ == '__main__':
        
    parser = argparse.ArgumentParser()
    parser.add_argument('image_data_path') 
    parser.add_argument('--save_file_name', default = 'sample.png')           
    
    args = parser.parse_args()
    
    read_image(args.image_data_path, args.save_file_name)
