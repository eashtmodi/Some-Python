import cv2

def snapShot():
    videoCaptureObject=cv2.VideoCapture(0)
    result=True
    while(result):
        ret,frame=videoCaptureObject.read()
        cv2.imwrite("pic1.jpg",frame)
        result=False
    videoCaptureObject.release()
    cv2.destroyAllWindows()

snapShot()
input("Enter To Exit!")
