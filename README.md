# Object Tracking using OpenCV control 2 dof servo (pan & tilt)

## Python libs:
- opencv-python                4.8.1.78
- cvzone                       1.6.1
- pyFirmata                    1.1.0

## Arduino Libs:
- Firmata 2.5.9

## Installation:
### Arduino:
- download Firmata lib
- open File -> Examples -> Firmata -> StandartFirmata
- upload to Arduino

### Python
```bash
pip install -r requirements.txt
```

## RUN
(you may edit the serial port on the code)
### Tracking Face run: python FaceTracking.py
### Tracking Hand run: python HandTracking.py
Controlling 2DOF Servo via WiFi (local) with HTML Webpage slider


![alt text](https://github.com//brifeb/2DOF-Servo-WiFi-Control/blob/master/img/servo-control-page.png?raw=true)

# Skecth

![alt text](https://github.com//brifeb/2DOF-Servo-WiFi-Control/blob/master/img/sketch-wemos-servo.png?raw=true)

Connect servo signal to pin D6 and pin D8