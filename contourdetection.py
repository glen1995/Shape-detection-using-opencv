import numpy as numpy
import cv2

img= cv2.imread('/media/glenja/New Volume/opencv/images/contour.jpg',-1)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#edge detection using canny
canny = cv2.Canny(gray,100,200)

# find contours
contours, _ = cv2.findContours(canny, 1,2)

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
cv2.imshow("output", img)
cv2.waitKey(0)