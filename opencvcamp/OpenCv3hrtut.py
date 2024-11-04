import cv2
import sleep
# from matplotlib import pyplot as plt
print("Done")
img = cv2.imread("image001.jpeg")
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
_,thresh2 = cv2.threshold(gray,50, 255,cv2.THRESH_BINARY_INV)
contours, hierarchy = cv2.findContours(thresh2, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

cv2.drawContours(img, contours, -1, (255, 255, 0), 3)
cv2.imshow("img",img)
print(img.shape)
cv2.imshow("duh",thresh2)
mask=cv2.bitwise_and(img,img,mask=thresh2)
cv2.imshow("haha",mask)


cv2.waitKey(0)
cv2.destroyAllWindows()
