#!/usr/bin/env python3

import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.IN)

try:
  while True:
    pir = GPIO.input(17)
    if pir == 1:
      print("人が侵入しました")
      GPIO.cleanup()
      break
except KeyboardInterrupt:
  GPIO.cleanup()
