import math
import cv2
import time
from matplotlib.pyplot import get
import mediapipe as mp
import math
landMarkArray={}

mpDraw=mp.solutions.drawing_utils
mpPose=mp.solutions.pose
pose=mpPose.Pose()

pTime=0
cap= cv2.VideoCapture(0)

tracing=False
def bicepCurl(a,traced):
    rightElbow=a.get('14')
    leftElbow=a.get('13')
    rightWrist=a.get('16')
    leftWrist=a.get('15')
    rightShoulder=a.get('12')
    leftShoulder=a.get('11')
    if traced:
        rightBicepAngle=calculateAngle(rightShoulder,rightWrist,rightElbow)
        if rightBicepAngle<0:
            rightBicepAngle=rightBicepAngle*-1
        else:
            pass
        cv2.ellipse(img, rightElbow, (50,50), 360, 0, rightBicepAngle-90, (0,0,255),  10)
        leftBicepAngle=calculateAngle(leftShoulder,leftWrist,leftElbow)
        if leftBicepAngle<0:
            leftBicepAngle=leftBicepAngle*-1
        else:
            pass
        cv2.ellipse(img, leftElbow, (50,50), leftBicepAngle, 360, leftBicepAngle, (0,0,255),  10)

        print(rightBicepAngle,leftBicepAngle)
    # print(rightElbow)

def calculateAngle(a,b,c):
    x1=a[0]
    y1=a[1]
    x2=b[0]
    y2=b[1]
    x3=c[0]
    y3=c[1]
    # print(x1,y1)
    angle=math.degrees(math.atan2(y3-y2,x3-x2)-math.atan2(y1-y2,x1-x2))
    return angle


while True:
    success,img=cap.read()
    imgRGB=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    results=pose.process(imgRGB)
    if results.pose_landmarks:
        mpDraw.draw_landmarks(img,results.pose_landmarks,mpPose.POSE_CONNECTIONS)
        for id,lm in enumerate(results.pose_landmarks.landmark):
            # print(id,lm)
            h,w,c=img.shape
            cx,cy=int(lm.x*w),int(lm.y*h)
            cv2.circle(img,(cx,cy),5,(0,0,255),15)
            landMarkArray.update({str(id):[cx,cy]})
            # print(landMarkArray)
            if not landMarkArray:
                tracing=False
            else:
                tracing=True


    bicepCurl(landMarkArray,tracing)
    cTime=time.time()
    fps=1/(cTime-pTime)
    pTime=cTime
    cv2.putText(img,str(int(fps)),(70,140),cv2.FONT_HERSHEY_COMPLEX,5,(255,0,255),3)

    cv2.imshow('vid1',img)

    

    cv2.waitKey(1)

