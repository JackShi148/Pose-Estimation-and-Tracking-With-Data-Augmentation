import cv2
import os
import random
import numpy as np

path = "images/original"



def Affine():
    num = 0
    for file_name in os.listdir(path):
        if random.randrange(-1, 1) < 0:
            continue
        else:
            img = cv2.imread(path + '/' + file_name)
            # cv2.imshow("original", img)
            # cv2.waitKey(0)

            height, width = img.shape[:2]

            point1 = np.float32([[150, 150], [400, 150], [600, 400]])
            point2 = np.float32([[80, 100], [400, 150], [900, 500]])
            point3 = np.float32([[250, 80], [400, 150], [450, 650]])

            # 随机仿射
            if random.randrange(-1, 1) > -0.5:
                M = cv2.getAffineTransform(point1, point2)
            else:
                M = cv2.getAffineTransform(point1, point3)
            img_change = cv2.warpAffine(img, M, (int(width), int(height)), borderValue=(255, 255, 255))
            cv2.imwrite("images/Affine/imgAff{}.png".format(num), img_change)
            num = num + 1

            # cv2.imshow("new", img_change)
            # cv2.waitKey(0)
