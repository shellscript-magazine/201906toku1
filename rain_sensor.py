#!/usr/bin/env python3

import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.IN)

try:
  while True:
    rain = GPIO.input(17)
    if rain == 0:
      print("雨が降り始めました")
      GPIO.cleanup()
      break
except KeyboardInterrupt:
  GPIO.cleanup()