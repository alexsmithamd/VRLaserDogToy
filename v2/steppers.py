import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

ControlPins = [7,11,13,15]

for pin in ControlPins:
    GPIO.setup(pin, GPIO.out)
    GPIO.output(pin, 0)


# half step sequence

hs_sequence = [ [1,0,0,0],
                [1,1,0,0],
                [0,1,0,0],
                [0,1,1,0],
                [0,0,1,0],
                [0,0,1,1],
                [0,0,0,1],
                [1,0,0,1] ]


for i in range(512):
        # goes through hs_sequence
        for halfstep in range(8):
            for pin in range(4):
                # set pin
                GPIO.output( ControlPins[pin], hs_sequence[halfstep][pin] )
            time.sleep(0.001)
            