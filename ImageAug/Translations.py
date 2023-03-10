import numpy as np
import cv2
import random
import os

file_path = "images/original"


def Translation():
    num = 0
    for img_name in os.listdir(file_path):
        if random.randrange(-1, 1) < 0:  # 选择50%的图片进行平移
            continue
        else:
            img = cv2.imread(file_path + '/' + img_name)
            height, width = img.shape[:2]

            x_change = random.randint(-500, 500)
            y_change = random.randint(-500, 500)

            # 平移矩阵
            if x_change < 0 and y_change < 0:
                img_change1 = cv2.copyMakeBorder(img, 0, abs(y_change)+300, 0, abs(x_change)+300,
                                                 borderType=cv2.BORDER_REPLICATE)
            if x_change > 0 and y_change < 0:
                img_change1 = cv2.copyMakeBorder(img, 0, abs(y_change)+300, abs(x_change)+300, 0,
                                                 borderType=cv2.BORDER_REPLICATE)
            if x_change < 0 and y_change > 0:
                img_change1 = cv2.copyMakeBorder(img, abs(y_change)+300, 0, 0, abs(x_change)+300,
                                                 borderType=cv2.BORDER_REPLICATE)
            else:
                img_change1 = cv2.copyMakeBorder(img, abs(y_change)+300, 0, abs(x_change)+300, 0, borderType=cv2.BORDER_REPLICATE)
            M = np.array([[1, 0, -200], [0, 1, -200]], dtype=np.float32)
            img_change = cv2.warpAffine(img_change1, M, dsize=(int(width), int(height)), borderValue=(255, 255, 255))
            cv2.imwrite("images/Translation/imgTrans{}.png".format(num), img_change)
            num = num + 1
            # cv2.imshow("show", img_change)
            # cv2.waitKey(0)
