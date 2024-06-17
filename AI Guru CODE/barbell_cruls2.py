import cv2
import numpy as np
from test2 import poseDetector

cap = None  # Initialize cap properly
detector = poseDetector()
count = 0
rep_up = 0
pTime = 0
per = 0

def init(a):
    global cap, detector, count
    if a:
        print("Turning on camera")
        cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
    else:
        print("Turning off camera")
        if cap:
            cap.release()
        count = 0

def run(x, y, z):
    global count, rep_up, pTime, detector, cap, per

    success, img = cap.read()
    if success:
        img = cv2.resize(img, (1280, 720))
        img = cv2.flip(img, 1)
        img = detector.findPose(img)
        lmList = detector.findPosition(img)

        if lmList:
            if z == 1:
                # Right arm
                angle = detector.findAngle(img, 11, 13, 15)
                per = np.interp(angle, (220, 300), (0, 100))
                bar = np.interp(angle, (220, 300), (650, 100))
            elif z == 0:
                # Left arm
                angle = detector.findAngle(img, 12, 14, 16)
                per = np.interp(angle, (30, 120), (100, 0))
                bar = np.interp(angle, (30, 120), (100, 650))
            elif z == 2:
                # Abs
                angle = detector.findAngle(img, 11, 23, 25)
                per = np.interp(angle, (190, 240), (0, 100))
                bar = np.interp(angle, (190, 240), (650, 100))
            elif z == 3:
                # Squat
                angle = detector.findAngle(img, 24, 26, 28)
                per = np.interp(angle, (190, 260), (0, 100))
                bar = np.interp(angle, (190, 260), (650, 100))
            elif z == 4:
                # Pushup
                angle = detector.findAngle(img, 11, 13, 15)
                per = np.interp(angle, (260, 310), (0, 100))  # Adjust angle range for push-up
                bar = np.interp(angle, (260, 310), (650, 100))  # Adjust interpolation range for push-up

            # Check for rep
            color = (255, 0, 255)
            if per == 100:
                color = (255, 0, 255)
                if rep_up == 0:
                    count += 1
                    rep_up = 1
            if per == 0:
                color = (0, 255, 0)
                if rep_up == 1:
                    count += 1
                    rep_up = 0

            cv2.rectangle(img, (1100, 100), (1175, 650), (255, 255, 255), 3)
            cv2.rectangle(img, (1100, int(bar)), (1175, 650), (255, 0, 255), cv2.FILLED)
            cv2.putText(img, f'{int(per)}%', (1100, 75), cv2.FONT_HERSHEY_PLAIN, 4, color, 3)

        img = cv2.resize(img, (x, y))
        return img, per, count
    else:
        return None, None, None  # Return None when img read fails
