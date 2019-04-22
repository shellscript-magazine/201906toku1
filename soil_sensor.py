#!/usr/bin/env python3

import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.IN)

try:
  while True:
    rain = GPIO.input(17)
    if rain == 1:
      print("水分量が足りません")
      GPIO.cleanup()
      break
except KeyboardInterrupt:
  GPIO.cleanup()
