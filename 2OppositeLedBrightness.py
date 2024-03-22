from machine import Pin, PWM
from time import sleep

frequency = 5000
led1 = PWM(Pin(5), frequency)
led2 = PWM(Pin(4), frequency)

while True:
    for duty_cycle in range(0, 1024, 1):
        led1.duty(duty_cycle)
        led2.duty(1023 - duty_cycle) 
        print("led 1's DC ", duty_cycle)
        print("led 2's DC ", 1023 - duty_cycle)
        sleep(0.009)
    
    for duty_cycle in range(1023, 0, -1):
        led1.duty(duty_cycle)          
        led2.duty(1023 - duty_cycle)
        print("led 1's DC ", duty_cycle)
        print("led 2's DC ", 1023 - duty_cycle)
        sleep(0.009)
