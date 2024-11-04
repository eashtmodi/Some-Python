import cv2
import numpy as np
pts1=np.zeros((4,2),np.int)
count=0

def mousePoints(event,x,y,flags,param):
    global count
    if event==cv2.EVENT_LBUTTONDOWN:
        if count<4: 
            pts1[count]=x,y
        if count==4:
            print(pts1)
            width,height=img.shape[0:2]
            pts2=np.array([[0,0],[width,0],[0,height],[width,height]])
            pers=cv2.getPerspectiveTransform(pts1,pts2)
            scan=cv2.warpPerspective(img,pers,(width,height))
            cv2.imshow("scan",scan)

        count=count+1
        print(x,y)

img=cv2.imread('TargetImage.jpeg')



cv2.imshow("image",img)


cv2.setMouseCallback("image",mousePoints)






cv2.waitKey(0)

