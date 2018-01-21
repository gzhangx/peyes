import RPi.GPIO as GPIO
import time
GPIO.VERSION
GPIO.setmode(GPIO.BOARD)
#GPIO.setwarnings(False)
ledPin = 29
GPIO.setup(ledPin, GPIO.OUT)
GPIO.output(ledPin, GPIO.HIGH)
GPIO.output(ledPin, GPIO.LOW)

ledSleep = 0.5

try:
  while 1:
    GPIO.output(ledPin, GPIO.HIGH)
    time.sleep(ledSleep)
    GPIO.output(ledPin, GPIO.LOW)
    time.sleep(ledSleep)
except KeyboardInterrupt:
  GPIO.cleanup()
