#!/usr/bin/env python3

from time import sleep
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.OUT)

try:
  for i in range(0,3):
    GPIO.output(17, GPIO.HIGH)
    GPIO.output(17, GPIO.LOW)
    sleep(2)
except KeyboardInterrupt:
  GPIO.cleanup()
