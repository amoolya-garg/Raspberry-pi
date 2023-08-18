import network
import time
from math import sin
from umqtt.simple import MQTTClient
from machine import Pin

# Fill in your WiFi network name (ssid) and password here:
wifi_ssid = "70906"
wifi_password = "0003062001"

# Connect to WiFi
wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(wifi_ssid, wifi_password)
while wlan.isconnected() == False:
    print('Waiting for connection...')
    time.sleep(1)
print("Connected to WiFi")

led = Pin("LED",Pin.OUT)
mqtt_host = "io.adafruit.com"
mqtt_username = "amoolya2001"  # Your Adafruit IO username
mqtt_password = "aio_vWfY52KC3EmdYQTKZGrMxSW4XleG"  # Adafruit IO Key
mqtt_publish_topic = "amoolya2001/feeds/pico-test"  # The MQTT topic for your Adafruit IO Feed

mqtt_client_id = "AmoolyaGarg2001abc"

mqtt_client = MQTTClient(
        client_id=mqtt_client_id,
        server=mqtt_host,
        user=mqtt_username,
        password=mqtt_password)

mqtt_client.connect()

counter = 0
try:
    while True:
        # Generate some dummy data that changes every loop
        sine = sin(counter)
        counter += .8
        
        # Publish the data to the topic!
        print(f'Publish {sine:.2f}')
        mqtt_client.publish(str(mqtt_publish_topic), str(sine))
        led.toggle()
        
        # Delay a bit to avoid hitting the rate limit
        time.sleep(3)
except Exception as e:
    print(f'Failed to publish message: {e}')
finally:
    mqtt_client.disconnect()