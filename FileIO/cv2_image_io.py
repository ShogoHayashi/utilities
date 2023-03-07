import argparse
import cv2



def read_image(file_name):
    img = cv2.imread("file_name")
    save_image(img)


def save_image(img):
    cv2.imwrite('sample.png', img)


if __name__ == '__main__':
        
    parser = argparse.ArgumentParser()
    parser.add_argument('file_namge')           
    args = parser.parse_args()
    
    read_image(args.file_name)