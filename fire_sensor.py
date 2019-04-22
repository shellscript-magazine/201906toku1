#!/usr/bin/env python3

import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.IN)

try:
  while True:
    fire = GPIO.input(17)
    if fire == 0:
      print("火災が発生しました")
      GPIO.cleanup()
      break
except KeyboardInterrupt:
  GPIO.cleanup()
