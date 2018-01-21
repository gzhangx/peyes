import RPi.GPIO as GPIO
import time
GPIO.VERSION
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
ledPin = 29
pin2 = 31
GPIO.setup(ledPin, GPIO.OUT)
GPIO.setup(pin2, GPIO.OUT)
GPIO.output(ledPin, GPIO.HIGH)
GPIO.output(ledPin, GPIO.LOW)

ledSleep = 0.5

try:
  while 1:
    GPIO.output(ledPin, GPIO.HIGH)
    GPIO.output(pin2, GPIO.HIGH)
    time.sleep(ledSleep)
    GPIO.output(ledPin, GPIO.LOW)
    GPIO.output(pin2, GPIO.LOW)
    time.sleep(ledSleep)
except KeyboardInterrupt:
  GPIO.cleanup()
