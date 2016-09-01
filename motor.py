def wait( sec):

    while(sec>0):
        sec=sec-1;
        print ("count:",sec);

def forward():
        print ("Forward Started");
        
        gpio.output(5,False);
        gpio.output(6,True);
        gpio.output(13,True);
        gpio.output(19,True);
        print ("delay1");

        #wait(delay);
        gpio.output(5,True);
        gpio.output(6,True);
        gpio.output(13,False);
        gpio.output(19,True);       

        print ("delay2");
        #wait(delay);
        gpio.output(5,True);
        gpio.output(6,False);
        gpio.output(13,True);
        gpio.output(19,True);

        print ("delay3");

        #wait(delay);
        gpio.output(5,True);
        gpio.output(6,True);
        gpio.output(13,True);
        gpio.output(19,False);
        print ("delay4");
        #wait(delay);
        print ("End");

def reverse():
          #print ("time:",times);
        print ("Started");
        
        gpio.output(5,False);
        gpio.output(6,True);
        gpio.output(13,True);
        gpio.output(19,True);
        print ("delay1");

        #wait(delay);
        gpio.output(5,True);
        gpio.output(6,True);
        gpio.output(13,False);
        gpio.output(19,True);       

        print ("delay2");
        #wait(delay);
        gpio.output(5,True);
        gpio.output(6,False);
        gpio.output(13,True);
        gpio.output(19,True);

        print ("delay3");

        #wait(delay);
        gpio.output(5,True);
        gpio.output(6,True);
        gpio.output(13,True);
        gpio.output(19,False);
        print ("delay4");
        #wait(delay);
        print ("End");


#renaming the rpi struct
import RPi.GPIO as gpio;

#avoiding warnings
gpio.setwarnings(False);

#Set mode as BCM or Board
gpio.setmode(gpio.BCM);

#set the pin as in or out direction
gpio.setup(5,gpio.OUT);
gpio.setup(6,gpio.OUT);
gpio.setup(13,gpio.OUT);
gpio.setup(19,gpio.OUT);
#disable the pin
gpio.output(5,True);
gpio.output(6,True);
gpio.output(13,True);
gpio.output(19,True);

#delay=input("Enter delay:")
#print("delay:",delay,type(delay));
#for times in range(0,5):
c=1;        
while(1):
      if c>0 && c<=160:
         forward()
      elif c >160 && c<=320
         reverse()
c=c+1
print("count:",c)
 
        

        







        
