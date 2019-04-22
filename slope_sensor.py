#!/usr/bin/env python3

import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.IN)

try:
  while True:
    if GPIO.wait_for_edge(17, GPIO.FALLING):
      print("傾きました")
      GPIO.cleanup()
      break
except KeyboardInterrupt:
  GPIO.cleanup()
