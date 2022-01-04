

from gpiozero import LED
from time import sleep

red=LED(16)

red.on()
sleep(3)
red.off()

blue=LED(20)

blue.on()
sleep(3)
blue.off()

green=LED(21)

green.on()
sleep(3)
green.off()

