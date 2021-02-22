import pymavlink
import mavgps
import dronekit
import goruntu_isleme_modulu as gim
import cv2
import otopilot


from __future__ import print_function

from dronekit import connect, VehicleMode, LocationGlobalRelative
import gps
import socket
import time
import sys

mavgps.main() #drone'u bilgisayara bağlar


#Set up option parsing to get connection string
import argparse
parser = argparse.ArgumentParser(description='Tracks GPS position of your computer (Linux only).')
parser.add_argument('--connect',
                   help="vehicle connection target string. If not specified, SITL automatically started and used.")
args = parser.parse_args()

connection_string = args.connect
sitl = None

#Start SITL if no connection string specified
if not connection_string:
    import dronekit_sitl
    sitl = dronekit_sitl.start_default()
    connection_string = sitl.connection_string()




# Connect to the Vehicle
print('Connecting to vehicle on: %s' % connection_string)
vehicle = connect(connection_string, wait_ready=True, timeout=300)

set_altitude = 100                               #çıkılacak yüksekliği yarlar. ben 100 metre yazdım

otopilot.arm_and_takeoff(set_altitude)            #drone kalkış yapar

print("Set default/target airspeed to 3")       #drone hızı ayarlanır
vehicle.airspeed = 3

otopilot.condition_yaw(0,relative=False)            #drone referans yaw açısı ayarlanır
otopilot.set_roi(location)                           #dronu'un lokasyonu belirlenir

targetX , targetY = gim.gettargetx_y()    #hedefi görüntü işleme ile tarar ve merkez noktlarını verir.


x = otopilot.get_location_metres(location,targetX, targetY)
#dronu'un lokasyonu ile görüntü işlemedeki veriler birleiştrilir.
#bu fonksiyon latitude, longtitude ve altitude değerlerine return yapar


print(x)   #çıktı yazdırılır.

