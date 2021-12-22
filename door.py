from adafruit_servokit import ServoKit

kit = ServoKit(channels=16)

def doorOpen():
    kit.servo[0].angle = 180
    print("door opened")

def doorClose():
    kit.servo[0].angle = 0
    print("door closed")