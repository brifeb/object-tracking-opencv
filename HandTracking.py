import cv2
import pyfirmata
from cvzone.HandTrackingModule import HandDetector
import numpy as np

cap = cv2.VideoCapture(0)

# Set size screen
ws, hs = 1280, 800
cap.set(3, ws)
cap.set(4, hs)

if not cap.isOpened():
    print("Camera couldn't Access")
    exit()

detector = HandDetector(detectionCon=0.7)

port = "/dev/tty.usbmodem14101"
# port = "/dev/tty.Bluetooth-Incoming-Port"

board = pyfirmata.Arduino(port)
servo_pinX = board.get_pin('d:9:s')  # pin 9 Arduino
servo_pinY = board.get_pin('d:10:s')  # pin 10 Arduino

q_pressed = False
while (not q_pressed):
    success, img = cap.read()
    img = cv2.flip(img, 1)
    hands, img = detector.findHands(img, draw=True, flipType=False)

    if hands:
        hand1 = hands[0]  # Get the first hand detected
        lmList1 = hand1["lmList"]  # List of 21 landmarks for the first hand

        fx, fy = lmList1[9][0], lmList1[9][1]
        posFinger = [fx, fy]
        # convert coordinat to servo degree
        servoX = np.interp(fx, [0, ws], [0, 180])
        servoY = np.interp(fy, [0, hs], [90, 0])

        cv2.circle(img, (fx-20, fy+50), 15, (0, 0, 255), cv2.FILLED)  # draw circle on center of hand
        cv2.putText(img, str(posFinger), (fx+10, fy+40), cv2.FONT_HERSHEY_PLAIN, 1, (0, 0, 255), 2)
        
        cv2.line(img, (0, fy+50), (ws, fy+50), (0, 0, 0), 2)  # x line
        cv2.line(img, (fx-20, hs), (fx-20, 0), (0, 0, 0), 2)  # y line

        cv2.putText(img, f'Servo X: {int(servoX)} deg', (50, 50), cv2.FONT_HERSHEY_DUPLEX, 1, (255, 0, 0), 2)
        cv2.putText(img, f'Servo Y: {int(servoY)} deg', (50, 100), cv2.FONT_HERSHEY_DUPLEX, 1, (255, 0, 0), 2)

        servo_pinX.write(servoX)
        servo_pinY.write(servoY)

    cv2.imshow("Camera", img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        q_pressed = True
        break
