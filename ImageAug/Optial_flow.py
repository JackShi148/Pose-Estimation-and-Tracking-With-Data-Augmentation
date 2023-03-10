#!/usr/bin/env python

import numpy as np
import cv2

cap = cv2.VideoCapture("images/Dog4_newDLC.mp4")
ret, frame = cap.read()
# params for ShiTomasi corner detection

feature_params = dict(maxCorners=100,
                      qualityLevel=0.3,
                      minDistance=7,
                      blockSize=7)

# Parameters for lucas kanade optical flow
lk_params = dict(winSize=(15, 15),
                 maxLevel=4,
                 criteria=(cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 10, 0.03))

# Create some random colors
color = np.random.randint(0, 255, (100, 3))

# Take first frame and find corners in it
# ret, old_frame = cap.read()
# filename = './data/figure_1_reg.png'
old_frame = frame
# print old_frame.shape
old_gray = cv2.cvtColor(old_frame, cv2.COLOR_BGR2GRAY)
# p0 = cv2.goodFeaturesToTrack(old_gray, mask = None, **feature_params)
p0 = np.array([
    [np.array([1311.336792, 338.217254])],  ## left ear
    [np.array([757.323486, 330.453064])],  ## right ear
    [np.array([1170.434692, 445.750702])],  ## left eye
    [np.array([907.260498, 447.582092])],  ## right eye
    [np.array([1067.489624, 714.866455])],  ## nose
    [np.array([1051.925903, 802.196167])]],  ## mouth
    # [np.array([942.,385.])], ## right hip
    # [np.array([850.,321.])]], ## left elbow
    # [np.array([973.,321.])]], ## right elbow
    np.float32)

# for item in p0:
#     item = np.ndarray(item)
#     for it in item:
#         it = np.ndarray(it)

# Create a mask image for drawing purposes
mask = np.zeros_like(old_frame)

# filenames = ['./data/figure_2_reg.png', './data/figure_3_reg.png', './data/figure_4_reg.png']

count = 0
while cap.isOpened():
    # ret,frame = cap.read()
    re, frame = cap.read()
    # frame = cv2.imread(file)
    frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # calculate optical flow
    p1, st, err = cv2.calcOpticalFlowPyrLK(old_gray, frame_gray, p0, None, **lk_params)
    # Select good points
    good_new = p1[st == 1]
    good_old = p0[st == 1]
    # draw the tracks
    for i, (new, old) in enumerate(zip(good_new, good_old)):
        a, b = new.ravel()
        c, d = old.ravel()
        mask = cv2.line(mask, (int(a), int(b)), (int(c), int(d)), color[i].tolist(), 2)
        frame = cv2.circle(frame, (int(a), int(b)), 5, color[i].tolist(), -1)
    img = cv2.add(frame, mask)
    cv2.imwrite('images/test/imgOF{}.png'.format(count), img)
    count += 1
    # cv2.imshow('frame',img)
    # k = cv2.waitKey(30) & 0xff
    # if k == 27:
    #     break
    # Now update the previous frame and previous points
    old_gray = frame_gray.copy()
    p0 = good_new.reshape(-1, 1, 2)
# cv2.destroyAllWindows()
# cap.release()
