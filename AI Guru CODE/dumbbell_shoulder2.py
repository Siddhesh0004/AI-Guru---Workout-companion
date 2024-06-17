import cv2
import time
import test2 as pr
import numpy as np

cap = None  # Initialize cap variable to None

detector = pr.poseDetector()

count = 0
rep_up = 0

def init(a):
    global cap, detector, count
    if a:
        print("Cam ON")
        cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
        # Initialize the pose detector
        #detector = pr.poseDetector()
    else:
        print("Cam OFF")
        if cap is not None:
            cap.release()  # Release the video capture
        cap = None
        count = 0

def run(x, y):
    global cap, detector, count, rep_up
    if cap is None:
        print("Error: Camera not initialized!")
        return

    success, image = cap.read()
    if not success:
        print("Error: Failed to read frame from the camera!")
        return

    image = cv2.resize(image, (1280, 720))
    image = cv2.flip(image, 2)
    image = detector.findPose(image, False)
    lmList = detector.findPosition(image)
    wrist = []

    if len(lmList) != 0:
        arm_r = detector.findAngle(image, 12, 14, 16)
        arm_l = detector.findAngle(image, 11, 13, 15)
        upbody_r = detector.findAngle(image, 24, 12, 14)
        upbody_l = detector.findAngle(image, 23, 11, 13)
        per_l = np.interp(upbody_l, (235, 270), (100, 0))
        per_r = np.interp(upbody_r, (95, 124), (0, 100))
        
        if lmList[11][2] > lmList[14][2]:  
            wrist.append([lmList[14][1], lmList[14][2] - detector.length(image, lmList[14][:2], lmList[16][:2])])
            wrist.append([lmList[13][1], lmList[13][2] - detector.length(image, lmList[14][:2], lmList[16][:2])])
            angle_r = detector.cosin2goc(image, wrist[0], lmList[14][:2], lmList[16][:2])
            angle_l = detector.cosin2goc(image, wrist[1], lmList[13][:2], lmList[15][:2])

        if (per_l == 100 and per_r == 100):
            color = (255, 0, 255)
            if rep_up == 0:
                count += 1
                rep_up = 1
        else:
            rep_up = 0
        if (per_l == 0 and per_r == 0):
            color = (0, 255, 0)
            if rep_up == 1:
                count += 1
                rep_up = 0

        print(count)
        cv2.rectangle(image, (0, 450), (250, 720), (0, 255, 0), cv2.FILLED)
        cv2.putText(image, str(int(count)), (40, 670), cv2.FONT_HERSHEY_PLAIN, 10, (255, 0, 0), 13)

    image = cv2.resize(image, (x, y))

    return image, per_r, count

# Initialize the camera
init(True)

bTime = time.time()
while True:
    frame, per_r, count = run(640, 480)
    nTime = time.time()
    fps = 1 / (nTime - bTime)
    bTime = nTime
    cv2.putText(frame, f"FPS: {int(fps)}", (50, 70), cv2.FONT_HERSHEY_SIMPLEX, 3, (255, 0, 0), 3)
    cv2.imshow("show", frame)
    if cv2.waitKey(5) & 0xFF == ord("q"):
        break

# Release the camera and close all OpenCV windows
if cap is not None:
    cap.release()
cv2.destroyAllWindows()
