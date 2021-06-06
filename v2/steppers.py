import sys
import curses   # curses keyboards or some other lib ??? -> pygame is kinda slows
import os
import time
import pygame
import RPi.GPIO as GPIO

GPIO.setwarnings(False)
GPIO.cleanup()
GPIO.setmode(GPIO.BOARD) #1-40

# curses lib setup
screen = curses.initscr()
curses.noecho()
curses.cbreak()
screen.keypad(True)


# define variables & pins
delay = .001  # delay between each sequence step to prevent jitter

#------------------------------------------------------

# Laser stuff  

GPIO.setup(8, GPIO.OUT)
class Laser:
        def __init__(self, status):
            self.status = status
            
        def toggle_laser(self):      
                if self.status == True:
                        self.status = False
                        print("Status changed to False")
                elif self.status == False:
                        self.status = True
                        print("Status changed to True")
                GPIO.output(8, self.status)

class Axis:
        # half step sequence -> should put inside class ???
        hs_sequence = [
        [1, 0, 0, 0],
        [1, 1, 0, 0],
        [0, 1, 0, 0],
        [0, 1, 1, 0],
        [0, 0, 1, 0],
        [0, 0, 1, 1],
        [0, 0, 0, 1],
        [1, 0, 0, 1] ]

        def __init__(self, position_index, pin1, pin2, pin3, pin4):
                self.position_index = position_index
                self.position = self.hs_sequence[self.position_index]
                self.pins = [pin1, pin2, pin3, pin4]

                for pin in self.pins:
                        print("Pin: " + str(pin))
                        GPIO.setup(pin, GPIO.OUT)

                self.set_pins(self.pins, self.position)

        def set_pins(self, pins_arr, position_arr):
                for i in range(4):
                        GPIO.output(pins_arr[i], position_arr[i])
                time.sleep(delay)

        def positive_spin(self):
                print("Old position:")
                print(self.position)
                
                for i in range(30):
                        if self.position_index == 7:
                                self.position_index = 0
                        else:
                                self.position_index += 1
                        self.position = self.hs_sequence[self.position_index]
                        # set new pins
                        self.set_pins(self.pins, self.position)
                
                print("New position:") 
                print(self.position)


        def negative_spin(self):
                print("Old position: ")
                print(self.position)
                
                for i in range(30):
                        if self.position_index == 0:
                                self.position_index = 7
                        else:
                                self.position_index -= 1
                        self.position = self.hs_sequence[self.position_index]
                        # set new pins
                        self.set_pins(self.pins, self.position)

                print("New position: ")
                print(self.position)
#-----------------------------------------------------

# define axis
yaw = Axis(0, 12, 16, 18, 22)  # Y.2 : will stay still until we need it later
pitch = Axis(0, 29, 31, 33, 35)   
roll = Axis(0, 7, 11, 13, 15)   
pitch = Axis(0, 32, 36, 38, 40)  

laser = Laser(False)

print("Initial status")
print(laser.status)
#------------------------------------------------------

# Start main loop
try:
        while True:
                key_press = screen.getch()
                if key_press == ord('q'):
                        #if q is pressed quit
                        break
                if key_press == ord('l'):
                        #toggles laser on/off when l is pressed
                        print("Laser before")
                        print(laser.status)
                        laser.toggle_laser()
                        print("Laser after")
                        print(laser.status)
                if key_press == ord('w'):
                        # pitch up
                        print("p+")
                        pitch.positive_spin()
                elif key_press == ord('s'):
                        # pitch down
                        print("p-")
                        pitch.negative_spin()

                if key_press == ord('a'):
                        # yaw left
                        print("y-")
                        yaw.negative_spin()
                elif key_press == ord('d'):
                        # yaw right
                        print("y+")
                        yaw.positive_spin()
                if key_press == ord('j'):
                        # roll left
                        print("r-")
                        roll.negative_spin()
                elif key_press == ord('k'):
                        # roll right
                        print("r+")
                        roll.positive_spin()
                if key_press == ord('g'):
                        # height down
                        print("h-")
                        height.negative_spin()
                elif key_press == ord('h'):
                        # height up
                        print("h+")
                        height.positive_spin()
finally:
    # shut down cleanly
    curses.nocbreak(); screen.keypad(0); curses.echo()
    curses.endwin()

GPIO.cleanup()
