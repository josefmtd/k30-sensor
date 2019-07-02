#!/usr/bin/python

import serial
import time

sensor = serial.Serial("/dev/ttyS0", baudrate = 9600, timeout = 0.5)
sensor.flushInput()

time.sleep(1)

for i in range(20):
    sensor.flushInput()
    sensor.write("\xFE\x04\x00\x03\x00\x01\xD5\xC5")
    time.sleep(.5)

    response = sensor.read(7)
    high = ord(response[3])
    low = ord(response[4])
    co2 = (high*256) + low
    print "CO2 = " + str(co2)
    time.sleep(.1)
