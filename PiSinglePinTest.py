#!/usr/bin/python
"""
Raspberry Pi Pin Test
"""
 
import time
import datetime
import RPi.GPIO as GPIO

# Define Variables
delay = 2.0
checkPin=36

def testPinState(pin, expected):
    pinTest = True # Assume no faults
    if GPIO.input(pin):
        print("  Pin " + str(pin) + " is high")
        if expected == 0:
            pinTest = False
    else:
        print("  Pin " + str(pin) + " is low")
        if expected == 1:
            pinTest = False
              
    if not(pinTest):
        print("  ** Fault **")
    return pinTest

def pinCheck(pin):
    func  = GPIO.gpio_function(pin)
    status = False # Assume pin can't be used
    if func == GPIO.IN:
        result = "Input"
        status = True
    elif func == GPIO.OUT:
        result = "Output"
        status = True
    elif func == GPIO.SPI:
        result = "SPI"
    elif func == GPIO.I2C:
        result = "I2C"
    elif func == GPIO.HARD_PWM:
        result = "PWM"
    elif func == GPIO.SERIAL:
        result = "Serial"
    elif func == GPIO.OUT:
        result = "Unknown"
    else:
        result = "Undefined!"
    print("Pin " + str(pin) + " is defined as: " + result)
    return status

def pinSingleTest(pin):
    resultTest = True # Assume no faults
    if (pin == 3) or (pin == 5):
        skipPullUpDown = True # I2C channel has physical pull-up resistors
    else:
        skipPullUpDown = False
        
    pinStatus = True # Assume pin is OK to test
    if not(pinCheck(pin)):
        pinStatus = False
        
    if pinStatus:
        if not(skipPullUpDown):
            GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

            print("Pin " + str(pin) + " pull-down")
            
            if not(testPinState(pin, 0)):
                resultTest = False
            time.sleep(delay)
        

            GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
            
            print("Pin " + str(pin) + " pull-up")
            
            if not(testPinState(pin, 1)):
                resultTest = False
            time.sleep(delay)
        
            GPIO.setup(pin, GPIO.IN)

        else:
            GPIO.setup(pin, GPIO.IN)

            print("Pin " + str(pin) + " pull-up (hardware resistor)")

            if not(testPinState(pin, 1)):
                resultTest = False
            time.sleep(delay)

        GPIO.setup(pin, GPIO.OUT)
        GPIO.output(pin, 0)

        print("Pin " + str(pin) + " out low")

        if not(testPinState(pin, 0)):
            resultTest = False
        time.sleep(delay)

        GPIO.output(pin, 1)
        
        print("Pin " + str(pin) + " out high")

        if not(testPinState(pin, 1)):
            resultTest = False
        time.sleep(delay)
                  
        GPIO.setup(pin, GPIO.IN)

    else:
        print("Unable to test pin " + str(pin))
        resultTest = False
    return resultTest
    

def pinTest():
    print("Start testing Pi Pin")
    print("====================")
    print("")
    GPIO.setmode(GPIO.BOARD)
    success = True # Assume no faults

    pinSingleTest(checkPin)

    GPIO.cleanup()
    print("")
    if success:
        print("All tests passed")
    else:
        print("!! Some tests failed !!")

    print("")
    print("==================")
    print("End testing Pi Pin")
    print("")



if __name__ == "__main__":
    pinTest()

     
