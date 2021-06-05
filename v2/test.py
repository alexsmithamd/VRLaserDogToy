import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.board)

controlpin = [7,11,13,15]

for pin in controlpin:
    GPIO.setup(pin, GPIO.OUT)

hs_sequence = [
        [1, 0, 0, 0],
        [1, 1, 0, 0],
        [0, 1, 0, 0],
        [0, 1, 1, 0],
        [0, 0, 1, 0],
        [0, 0, 1, 1],
        [0, 0, 0, 1],
        [1, 0, 0, 1] ]

for i in range(512):
    for hs in range(8):
        for pin in range(4):
            GPIO.output(controlpin[pin], hs_sequence[hs][pin])
        time.sleep(0.001)

GPIO.cleanup()