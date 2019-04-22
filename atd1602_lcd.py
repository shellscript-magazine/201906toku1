#!/usr/bin/env python3

from lcd_st7032 import ST7032

lcd = ST7032()
lcd.write("Shellscript")
lcd.setCursor(1, 0)
lcd.write([0xbc, 0xaa, 0xd9, 0xbd, 0xb8, 0xd8, 0xcc, 0xdf, 0xc4])
