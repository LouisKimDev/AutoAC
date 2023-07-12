import pigpio
import time

# pigpio 라이브러리를 이용
'''
set_servo_pulsewidth(user_gpio, pulsewidth)

Parameter:
1. user_gpio = 0~31

2. pulsewidth = 0(off), 500(0-degree) ~ 2500(180-degree)
pulsewidth를 500, 2500로 쓰면 서보모터에 데미지 줄 수 있다.
그래서 600 ~ 2400사이 권장
각도 공식
f(x) = 600 + 10x

'''

pi = pigpio.pi()
pi.set_servo_pulsewidth(18, 0) # 18번 채널에연결된 서보모터를 꺼줍니다. 

sleep(1) 

pi.set_servo_pulsewidth(18, 500) # 18번채널에 연결된 서보모터를 0도로 이동

sleep(1)

pi.set_servo_pulsewidth(18, 1500) # 가운데로 이동 90도

sleep(1)

pi.set_servo_pulsewidth(18, 2500) # 180도 끝으로 이동. 

sleep(1)