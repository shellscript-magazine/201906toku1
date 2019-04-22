#!/usr/bin/env python3

import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(27, GPIO.OUT)
GPIO.setup(17, GPIO.IN)

GPIO.output(27, GPIO.LOW)
time.sleep(0.3)
GPIO.output(27, GPIO.HIGH)
time.sleep(0.00001)
GPIO.output(27, GPIO.LOW)

try:
  while GPIO.input(17) == 0:
    palse_start = time.time()
  while GPIO.input(17) == 1:
    palse_end = time.time()
  palse_width_time = palse_end - palse_start
  distance = palse_width_time * 1000000 / 58
  print("距離は {0} cmです".format(distance))
  GPIO.cleanup()
except KeyboardInterrupt:
  GPIO.cleanup()
