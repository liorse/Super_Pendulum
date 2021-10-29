# A simple state machine which turns the blue LED on the pyboard on and off when the

# usr pushbutton on the pyboard is pressed.  Does not require any hardware except a

# micropython board.

 

from pyControl.utility import *

from devices import *

 

# Define hardware (normally done in seperate hardware definition file).

 

pyboard_button = Digital_input('X1', falling_event='object_in_beam', rising_event='object_out_beam')  # USR button on pyboard.

 

blue_LED = Digital_output('B4')

 

# States and events.

  

states= ['OBJECT_IN',

         'OBJECT_OUT']

 

events = ['object_in_beam', 'object_out_beam']

 

initial_state = 'OBJECT_OUT'

 

# Define behaviour.

 

def OBJECT_IN(event):

    if event == 'entry':

        blue_LED.on()

    elif event == 'exit':

        blue_LED.off()

    elif event == 'object_out_beam':

        goto_state('OBJECT_OUT')

 

def OBJECT_OUT(event):

    if event == 'object_in_beam':

        goto_state('OBJECT_IN')

 

def run_end():  # Turn off hardware at end of run.

    blue_LED.off()