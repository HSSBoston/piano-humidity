import RPi.GPIO as GPIO, kintone, time, sys
from kintone import getCurrentTimeStamp
from Adafruit_DHT import AM2302, read_retry as readTempHumidity
GPIO.setmode(GPIO.BCM)
# Start writing your program below

tempSensorPin = 21

humidity, temp = readTempHumidity(AM2302, tempSensorPin)

if humidity is not None and temp is not None:
    print(getCurrentTimeStamp(), end=" ")
    print("Temp: " + str(temp), end=" ")
    print("Humidity: " + str(humidity))
else:
    print("Failed to get sensor reading")

# Write your program above this line
#GPIO.cleanup()
