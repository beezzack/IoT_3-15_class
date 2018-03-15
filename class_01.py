import RPi.GPIO as GPIO
import time

def Setup(GPIO2, OUT_IN):
    GPIO.setmode(GPIO.BCM)

    if OUT_IN == "OUT":
        GPIO.setup(GPIO2, GPIO.OUT)
    else:
        GPIO.setup(GPIO2, GPIO.IN)

def TurnOnLED(GPIO2):
    GPIO.output(GPIO2, True)

def TurnOffLED(GPIO2):
    GPIO.output(GPIO2, False)

def GetGPIOStatus(GPIO2):
    GPIO_State = GPIO.input(GPIO2)
    return GPIO_State

if _name_ == "main":
    try:
        Setup(2, "IN")
        print("The status of the GPIO{0} is {1}".format(2, GetGPIOStatus(2)))
        Setup(2, "OUT")
        while True:
            TurnOnLED(2)
            time.sleep(1)
            TurnOffLED(2)
            time.sleep(1)
        except KeyboardInterrpt:
            GPIO.cleanup()
