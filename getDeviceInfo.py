#!/usr/bin/python

import serial
import time

sensor = serial.Serial("/dev/ttyS0", baudrate = 9600, timeout = 0.5)
sensor.flushInput()

time.sleep(1)

sensor.flushInput()

# Get Vendor Name
sensor.write("\x68\x2B\x0E\x04\x00\x2F\x2E")
time.sleep(.5)

response = sensor.read(23)
print(response)

# Get Product Code
sensor.write("\x68\x2B\x0E\x04\x01\xEE\xEE")
time.sleep(.5)

response = sensor.read(26)
print(response)
