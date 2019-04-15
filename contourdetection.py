import numpy as numpy
import cv2

img= cv2.imread('/media/glenja/New Volume/opencv/images/4.jpg',-1)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(gray, (5, 5), 0)
(t, binary) = cv2.threshold(blur, 127, 255, cv2.THRESH_BINARY)

# find contours
_, contours = cv2.findContours(binary, 1,2)

# print table of contours and sizes
print("Found %d objects." % len(contours))
for (i, c) in enumerate(contours):
    print("\tSize of contour %d: %d" % (i, len(c)))

# draw contours over original image
length = len(contours)
# print(length)
if length > 0:
        for i in range(len(contours)):
            cv2.drawContours(img, contours, i, (0,255,0), 2, cv2.LINE_8)

# display original image with contours
cv2.namedWindow("output", cv2.WINDOW_NORMAL)
cv2.imshow("output", binary)
cv2.waitKey(0)