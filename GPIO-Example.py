import Rpi.GPIO as GPIO
GPIO.setup(18, GPIO.OUT)
GPIO.setup(11, GPIO.IN)
while True:
	if GPIO.input(11):
		GPIO.output(18, True)
	else:
		GPIO.output(18, False)