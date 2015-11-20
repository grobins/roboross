import RPi.GPIO as GPIO ## Import GPIO Library
import time ## Import 'time' library.  Allows us to use 'sleep'

GPIO.setmode(GPIO.BOARD) ## Use BOARD pin numbering
GPIO.setup(15, GPIO.OUT) ## Setup GPIO pin 7 to OUT
GPIO.setup(19, GPIO.OUT)
GPIO.setup(21, GPIO.OUT)
GPIO.setup(23, GPIO.OUT)

## Define function named Blink()
def Blink(numTimes, speed):
    for i in range(0,numTimes): ## Run loop numTimes
        print "Iteration " + str(i+1) ##Print current loop
        GPIO.output(23, False)  
        GPIO.output(15, True) ## Turn on GPIO pin 7
        time.sleep(speed) ## Wait
        GPIO.output(15, False)        
        GPIO.output(19, True)
        time.sleep(speed) ## Wait
        GPIO.output(19, False)        
        GPIO.output(21, True)
        time.sleep(speed) ## Wait
        GPIO.output(21, False)        
        GPIO.output(23, True)
        time.sleep(speed) ## Wait
        GPIO.output(23, False)        
        print "Done" ## When loop is complete, print "Done"
        GPIO.cleanup()

## Prompt user for input
numTimes = raw_input("Enter the total number of times to blink: ")
speed = raw_input("Enter the length of each blink in seconds: ")

## Start Blink() function. Convert user input from strings to numeric data types and pass to Blink() as parameters
Blink(int(iterations),float(speed))
