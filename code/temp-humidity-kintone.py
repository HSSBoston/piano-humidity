import RPi.GPIO as GPIO, kintone, time, sys
from kintone import getCurrentTimeStamp
from Adafruit_DHT import AM2302, read_retry as readTempHumidity
GPIO.setmode(GPIO.BCM)
# Start writing your program below

#sdomain = "SUB-DOMAIN-NAME"
#appId = "APP-ID-NUMBER"
#token = "APP-TOKEN"

sdomain = "jxsboston"
appId = "5"
token = ""

tempSensorPin = 21
interval = 900

while True:
    try:
        humidity, temp = readTempHumidity(AM2302, tempSensorPin)

        if humidity is not None and temp is not None:
            print(getCurrentTimeStamp(), end=" ")
            print("Temp: " + str(temp), end=" ")
            print("Humidity: " + str(humidity))

            payload = {"app": appId,
                       "record": {"tempC": {"value": temp},
                                  "humidity": {"value": humidity} }}

            recordId = kintone.uploadRecord(subDomain=sdomain,
                                            apiToken=token,
                                            record=payload)
            if recordId is None:
                sys.exit()        
        else:
            print("Failed to get sensor reading")
        time.sleep(interval)
    
    except KeyboardInterrupt:
        break

# Write your program above this line
#GPIO.cleanup()
