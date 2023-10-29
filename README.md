# Object Tracking using OpenCV control 2 dof servo (pan & tilt)

## DEMO

YouTube shorts: <https://www.youtube.com/shorts/iiOM-0opG1Y>

## Skecth

![alt text](https://github.com//brifeb/object-tracking-opencv/blob/master/img/schema.jpeg?raw=true)

- servo 1 signal to pwm pin 9
- servo 2 signal to pwm pin 10

## Libraries

### Python libs

- opencv-python                4.8.1.78
- cvzone                       1.6.1
- pyFirmata                    1.1.0

### Arduino Libs

- Firmata 2.5.9

## Installation

### Arduino

- download Firmata lib
- open File -> Examples -> Firmata -> StandartFirmata
- upload to Arduino

### Python

```bash
pip install -r requirements.txt
```

## RUN

(you may edit the serial port on the code first)

### Tracking Face

```bash
python FaceTracking.py
```

### Tracking Hand

```bash
python HandTracking.py
```

***
brifeb@  <http://ndoware.com> 2023
