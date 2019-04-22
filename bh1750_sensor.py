#!/usr/bin/env python3

import smbus2
from i2csense.bh1750 import BH1750

bus = smbus2.SMBus(1)
sensor = BH1750(bus)

sensor.update()
print(sensor.light_level)
print(sensor.current_state_str)
