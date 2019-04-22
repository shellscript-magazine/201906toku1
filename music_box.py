#!/usr/bin/env python3

from time import sleep
import RPi.GPIO as GPIO
import sys

GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.OUT)

for _ in range(args):
  GPIO.output(17, GPIO.HIGH)
  sleep(0.01)
  GPIO.output(17, GPIO.LOW)
  sleep(0.05)
GPIO.cleanup()
