def set_pwm(duty,cntr):
    
    import RPi.GPIO as GPIO
    import time
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(12,GPIO.OUT)
    pwm = GPIO.PWM(12,100)
    cntr = get_counter()
    cntr = get_counter()
    print("counter",cntr)
    if (cntr > 1 ):
        pwm.start(duty)
    else:
        pwm.ChangeDutyCycle(25)

