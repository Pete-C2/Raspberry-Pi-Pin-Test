#!/usr/bin/python
"""
Raspberry Pi Pin Test
"""
 
import time
import datetime
import RPi.GPIO as GPIO

# Define Variables
delay = 0.1
pins=[[3,5],[7,11],[13,15],[19,21],[23,29],[31,33],[35,37],[8,10],[12,16],[18,22],[24,26],[32,36],[38,40]]
# Each pair of pin numbers need to be shorted together to enable the tests to work

def testPinState(pin1, pin2, expected):
    pinTest = True # Assume no faults
    if GPIO.input(pin1):
        print("  Pin " + str(pin1) + " is high")
        if expected == 0:
            pinTest = False
    else:
        print("  Pin " + str(pin1) + " is low")
        if expected == 1:
            pinTest = False
              
    if GPIO.input(pin2):
        print("  Pin " + str(pin2) + " is high")
        if expected == 0:
            pinTest = False
    else:
        print("  Pin " + str(pin2) + " is low")
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

def pinPairTest(pin1, pin2):
    pairTest = True # Assume no faults
    if (pin1 == 3) or (pin1 == 5) or (pin2 == 3) or (pin2 == 5):
        skipPullUpDown = True # I2C channel has physical pull-up resistors
        pullUp = " (hardware resistors)"
    else:
        skipPullUpDown = False
        pullUp = ""
        
    pinStatus = True # Assume pins are OK to test
    if not(pinCheck(pin1)):
        pinStatus = False
    if not(pinCheck(pin2)):
        pinStatus = False
        
    if pinStatus:
        if not(skipPullUpDown):
            GPIO.setup(pin1, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
            GPIO.setup(pin2, GPIO.IN)

            print("Pin " + str(pin1) + " pull-down")
            
            if not(testPinState(pin1, pin2, 0)):
                pairTest = False
            time.sleep(delay)
        

            GPIO.setup(pin1, GPIO.IN, pull_up_down=GPIO.PUD_UP)
            
            print("Pin " + str(pin1) + " pull-up")
            
            if not(testPinState(pin1, pin2, 1)):
                pairTest = False
            time.sleep(delay)
        
            GPIO.setup(pin1, GPIO.IN)
            GPIO.setup(pin2, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

            print("Pin " + str(pin2) + " pull-down")
            
            if not(testPinState(pin1, pin2, 0)):
                pairTest = False
            time.sleep(delay)
        

            GPIO.setup(pin2, GPIO.IN, pull_up_down=GPIO.PUD_UP)
            
            print("Pin " + str(pin2) + " pull-up")
            
            if not(testPinState(pin1, pin2, 1)):
                pairTest = False
            time.sleep(delay)
        else:
            GPIO.setup(pin1, GPIO.IN)
            GPIO.setup(pin2, GPIO.IN)

            print("One or both pins " + str(pin1) + " & " + str(pin2) + " pull-up (hardware resistors)")

            if not(testPinState(pin1, pin2, 1)):
                pairTest = False
            time.sleep(delay)

        GPIO.setup(pin1, GPIO.OUT)
        GPIO.output(pin1, 0)

        print("Pin " + str(pin1) + " out low")

        if not(testPinState(pin1, pin2, 0)):
            pairTest = False
        time.sleep(delay)

        if not((pin2 == 3) or (pin2 == 5)):
            GPIO.setup(pin2, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        GPIO.output(pin1, 1)
        
        print("Pin " + str(pin1) + " out high")

        if not(testPinState(pin1, pin2, 1)):
            pairTest = False
        time.sleep(delay)
                  
        if not((pin1 == 3) or (pin1 == 5)):
            GPIO.setup(pin1, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.setup(pin2, GPIO.OUT)
        GPIO.output(pin2, 0)

        print("Pin " + str(pin2) + " out low")

        if not(testPinState(pin1, pin2, 0)):
            pairTest = False
        time.sleep(delay)

        if not((pin1 == 3) or (pin1 == 5)):
            GPIO.setup(pin1, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        GPIO.output(pin2, 1)
        
        print("Pin " + str(pin2) + " out high")

        if not(testPinState(pin1, pin2, 1)):
            pairTest = False
        time.sleep(delay)
        GPIO.setup(pin1, GPIO.IN)
        GPIO.setup(pin2, GPIO.IN)

    else:
        print("Unable to test pins " + str(pin1) + " & " + str(pin2))
        pairTest = False
    return pairTest
    

def pinTest():
    print("Start testing Pi Pins")
    print("=====================")
    print("")
    GPIO.setmode(GPIO.BOARD)
    success = True # Assume no faults

    for set in pins:
        if(not(pinPairTest(set[0], set[1]))):
            success = False
        print("---------------------")

    GPIO.cleanup()
    print("")
    if success:
        print("All tests passed")
    else:
        print("!! Some tests failed !!")

    print("")
    print("===================")
    print("End testing Pi Pins")
    print("")



if __name__ == "__main__":
    pinTest()

     
