import cv2 as cv
from matplotlib.pyplot import imshow
import numpy as np

#convert it to gray scale

originalImg = cv.imread("19.1 capstone_coins.png")
originalImg = cv.resize(originalImg, (int(originalImg.shape[1] * 0.9), int(originalImg.shape[0] * 0.9)), interpolation=cv.INTER_AREA)
# cv.imshow("Original Image", originalImg)
cv.waitKey(0)
grayscaleImg = cv.cvtColor(originalImg, cv.COLOR_RGB2GRAY)


#Blurring
blurredImg = cv.GaussianBlur(grayscaleImg, (7, 7), cv.BORDER_DEFAULT)



#Hough algorthim
circles = cv.HoughCircles(blurredImg, cv.HOUGH_GRADIENT_ALT, 1, 50, param2= 0.9, maxRadius=-1)
for circle in circles[0, :]:
    output = cv.circle(originalImg, (int(circle[0]), int(circle[1])), int(circle[2]), (0, 255, 0), 2)
    output = cv.circle(output, (int(circle[0]), int(circle[1])), 1, (0, 0, 255), 2)
    if 90 < circle[2] < 100:
        output = cv.putText(output, "2p", (int(circle[0]), int(circle[1])),cv.FONT_HERSHEY_PLAIN, 3, (0, 0, 0), 2)
    elif 80 < circle[2] < 90:
        output = cv.putText(output, "10p", (int(circle[0]), int(circle[1])), cv.FONT_HERSHEY_PLAIN, 3, (0, 0, 0), 2)
    elif 70 < circle[2] < 80:
        output = cv.putText(output, "1p", (int(circle[0]), int(circle[1])), cv.FONT_HERSHEY_PLAIN, 3, (0, 0, 0), 2)
    elif 60 < circle[2] < 70:
        output = cv.putText(output, "5p", (int(circle[0]), int(circle[1])), cv.FONT_HERSHEY_PLAIN, 3, (0, 0, 0), 2)


#Edges 
blurredImg = cv.GaussianBlur(grayscaleImg, (3, 3), cv.BORDER_DEFAULT)

canny = cv.Canny(blurredImg, 10, 10)
# cv.imshow("canny", canny)
lines = cv.HoughLinesP(canny, 1, np.pi/180, 100)
print(lines)
for line in lines[0, :]:
    output = cv.line(output, (int(line[0]), int(line[1])), (int(line[1]), int(line[2])), (0, 255, 0), 2)
cv.imshow("output", output)
cv.waitKey(0)

