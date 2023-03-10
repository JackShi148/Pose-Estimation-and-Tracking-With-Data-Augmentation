import cv2
import random
import os

path = "images/original"


def Flipping():
    num = 0
    for file_name in os.listdir(path):
        if random.randrange(-1, 1) < 0:  # 选择50%的图片进行翻转
            continue
        else:
            img = cv2.imread(path + "/" + file_name)
            rand = random.randint(-1, 2)

            # 随机翻转
            img_change = cv2.flip(img, rand)
            cv2.imwrite("images/Flipping/imgFlip{}.png".format(num), img_change)
            num = num + 1
            # cv2.imshow("new_image", img_change)
            # cv2.waitKey(0)
