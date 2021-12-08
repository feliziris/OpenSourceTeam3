from machine import Pin
from socket import *
import time
import json
import machine
import network

detector = Pin(14, Pin.IN)
detector_loc = (0, 2)
SSID = "**"
PWD = "**"
SERVER_IP = "**"
SERVER_PORT = 9999


def led_blink(count):
    built_LED = Pin(16, Pin.OUT)

    for i in range(count):
        built_LED.off()
        time.sleep(0.25)
        built_LED.on()
        time.sleep(0.25)


def wifi_connect():
    print("WiFi Connection Start")

    # WiFi Connection Information
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


def get_value(sensor):
    return sensor.value()


def set_data(id, location, detect):
    dictData = {"id": id, "location": location, "detect": detect}
    return json.dumps(dictData)


wifi_connect()
led_blink(5)

server_ip = SERVER_IP
sever_port = SERVER_PORT
clientSock = socket(AF_INET, SOCK_STREAM)
clientSock.connect((server_ip, sever_port))

detect_count = 0

while True:
    sensor_val = get_value(detector)

    if sensor_val > 0:
        led_blink(1)
        jsonData = set_data(0, detector_loc, sensor_val)
        clientSock.send(jsonData.encode())
        machine.soft_reset()

    time.sleep(1)
