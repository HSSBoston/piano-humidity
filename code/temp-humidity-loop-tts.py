import RPi.GPIO as GPIO, kintone, time, os, sys
from kintone import getCurrentTimeStamp
from Adafruit_DHT import AM2302, read_retry as readTempHumidity
GPIO.setmode(GPIO.BCM)
# Start writing your program below

tempSensorPin = 21
interval = 5

while True:
    try:
        humidity, temp = readTempHumidity(AM2302, tempSensorPin)

        if humidity is not None and temp is not None:
            print(getCurrentTimeStamp(), end=" ")
            print("Temp: " + str(temp), end=" ")
            print("Humidity: " + str(humidity))
            
            if humidity < 40:
                command1 = "vlc -I dummy 'http://translate.google.com/translate_tts?ie=UTF-8&client=tw-ob&tl=en&q=Humidity+is+low.+You+may+wanna+turn+on+a+humidifier.' --play-and-exit"
                command2 = "vlc -I dummy 'http://translate.google.com/translate_tts?ie=UTF-8&client=tw-ob&tl=ja&q=湿度が高くなっています。加湿器を使って下さい&tl=ja' --play-and-exit"
                os.system(command1)
                os.system(command2)
        else:
            print("Failed to get sensor reading")
        time.sleep(interval)
    
    except KeyboardInterrupt:
        break

# Write your program above this line
#GPIO.cleanup()
