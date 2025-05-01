from machine import Pin
import time 
_init()
 
LedPin_red = 16
LedPin_green = 0
 
led_red = Pin(LedPin_red, Pin.OUT)
led_green = Pin(LedPin_green, Pin.OUT)
 
while True:
    led_red.off()
    led_green.off()
    time.sleep(2)
    led_red.on()
    time.sleep(2)
    led_green.on()

