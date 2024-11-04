import cv2
import numpy as np

cap=cv2.VideoCapture(0)

trainX=[]
trainY = ["spoiled", "good", "None"]

spoiled_banana="testModelBanana/spoiled.png"
good_banana="testModelBanana/good.png"
no_banana="testModelBanana/none.png"

def averagecolor(image):
    # return np.mean(image,axis=(0,1))
    return np.mean(image, axis=(0, 1))

avgSpoiled = averagecolor(spoiled_banana)
avgGood = averagecolor(good_banana)
avgNone = averagecolor(no_banana)

trainX.append(avgSpoiled)
trainX.append(avgGood)
trainX.append(avgNone)


while True:
    _,frame=cap.read()
    img_hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    hue_min = 10
    hue_max = 27
    sat_min = 90
    sat_max = 255
    min_val = 47
    max_val = 255

    lower = np.array([hue_min, sat_min, min_val])
    upper = np.array([hue_max, sat_max, max_val])
    masked_img = cv2.inRange(img_hsv, lower, upper)
    final_img = cv2.bitwise_and(frame, frame, mask=masked_img)

    liveAverage=averagecolor(final_img)

    calculated_distances = []
    for card in (trainX):
        calculated_distances.append(np.linalg.norm(liveAverage - card))

    print(trainY[np.argmin(calculated_distances)])

    print(calculated_distances)

    cv2.imshow("HSV", img_hsv)
    cv2.imshow("mask", masked_img)
    cv2.imshow("final", final_img)
    cv2.imshow("Camera",frame)
    if cv2.waitKey(1) & 0XFF==ord(" "):
        break