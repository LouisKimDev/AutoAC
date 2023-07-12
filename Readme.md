https://github.com/LouisKimDev/AutoAC

- master.py
    - 라즈베리파이의 GPIO 라이브러리 이용
    - 서보모터 stop시 떨림현상
        - GPIO를 IN으로 설정해서 해결
    
    - 3시간마다 4분 대기하고 메인 전원을 켠다
        - Time함수로 현재 시간 받는다
    - 30분을 기다린뒤 test모드를 켠다
        - 중복을 막기위해 매 30분 마다 20초씩 누적해서 대기한다


- test.py
    - pigpio 라이브러리 이용
    - 서보모터 Idle시 안정적
    - 함수 각도 테스트 필요


