import sys
import curses   # curses keyboards or some other lib ??? -> pygame is kinda slows
import os
import time
import pygame
import RPi.GPIO as GPIO

# 1-40, criss cross setup
GPIO.setmode(GPIO.BOARD)

# curses lib setup
screen = curses.initscr()
curses.noecho()
curses.cbreak()
screen.keypad(True)

# define variables & pins
delay = .001  # delay between each sequence step to prevent jitter





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

                if self.position_index == 7:
                        self.position_index = 0
                else:
                        self.position_index += 1
                self.position = self.hs_sequence[self.position_index]
                print("New position: " + self.position)

                # set new pins
                self.set_pins(self.pins, self.position)

        def negative_spin(self):
                print("Old position: ")
                print(self.position)
                
                if self.position_index == 0:
                        self.position_index = 7
                else:
                        self.position_index -= 1
                self.position = self.hs_sequence[self.position_index]
                print("New position: " + self.position)
                
                # set new pins
                self.set_pins(self.pins, self.position)

#-----------------------------------------------------

# define axis
yaw = Axis(0, 31, 33, 35, 37)   # X
pitch = Axis(0, 7, 11, 13, 15)   # Y
roll = Axis(0, 32, 36, 38, 40)  # Z

#------------------------------------------------------

# Start main loop
try:
        while True:
                key_press = screen.getch()
                if key_press == ord('q'):
                        #if q is pressed quit
                        break
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
                if key_press == curses.KEY_LEFT:
                        # roll left
                        print("r-")
                        roll.negative_spin()
                elif key_press == curses.KEY_RIGHT:
                        # roll right
                        print("r+")
                        roll.positive_spin()
finally:
    # shut down cleanly
    curses.nocbreak(); screen.keypad(0); curses.echo()
    curses.endwin()

GPIO.cleanup()
