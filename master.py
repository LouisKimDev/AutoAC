import RPi.GPIO as GPIO
import time

'''
duty clycle (degree)
10    :   160
7.5   :   120
5     :    80
2.5   :    40
'''

class motorz:
    def __init__(self):
        self.SERVO_1 = 18
        self.SERVO_2 = 23
        self.MOVE_TIME = 0.3
        self.COUNT = 1

        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.SERVO_1, GPIO.OUT)
        GPIO.setup(self.SERVO_2, GPIO.OUT)
        self.pwm1 = GPIO.PWM(self.SERVO_1, 50)
        self.pwm2 = GPIO.PWM(self.SERVO_2, 50)
        self.pwm1.start(0)
        self.pwm2.start(0)
        GPIO.setwarnings(False)


    def Servo1Routine(self, iterations):
        GPIO.setup(self.SERVO_1, GPIO.OUT)
        for i in range(iterations):
            self.pwm1.ChangeDutyCycle(7.5)
            time.sleep(self.MOVE_TIME)
            self.pwm1.ChangeDutyCycle(10)
            time.sleep(self.MOVE_TIME)

        self.pwm1.ChangeDutyCycle(7.5)
        time.sleep(self.MOVE_TIME)
        GPIO.setup(self.SERVO_1, GPIO.IN)
        print(f'servo1 activated for {iterations} times')


    def Servo2Routine(self, iterations):
        for i in range(iterations):
            GPIO.setup(self.SERVO_2, GPIO.OUT)
            self.pwm2.ChangeDutyCycle(7.5)
            time.sleep(self.MOVE_TIME)
            self.pwm2.ChangeDutyCycle(10)
            time.sleep(self.MOVE_TIME)
            
        self.pwm2.ChangeDutyCycle(7.5)
        time.sleep(self.MOVE_TIME)
        GPIO.setup(self.SERVO_2, GPIO.IN)
        print(f'servo2 activated for {iterations} times')


    def PrintTime(self):
        print(time.strftime('%H:%M:%S'))


    def test(self):
        try:
            while True:
                if time.localtime().tm_sec % 1 == 0:
                    print('test routine start')

                    self.Servo1Routine(1)
                    self.Servo2Routine(4)

                    print('test routine ended')

        except KeyboardInterrupt:
            self.pwm1.stop()
            self.pwm2.stop()
            print('End')
            GPIO.cleanup()


    def main(self):
        try:
            while True:
                if ((time.localtime().tm_hour % 3 == 0) and (time.localtime().tm_min == 0)) :

                    time.sleep(240)

                    self.PrintTime()
                    self.Servo1Routine(1) # 00:04:00
                    self.Servo2Routine(4)
                    time.sleep(1820)

                    self.PrintTime()
                    self.Servo2Routine(4) # 00:34:20
                    time.sleep(1840)

                    self.PrintTime()
                    self.Servo2Routine(4) # 01:05:00
                    time.sleep(1860)

                    self.PrintTime()
                    self.Servo2Routine(4) # 01:36:00
                    time.sleep(1880)

                    self.PrintTime()
                    self.Servo2Routine(4) # 02:07:20
                    time.sleep(1900)

                    self.PrintTime()
                    self.Servo2Routine(4) # 02:39:00

        except KeyboardInterrupt:
            self.pwm1.stop()
            self.pwm2.stop()
            print('End')
            GPIO.cleanup()



if __name__ == "__main__":
    a = motorz()
    a.main()
else:
    print('Excution Failed')