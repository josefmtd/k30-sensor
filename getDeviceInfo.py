#!/usr/bin/python

import serial
import time

sensor = serial.Serial("/dev/ttyS0", baudrate = 9600, timeout = 0.5)
sensor.flushInput()

time.sleep(1)

sensor.flushInput()
sensor.write("\xFE\x2B\x0E\x04\x01\xA6\xF3")
time.sleep(.5)

response = sensor.read(26)
print(response)
