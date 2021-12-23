from adafruit_servokit import ServoKit

kit = ServoKit(channels=16)

def lightOn():
    kit.servo[1].angle = 180
    print("light on")

def lightOff():
    kit.servo[1].angle = 0
    print("light off")
