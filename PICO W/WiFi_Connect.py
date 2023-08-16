import network
import socket
from time import sleep
from picozero import pico_temp_sensor,pico_led
import machine

ssid = "70906"
password = "0003062001"

def connect():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(ssid,password)
    while wlan.isconnected() == False:
            print("Waiting for connection...")
            sleep(1)
    print("Connection Successful")
    print(wlan.ifconfig())    
try:
    connect()
except KeyboardInterrupt:
        machine.reset()
        