#Juan Ricardo Cortes Morales
#Interfaces programables
#Muestra los digitods del 0-9 utilizando mascara de bits
#Display catodo común
import machine
import time
from machine import Pin, mem32
GPIO_OUT_REG = 0X3FF44004
a = 21
b = 19
c = 18
d = 5
e = 4
f = 2
g = 15

led_a = Pin(a, Pin.OUT)
led_b = Pin(b, Pin.OUT)
led_c = Pin(c, Pin.OUT)
led_d = Pin(d, Pin.OUT)
led_e = Pin(e, Pin.OUT)
led_f = Pin(f, Pin.OUT)
led_g = Pin(g, Pin.OUT)

mem32[GPIO_OUT_REG] = (1 << a) | (1 << b) | (1 << c) | (1 << d) | (1 << e) | (1 << f) | (1 << g)

mem32[GPIO_OUT_REG] ^=  (1 << g) #0
time.sleep(1)
while True:
            
    mem32[GPIO_OUT_REG] ^= (1 << a) | (1 << d) | (1 << e) | (1 << f) #1
    time.sleep(1)
           
    mem32[GPIO_OUT_REG] ^= (1 << a) | (1 << c) | (1 << d) | (1 << e) | (1 << g) #2
    time.sleep(1)
           
    mem32[GPIO_OUT_REG] ^=   (1 << c) | (1 << e) #3
    time.sleep(1)
            
    mem32[GPIO_OUT_REG] ^= (1 << a) | (1 << d) | (1 << f) #4
    time.sleep(1)
            
    mem32[GPIO_OUT_REG] ^= (1 << a) | (1 << b) | (1 << d) #5
    time.sleep(1)
            
    mem32[GPIO_OUT_REG] ^=  (1 << e) #6
    time.sleep(1)
            
    mem32[GPIO_OUT_REG] ^= (1 << b) | (1 << d) | (1 << e) | (1 << f) | (1 << g) #7
    time.sleep(1)
            
    mem32[GPIO_OUT_REG] ^= (1 << d) | (1 << e) | (1 << f) | (1 << g) #8
    time.sleep(1)
    
    mem32[GPIO_OUT_REG] ^=  (1 << d) | (1 << e) #9
    time.sleep(1)
    
    mem32[GPIO_OUT_REG] ^=  (1 << d) | (1 << e) | (1 << g) #0
    time.sleep(1)


 

