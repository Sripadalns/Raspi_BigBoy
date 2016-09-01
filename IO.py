import RPi.GPIO as GPIO
import time
from ultra import get_distance
from l293d import md_l293d
# Temporary variable
counter = 0
# Select Raspi pin settings
GPIO.setmode(GPIO.BOARD)

# Suppress Warnings
GPIO.setwarnings(False)

# Define Pin Functions

# Buzzer is output and Pin 11 will be used
Buzzer = 11

# IR sensor is Input  and Pin 29,31 and33
Leftsensor   =29
Rightsensor =31
Midsensor    =33



# Set the proper GPIOS
GPIO.setup(Buzzer,GPIO.OUT)
GPIO.setup(Leftsensor,GPIO.IN)
GPIO.setup(Rightsensor,GPIO.IN)
GPIO.setup(Midsensor,GPIO.IN)


while 1:
    # continuously loop here

    # If sensor is detecting black Then Turn On Ultra
    if (GPIO.input(Midsensor) == False):

         # Invoke the Ultrasound and get distance
         distance = get_distance()

         # Distance is more than 30 cm then move motor
         if distance > 500:
             print("run motor")
             md_l293d(80)
         else:
             if (distance > 100)and(distance<501):
                 md_l293d(50)
             else :
                 if (distance > 30)and(distance<101):
                     md_l293d(20)
                 else:
                     GPIO.output(Buzzer,True)
                     md_l293d(0)
    else:
        print("getout")


    
    
