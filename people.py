import RPi.GPIO as GPIO
import time

def init():
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(12, GPIO.IN)
    GPIO.setup(11,GPIO.out)

def detct():
    for i in range(1,31):
        if GPIO.input(12) == True:
            print time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))+ "Someone is closing!"
        else:
            print time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))+"Noanybady!"
            time.sleep(6)

time.sleep(2)
init()
detct()
GPIO.cleanup()
