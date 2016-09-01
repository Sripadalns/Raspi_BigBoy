def md_l293d(duty):
    import RPi.GPIO as GPIO
    import time
    from PWM import set_pwm
    
    # Select Raspi pin settings
    GPIO.setmode(GPIO.BOARD)

    # Suppress Warnings
    GPIO.setwarnings(False)

    # Define Pin Functions

    # Motor Left will have 2 pins i.e. Pin 38 and Pin 40
    LeftMotor_up = 38
    LeftMotor_down = 40


    # Motor right will have 2 pins i.e. Pin 32 and Pin 36
    RightMotor_up = 32
    RightMotor_down = 36


    # Set the proper GPIOS
    GPIO.setup(LeftMotor_up,GPIO.OUT)
    GPIO.setup(LeftMotor_down,GPIO.OUT)
    GPIO.setup(RightMotor_up,GPIO.OUT)
    GPIO.setup(RightMotor_down,GPIO.OUT)

    # Set the port pins for Motor
    GPIO.output(LeftMotor_up,1)
    GPIO.output(LeftMotor_down,0)    
    GPIO.output(RightMotor_up,1)
    GPIO.output(RightMotor_down,0)

    set_pwm(duty)

