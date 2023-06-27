import RPi.GPIO as GPIO
import time

servo_1 = 18
servo_2 = 23
move_time = 0.5

GPIO.setmode(GPIO.BCM)
GPIO.setup(servo_1, GPIO.OUT)
GPIO.setup(servo_2, GPIO.OUT)

pwm1 = GPIO.PWM(servo_1, 50)
pwm2 = GPIO.PWM(servo_2, 50)

pwm1.start(3.0)
pwm2.start(3.0)

GPIO.setwarnings(False)

def Servo1Routine(iterations):
	for i in range(iterations):
		pwm1.ChangeDutyCycle(3)
		time.sleep(move_time)
		pwm1.ChangeDutyCycle(12.5)
		time.sleep(move_time)
	pwm1.ChangeDutyCycle(3)
	time.sleep(move_time)
	print(f'servo1 activated for {iterations} times')


def Servo2Routine(iterations):
	for i in range(iterations):
		pwm2.ChangeDutyCycle(3)
		time.sleep(move_time)
		pwm2.ChangeDutyCycle(12.5)
		time.sleep(move_time)
	pwm2.ChangeDutyCycle(3)
	time.sleep(move_time)
	print(f'servo2 activated for {iterations} times')


def PrintTime():
	print(time.strftime('%H:%M:%S'))



try:
	while True:
		if(time.localtime().tm_hour % 3 == 0) and \
			time.localtime().tm_min == 0 and \
			time.localtime().tm_sec == 0:

			PrintTime()
			time.sleep(5)
			Servo1Routine(1)
			Servo2Routine(4)

			print('3hr routine ended')


		elif time.localtime().tm_min % 30 == 0 and \
			time.localtime().tm_sec == 0:

			PrintTime()
			time.sleep(5)
			Servo2Routine(4)

			print('30min routine ended')


		elif time.localtime().tm_min % 13 == 0 and \
			time.localtime().tm_sec == 0:
			print(time.strftime('%H:%M:%S'))
			time.sleep(5)


		else:
			pwm1.stop()
			pwm2.stop()


except KeyboardInterrupt:
	pwm1.stop()
	pwm2.stop()
	print('End')
	GPIO.cleanup()
