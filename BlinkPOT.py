from machine import Pin, ADC
import time

led_pin = Pin(4, Pin.OUT)
pot_pin = ADC(34)


while True:
    pot_value = pot_pin.read()
    toggling_rate = int((pot_value / 4095) * 900 + 100)
    led_pin.value(not led_pin.value())
    print("Toggle Rate :" ,toggling_rate)
    time.sleep_ms(toggling_rate)
