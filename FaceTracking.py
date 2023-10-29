import cv2
from cvzone.FaceDetectionModule import FaceDetector
import pyfirmata
import numpy as np

cap = cv2.VideoCapture(0)
ws, hs = 1280, 720
cap.set(3, ws)
cap.set(4, hs)

if not cap.isOpened():
    print("Camera couldn't Access!!!")
    exit()

# edit serial port here
# port = "COM3"
port = "/dev/tty.usbmodem14101"

board = pyfirmata.Arduino(port)
servo_pinX = board.get_pin('d:9:s') #pin 9 Arduino
servo_pinY = board.get_pin('d:10:s') #pin 10 Arduino
servoX = 90 #initial position
servoY = 45

detector = FaceDetector()

q_pressed = False
while (not q_pressed):
    success, img = cap.read()
    img = cv2.flip(img, 1) # flip camera
    img, bboxs = detector.findFaces(img, draw=False)

    if bboxs:
        #get the coordinate
        fx, fy = bboxs[0]["center"][0], bboxs[0]["center"][1]
        pos = [fx, fy]

        #convert coordinat to servo degree
        servoX = np.interp(fx, [0, ws], [0, 180])
        servoY = np.interp(fy, [0, hs], [90, 0])

        cv2.circle(img, (fx, fy), 80, (0, 0, 255), 2)
        cv2.putText(img, str(pos), (fx+15, fy-15), cv2.FONT_HERSHEY_PLAIN, 1, (255, 0, 0), 2 )
        cv2.line(img, (0, fy), (ws, fy), (0, 0, 0), 2)  # x line
        cv2.line(img, (fx, hs), (fx, 0), (0, 0, 0), 2)  # y line
        cv2.circle(img, (fx, fy), 15, (0, 0, 255), cv2.FILLED)

    cv2.putText(img, f'Servo X: {int(servoX)} deg', (50, 50), cv2.FONT_HERSHEY_PLAIN, 2, (255, 0, 0), 2)
    cv2.putText(img, f'Servo Y: {int(servoY)} deg', (50, 100), cv2.FONT_HERSHEY_PLAIN, 2, (255, 0, 0), 2)

    servo_pinX.write(servoX)
    servo_pinY.write(servoY)

    # img = cv2.flip(img, 1)
    cv2.imshow("Camera", img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        q_pressed = True
        break
