import RPi.GPIO as GPIO
from gpiozero import LED
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(11,GPIO.OUT)
GPIO.setup(36,GPIO.OUT)

GPIO.output(36,True)

servo1=GPIO.PWM(11,40)
servo1.start(0)
print("Waiting for 2 seconds")
time.sleep(2)

print('Welcome')

servo1.ChangeDutyCycle(7)
time.sleep(2)


servo1.ChangeDutyCycle(2)
time.sleep(0.5)
servo1.ChangeDutyCycle(0)



servo1.stop()
GPIO.cleanup()
print('Goodbye')

#red.off()
