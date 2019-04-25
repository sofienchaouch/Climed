#!/usr/bin/python
# coding=utf-8
# "DATASHEET": http://cl.ly/ekot
# https://gist.github.com/kadamski/92653913a53baf9dd1a8
from __future__ import print_function
import serial, struct, sys, time, json
from Adafruit_BMP085 import BMP085
from firebase import firebase
import urllib2, urllib, httplib
from functools import partial
import numpy as np
import paho.mqtt.client as mqtt
from ubidots import ApiClient
import math
import time

#ubidots

# Create an ApiClient object
api = ApiClient(token="")
# Get a Ubidots Variable
variable_t = api.get_variable("5c9cc384c03f9728539dbcfc")
variable_p = api.get_variable("5c9cc3b4c03f9728539dbd1c")
variable_altitude = api.get_variable("5c9cc7cec03f972c92401c10")
variable_pm10 = api.get_variable("5c9cc7e6c03f972c92401c1a")
variable_pm25 = api.get_variable("5c9cc7ecc03f972c92401c21")



#ThinkBoard Config
iot_hub = "demo.thingsboard.io"
port = 1883
username = ""
password = ""
topic = "v1/devices/me/telemetry"
client = mqtt.Client()
client.username_pw_set(username,password)
client.connect(iot_hub, 1883, 60)
print("Connection success")


DEBUG = 0
CMD_MODE = 2
CMD_QUERY_DATA = 4
CMD_DEVICE_ID = 5
CMD_SLEEP = 6
CMD_FIRMWARE = 7
CMD_WORKING_PERIOD = 8
MODE_ACTIVE = 0
MODE_QUERY = 1

ser = serial.Serial()
ser.port = "/dev/ttyUSB0"
ser.baudrate = 9600

ser.open()
ser.flushInput()

byte, data = 0, ""

firebase = firebase.FirebaseApplication('', None)


def dump(d, prefix=''):
    print(prefix + ' '.join(x.encode('hex') for x in d))

def construct_command(cmd, data=[]):
    assert len(data) <= 12
    data += [0,]*(12-len(data))
    checksum = (sum(data)+cmd-2)%256
    ret = "\xaa\xb4" + chr(cmd)
    ret += ''.join(chr(x) for x in data)
    ret += "\xff\xff" + chr(checksum) + "\xab"

    if DEBUG:
        dump(ret, '> ')
    return ret

def process_data(d):
    r = struct.unpack('<HHxxBB', d[2:])
    pm25 = r[0]/10.0
    pm10 = r[1]/10.0
    checksum = sum(ord(v) for v in d[2:8])%256
    print("PM 2.5: {} μg/m^3  PM 10: {} μg/m^3 CRC={}".format(pm25, pm10, "OK" if (checksum==r[2] and r[3]==0xab) else "NOK"))

    return [pm25, pm10]
    #print("PM 2.5: {} μg/m^3  PM 10: {} μg/m^3 CRC={}".format(pm25, pm10, "OK" if (checksum==r[2] and r[3]==0xab) else "NOK"))

def process_version(d):
    r = struct.unpack('<BBBHBB', d[3:])
    checksum = sum(ord(v) for v in d[2:8])%256
    print("Y: {}, M: {}, D: {}, ID: {}, CRC={}".format(r[0], r[1], r[2], hex(r[3]), "OK" if (checksum==r[4] and r[5]==0xab) else "NOK"))

def read_response():
    byte = 0
    while byte != "\xaa":
        byte = ser.read(size=1)

    d = ser.read(size=9)

    if DEBUG:
        dump(d, '< ')
    return byte + d

def cmd_set_mode(mode=MODE_QUERY):
    ser.write(construct_command(CMD_MODE, [0x1, mode]))
    read_response()

def cmd_query_data():
    ser.write(construct_command(CMD_QUERY_DATA))
    d = read_response()
    values = []
    if d[1] == "\xc0":
        values = process_data(d)
    return values

def cmd_set_sleep(sleep=1):
    mode = 0 if sleep else 1
    ser.write(construct_command(CMD_SLEEP, [0x1, mode]))
    read_response()

def cmd_set_working_period(period):
    ser.write(construct_command(CMD_WORKING_PERIOD, [0x1, period]))
    read_response()

def cmd_firmware_ver():
    ser.write(construct_command(CMD_FIRMWARE))
    d = read_response()
    process_version(d)

def cmd_set_id(id):
    id_h = (id>>8) % 256
    id_l = id % 256
    ser.write(construct_command(CMD_DEVICE_ID, [0]*10+[id_l, id_h]))
    read_response()
    
# Initialise the BMP085 and use STANDARD mode (default value)
# bmp = BMP085(0x77, debug=True)
bmp = BMP085(0x77)
  

if __name__ == "__main__":
    while True:
        cmd_set_sleep(0)
        cmd_set_mode(1);


        for t in range(15):
            values = cmd_query_data()
            pressure = bmp.readPressure()
            altitude = bmp.readAltitude()
            temp = bmp.readTemperature()
            
         
            if values is not None:
                print("PM2.5: ", values[0], ", PM10: ", values[1])
                print ("Pressure:    %.2f hPa" % (pressure/100))
                print ("Temperature: %.2f C" % temp)
                print("Altitude:    %.2f" % altitude)
                time.sleep(2)

        # open stored data
        with open('/var/www/html/aqi.json') as json_data:
            data = json.load(json_data)

        # check if length is more than 100 and delete first element
        if len(data) > 100:
            data.pop(0)

        # append new values
        sensor_data = {'pm25': values[0], 'pm10': values[1],'temperature': temp,'pression':pressure ,'altitude':altitude ,'time': time.strftime("%d.%m.%Y %H:%M:%S")}
        data.append(sensor_data)
        #firebase.post('/sensors', sensor_data)
        response_t = variable_t.save_value({"value": temp })
        response_p = variable_p.save_value({"value": pressure })
        response_altitude = variable_altitude.save_value({"value": altitude })
        response_pm10 = variable_pm10.save_value({"value": values[1] })
        response_pm25 = variable_pm25.save_value({"value": values[0] })


        #client.publish(topic, json.dumps(sensor_data), 1)

        # save it
        with open('/var/www/html/aqi.json', 'w') as outfile:
            json.dump(data, outfile)

        print("Going to sleep for 1 min...")
        cmd_set_mode(0);
        cmd_set_sleep()
        time.sleep(60)
