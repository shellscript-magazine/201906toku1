#!/usr/bin/env python3

import smbus2
import bme280
i2c = smbus2.SMBus(1)

data = bme280.sample(i2c, 0x76)
print('気温 :' + str(round(data.temperature, 1)) + '度')
print('湿度 :' + str(round(data.humidity, 1)) + '％')
print('気圧 :' + str(round(data.pressure, 1)) + 'hPa')
