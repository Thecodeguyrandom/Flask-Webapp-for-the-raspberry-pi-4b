from sense_hat import SenseHat
from time import sleep

sense = SenseHat()

w = (150, 150, 150)
b = (0, 0, 255)
e = (0, 0, 0)
r = (255, 0, 0)

image = [
w,w,w,e,e,w,w,w,
w,w,b,e,e,w,w,b,
w,w,w,e,e,w,w,w,
e,r,e,e,e,r,e,e,
e,e,r,e,e,e,r,e,
w,w,w,e,e,w,w,w,
b,w,w,e,e,b,w,w,
w,w,w,e,e,w,w,w,
]

sense.set_pixels(image)

while True:
    sleep(1)
    sense.flip_h()