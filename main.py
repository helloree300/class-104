import cv2
image1 = cv2.imread("butterfly.jpg")
cv2.imshow("display image",image1)
image2 = cv2.cvtColor(image1,cv2.COLOR_RGB2GRAY)
cv2.imshow("show image",image2)
cv2.waitKey(0)
