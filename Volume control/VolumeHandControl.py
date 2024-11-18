import cv2
import numpy as np
import time
import HandTrackingModule as htm
import math
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
##############################################
wCam, hCam = 640, 480
##############################################
pink = (255,0,255)
blue = (255,0,0)
cap = cv2.VideoCapture(0)
cap.set(3,wCam)
cap.set(4,hCam)
pTime = 0

detector = htm.handDetector(detectionCon=0.7)


devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(
    IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = interface.QueryInterface(IAudioEndpointVolume)
# volume.GetMute()
# volume.GetMasterVolumeLevel()
volRange = volume.GetVolumeRange()
minVol = -65
maxVol = 0
# volume.SetMasterVolumeLevel(-65, None)
volBar = 400
vol = 0
volPer = 0
while True:
    success, img = cap.read()
    img = detector.findHands(img)
    lmList = detector.findPosition(img, draw=False)
    if len(lmList) != 0:
        # print(lmList[4], lmList[8])
        
        x1,y1 = lmList[4][1], lmList[4][2]
        x2,y2 = lmList[8][1], lmList[8][2]
        cx,cy = int((x1+x2)/2), int((y1+y2)/2)
        
        cv2.circle(img, (x1,y1), 15, pink,cv2.FILLED)
        cv2.circle(img, (x2,y2), 15, pink,cv2.FILLED)
        cv2.circle(img, (cx,cy), 15, pink,cv2.FILLED)
        cv2.line(img, (x1,y1), (x2,y2), pink,3)
        
        #Hand range :30,290
        #Vol range: -65,0
        length, img, lineInfo = detector.findDistance(4, 8, img)
        
        
        
        # length = math.sqrt(((x2-x1)**2)+((y2-y1)**2))
        vol = np.interp(length,[30,200],[minVol,maxVol])
        volBar = np.interp(length,[30,200],[400,150])
        smoothness = 10
        volPer = np.interp(length,[30,200],[0,100])
        volPer = smoothness * round(volPer / smoothness)
        # print("Length:",length)
        print('Volume:', vol)
        # volume.SetMasterVolumeLevel(vol, None)
        
        if length < 30:
            cv2.circle(img, (cx,cy), 15, (9,255,0), cv2.FILLED)
            
        #Set volume using fingers:
        fingers = detector.fingersUp()
        
        if not fingers[4]:
            volume.SetMasterVolumeLevelScalar(volPer / 100, None)
            cv2.circle(img, (lineInfo[4], lineInfo[5]), 15, (0, 255, 0), cv2.FILLED)
            colorVol = (0, 255, 0)
        else:
            colorVol = (255, 0, 0)
            
    cv2.rectangle(img, (50,150), (85,400),blue, 3)
    cv2.rectangle(img, (50,int(volBar)), (85,400),blue, cv2.FILLED)
    cv2.putText(img,f'{int(volPer)} %',(40,450),cv2.FONT_HERSHEY_COMPLEX_SMALL,1,blue, 3)
            
        

    
    

    
    cTime = time.time()
    fps = 1/(cTime-pTime)
    pTime = cTime
    
    cv2.putText(img,f'Fps: {int(fps)}',(40,70),cv2.FONT_HERSHEY_COMPLEX_SMALL,1,blue, 3)
    
    
    cv2.imshow("Img",img)
    cv2.waitKey(1)
    