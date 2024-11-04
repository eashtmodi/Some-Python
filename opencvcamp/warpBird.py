import cv2
import numpy as np
imgName=str(input("Tell the name of Image: "
                  "book.jpeg,book0.jeg,TargetImage.jpeg: "))
img = cv2.imread(imgName)
circles =np.zeros((4,2),dtype=int)

count=0

def mousePoints(event, x, y, flags, params):
    global count
    if event == cv2.EVENT_LBUTTONDOWN:

        print(x, ' ', y)
        circles[count]=x,y
        count= count+1
        print(circles)
        print(count)



while True:

    if count==4:
        width, height = 250, 350

        points = np.float32([circles[0],circles[1],circles[2],circles[3]])
        points0 = np.float32([[0,0],[width,0],[0,height],[width,height]])



        matrix= cv2.getPerspectiveTransform(points,points0)

        output=cv2.warpPerspective(img,matrix,(width,height))
        cv2.imshow("IDK", output)
        cv2.circle(img, (circles[0][0], circles[0][1]), 10, (0, 0, 255), cv2.FILLED)
        cv2.circle(img, (circles[1][0], circles[1][1]), 10, (0, 255, 0), cv2.FILLED)
        cv2.circle(img, (circles[2][0], circles[2][1]), 10, (255, 0, 0), cv2.FILLED)
        cv2.circle(img, (circles[3][0], circles[3][1]), 10, (255, 0, 255), cv2.FILLED)

        if cv2.waitKey(1) & 0xFF == ord(' '):  # Stop if spacebar is detected
            break
            cv2.destroyAllWindows()
    cv2.imshow("IMAGE",img)
    cv2.setMouseCallback("IMAGE",mousePoints)
    cv2.waitKey(1)



