import cv2
import os
import random
import numpy as np

path = "images/original"
face_location = [400, 200, 1500, 800]

x = face_location[0]
y = face_location[1]
w = face_location[2] - face_location[0]
h = face_location[3] - face_location[1]


# 局部马赛克处理
def mosaic(img, x, y, w, h, neighbor=15):
    """

    :param img:
    :param x:  马赛克左顶点x坐标
    :param y:  马赛克左顶点y坐标
    :param w:  马赛克宽度
    :param h:  马赛克高度
    :param neighbor:  马赛克小块宽度
    """
    for i in range(0, h, neighbor):
        for j in range(0, w, neighbor):
            rect = [j + x, i + y]
            color = img[i + y][j + x].tolist()  # 每次都选左上角像素颜色代替马赛克小块颜色
            left_up = (rect[0], rect[1])
            x2 = rect[0] + neighbor - 1
            y2 = rect[1] + neighbor - 1
            if x2 > x + w:
                x2 = x + w
            if y2 > y + h:
                y2 = y + h
            right_down = (x2, y2)
            cv2.rectangle(img, left_up, right_down, color, thickness=-1)  # 将马赛克小块颜色替换

    return img


def do_mosaic():
    num = 0
    for file_name in os.listdir(path):
        if random.randrange(-1, 1) < 0:
            continue
        else:
            img = cv2.imread(path + '/' + file_name)
            img_change = mosaic(img, x, y, w, h)
            cv2.imwrite("images/Mosaic/imgMos{}.png".format(num), img_change)
            num = num + 1
            # cv2.imshow("new", img_change)
            # cv2.waitKey(0)


