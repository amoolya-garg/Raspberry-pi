from machine import Pin,UART
import time

uart = UART(1,baudrate = 2400, tx = Pin(8), rx = Pin(9))
uart.init(bits = 8, parity = None,stop = 2)
led = Pin("LED", Pin.OUT)
while True:
    if uart.any():
        data = uart.read()
        print(data)
        led.toggle()
    time.sleep(1)