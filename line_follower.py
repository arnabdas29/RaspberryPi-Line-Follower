"""
Author : Arnab Das
"""

import RPi.GPIO as GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

#Setup lines
ir1 = 2; ir2 = 3  #IR Sensors pin
ma1=4; ma2=14; mb1=17; mb2=18  #Motor sensors pin
GPIO.setup(ir1,GPIO.IN) #GPIO 2 -> left IR
GPIO.setup(ir2,GPIO.IN) #GPIO 3 -> right IR

GPIO.setup(ma1,GPIO.OUT) #GPIO 4 -> Right Motor A
GPIO.setup(ma2,GPIO.OUT) #GPIO 14 -> Right Motor B

GPIO.setup(mb1,GPIO.OUT) #GPIO 17 -> Left Motor A
GPIO.setup(mb2,GPIO.OUT) #GPIO 18 -> Left Motor B

#Working lines
if GPIO.input(ir1) == True and GPIO.input(ir2) == True:   #straight
    GPIO.output(ma1, True)
    GPIO.output(ma2, False)
    GPIO.output(mb1, True)
    GPIO.output(mb2, False)

elif GPIO.input(ir1) == False and GPIO.input(ir2) == True:  #right
    GPIO.output(ma1, True)
    GPIO.output(ma2, True)
    GPIO.output(mb1, True)
    GPIO.output(mb2, False)
elif GPIO.input(ir1) == True and GPIO.input(ir2) == False:  #left
    GPIO.output(ma1, True)
    GPIO.output(ma2, False)
    GPIO.output(mb1, True)
    GPIO.output(mb2, True)
else: #stop
    GPIO.output(ma1, True)
    GPIO.output(ma2, True)
    GPIO.output(mb1, True)
    GPIO.output(mb2, True)