from sense_hat import SenseHat

sense = SenseHat()

from time import sleep

p = sense.get_pressure()
t = sense.get_temperature()
h = sense.get_humidity()
    
r = (255, 0, 0)
g = (0, 255, 0)
    
if t > 18  and t < 21:
    bg = g
else:
    bg = r
    
if p >979 and p < 1027:
    bg1 = g
else:
    bg1 = r
if h > 20 and h < 50:
    bg2 = g
else:
    bg2 = r
    
t = str(round(t, 1))
p = str(round(p, 1))
h = str(round(h, 1))
    
color = (0, 0, 255)
    
print(t)
sense.show_message("Tempreature =" + "   " + t , scroll_speed = 0.1, back_colour = bg, text_colour = color)
sleep(1)
print(p)
sense.show_message("Preasure =" + "   " + p , scroll_speed = 0.1, back_colour = bg1, text_colour = color)
sleep(1)
print(h)
sense.show_message("Humidity =" + "   " + h , scroll_speed = 0.1, back_colour = bg2, text_colour = color)
sense.clear()