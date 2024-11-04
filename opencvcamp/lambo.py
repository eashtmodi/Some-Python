import cv2
import numpy as np

frameWidth= 150
frameHeight= 100
cap = cv2.VideoCapture(0) #not any with my link change 1 to 0 if not working
cap.set(3,frameWidth)
cap.set(4,frameHeight)
cap.set(10, 1000)

def stackImages(imgArray,scale,lables=[]):
    rows = len(imgArray)
    cols = len(imgArray[0])
    rowsAvailable = isinstance(imgArray[0], list)
    width = imgArray[0][0].shape[1]
    height = imgArray[0][0].shape[0]
    if rowsAvailable:
        for x in range ( 0, rows):
            for y in range(0, cols):
                imgArray[x][y] = cv2.resize(imgArray[x][y], (0, 0), None, scale, scale)
                if len(imgArray[x][y].shape) == 2: imgArray[x][y]= cv2.cvtColor( imgArray[x][y], cv2.COLOR_GRAY2BGR)
        imageBlank = np.zeros((height, width, 3), np.uint8)
        hor = [imageBlank]*rows
        hor_con = [imageBlank]*rows
        for x in range(0, rows):
            hor[x] = np.hstack(imgArray[x])
            hor_con[x] = np.concatenate(imgArray[x])
        ver = np.vstack(hor)
        ver_con = np.concatenate(hor)
    else:
        for x in range(0, rows):
            imgArray[x] = cv2.resize(imgArray[x], (0, 0), None, scale, scale)
            if len(imgArray[x].shape) == 2: imgArray[x] = cv2.cvtColor(imgArray[x], cv2.COLOR_GRAY2BGR)
        hor= np.hstack(imgArray)
        hor_con= np.concatenate(imgArray)
        ver = hor
    if len(lables) != 0:
        eachImgWidth= int(ver.shape[1] / cols)
        eachImgHeight = int(ver.shape[0] / rows)
        #print(eachImgHeight)
        for d in range(0, rows):
            for c in range (0,cols):
                cv2.rectangle(ver,(c*eachImgWidth,eachImgHeight*d),(c*eachImgWidth+len(lables[d])*13+27,30+eachImgHeight*d),(255,255,255),cv2.FILLED)
                cv2.putText(ver,lables[d],(eachImgWidth*c+10,eachImgHeight*d+20),cv2.FONT_HERSHEY_COMPLEX,0.7,(255,0,255),2)
    return ver

def empty(a):
    pass
while True:
    _, img =cap.read()

    img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    img_hsv_blur=cv2.GaussianBlur(img_hsv,(11,11),0)

    cv2.namedWindow("Callibration")
    cv2.resizeWindow("Callibration",640,220)
    cv2.createTrackbar("hue_min","Callibration",0,179,empty)
    cv2.createTrackbar("hue_max","Callibration",179,179,empty)
    cv2.createTrackbar("sat_min","Callibration",0,255,empty)
    cv2.createTrackbar("sat_max","Callibration",255,255,empty)
    cv2.createTrackbar("min_val","Callibration",0,255,empty)
    cv2.createTrackbar("max_val","Callibration",255,255,empty)

    hue_min=cv2.getTrackbarPos("hue_min","Callibration")
    hue_max=cv2.getTrackbarPos("hue_max","Callibration")
    sat_min=cv2.getTrackbarPos("sat_min","Callibration")
    sat_max=cv2.getTrackbarPos("sat_max","Callibration")
    min_val=cv2.getTrackbarPos("min_val","Callibration")
    max_val=cv2.getTrackbarPos("max_val","Callibration")
    print(min_val)
    kernel=np.ones((5,5),np.uint8)
    lower=np.array([hue_min,sat_min,min_val])
    upper=np.array([hue_max,sat_max,max_val])
    masked_img=cv2.inRange(img_hsv,lower,upper)
    new_img=cv2.bitwise_and(img,img,mask=masked_img)
    dil_new_img=cv2.dilate(new_img,kernel,iterations=1)
    img_erode=cv2.erode(new_img,kernel,iterations=1)

    cv2.resize(img,(150,100))
    cv2.resize(img_hsv,(150,100))
    cv2.resize(masked_img,(150,100))
    cv2.resize(new_img,(150,100))

    imgArray=([img,img_hsv,masked_img],[new_img,img_hsv_blur,dil_new_img],[img_erode,img_erode,img_erode])
    # labelArray=[["img","img_hsv"],["masked_img","new_img"]]
    stack=stackImages(imgArray,0.3)

    cv2.imshow("Window",stack)
    # # cv2.imshow("masked",imgHor2)
    #
    # # cv2.imshow("Orignal",img)
    # cv2.imshow("hsv_blur",img_hsv_blur)
    # cv2.imshow("mask",masked_img)
    # cv2.imshow("new",new_img)

    if cv2.waitKey(1) & 0xFF==ord(' '):
        break
cap.release()
cv2.destroyAllWindows()



