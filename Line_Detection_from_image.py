import cv2
import numpy as np
import matplotlib.pyplot as plt

def canny(image):
    gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
    blured = cv2.GaussianBlur(gray,(5,5),0)
    can =cv2.Canny(blured,50,150)
    return can

def display_lines(image,lines):
    line_image = np.zeros_like(image)
    if lines is not None:
        for line in lines:
            x1, y1, x2, y2 = line.reshape(4)
            cv2.line(line_image, (x1,y1),(x2,y2),(255,0,0),10)
    return line_image


def region_of_interest(image):
    h = image.shape[0]
    poly = np.array([[(200,100),(0,165),(0,h),(h,h),(h,165)]])
    mask = np.zeros_like(image)
    cv2.fillPoly(mask,poly,255)
    masked_image = cv2.bitwise_and(image,mask)
    return masked_image
image = cv2.imread('Road.jpg')

side_line_image = np.copy(image)
canny_image = canny(side_line_image)
cropped_image = region_of_interest(canny_image)
lines = cv2.HoughLinesP(cropped_image, 2 , np.pi/180, 100, np.array([]), minLineLength = 40, maxLineGap = 5)
image_with_line = display_lines(side_line_image,lines)
combined_image = cv2.addWeighted(side_line_image,0.8, image_with_line, 1,1)
cv2.imshow('result',combined_image)
cv2.waitKey()

# cap = cv2.VideoCapture("test2.mp4")
# while(cap.isOpened()):
#     _, frame = cap.read()
#     canny_image = canny(frame)
#     cropped_image = region_of_interest(canny_image)
#     lines = cv2.HoughLinesP(cropped_image, 2 , np.pi/180, 100, np.array([]), minLineLength = 40, maxLineGap = 5)
#     line_image = display_lines(frame,lines)
#     combo_image = cv2.addWeighted(frame,0.8, line_image, 1,1)
#     cv2.imshow('result',combo_image)
#     if cv2.waitKey(1)== ord('q'):
#         break
# cap.release()
# cv2.destroyAllWindows()    
