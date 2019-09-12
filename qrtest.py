#!/usr/bin/python

from Adafruit_Thermal import *

printer = Adafruit_Thermal("/dev/serial0", 19200, timeout=5)

# Test character double-height on & off
printer.doubleHeightOn()
printer.println("Double Height ON HELLO THIS IS A QR TEST")
printer.doubleHeightOff()


import qrPY as qr
print(str(qr.width))
print(str(qr.height))
#print(str(qr.data))
printer.printBitmap(qr.width, qr.height, qr.data)
printer.feed(4)

printer.sleep()      # Tell printer to sleep
printer.wake()       # Call wake() before printing again, even if reset
printer.setDefault() # Restore printer to defaults
