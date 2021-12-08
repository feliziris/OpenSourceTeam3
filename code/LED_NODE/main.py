from neopixel import NeoPixel
from machine import Pin
from socket import *
import json
import time
import network


led_light = {"up": [1, 5, 7], "down": [1, 3, 7], "right": [3, 5, 7], "left": [1, 3, 5],
             "STOP": [0, 1, 2, 3, 4, 5, 6, 7, 8]}
led = Pin(14, Pin.OUT)
OFF = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
SSID = "**"
PWD = "**"
LED_CNT = 9


def led_clear(pin, cnt):
    np = NeoPixel(pin, cnt)
    for i in range (0, cnt):
        np[i] = OFF

    np.write()


def led_on(pin, cnt, dir, color):
    np = NeoPixel(pin, cnt)
    for i in led_light[dir]:
        np[i] = color

    np.write()


def led_blink(count):
    built_LED = Pin(16, Pin.OUT)

    for i in range(count):
        built_LED.off()
        time.sleep(0.25)
        built_LED.on()
        time.sleep(0.25)


def wifi_connect():
    print("WiFi Connection Start")

    ssid = SSID
    password = PWD

    station = network.WLAN(network.STA_IF)

    if station.isconnected() is True:
        print("network config:", station.ifconfig())
        print("Already connected")
        return

    station.active(True)

    if not station.isconnected():
        print("Try to connect network")
        station.connect(ssid, password)
        while not station.isconnected():
            pass

    print("Connection successful")
    print("network config:", station.ifconfig())


wifi_connect()
led_blink(5)

sock = socket(AF_INET, SOCK_STREAM)
sock.bind(('', 9999))
sock.listen(10)

while True:
    server_sock, addr = sock.accept()

    rawData = server_sock.recv(1024).decode()
    jsonData = json.loads(rawData)

    print(jsonData)

    direction = jsonData["direction"]
    if direction is None:
        direction = "STOP"
        led_on(led, LED_CNT, direction, RED)
        time.sleep(3)

        led_clear(led, LED_CNT)
        continue

    for i in range(5):
        led_clear(led, LED_CNT)
        time.sleep(1.5)
        led_on(led, LED_CNT, direction, GREEN)
        time.sleep(3)

    led_clear(led, LED_CNT)
