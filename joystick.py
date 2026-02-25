from sense_hat import SenseHat
from time import sleep

sense = SenseHat()

def red():
    sense.clear(255, 0, 0)

def blue():
    sense.clear(0, 0, 255)
    
def green():
    sense.clear(0, 255, 0)
    
def yellow():
    sense.clear(255, 255, 0)

def clear():
    sense.clear()

while True:
    for event in sense.stick.get_events():
        if event.action == 'held':
            red()
            sleep(1)
            yellow()
            sleep(1)
            blue()
            sleep(1)
            green()
            sleep(1)
            clear()
            break
        elif event.direction == 'up':
            red()
        elif event.direction == 'down':
            yellow()
        elif event.direction == 'left':
            blue()
        elif event.direction == 'right':
            green()
        elif event.direction == 'middle':
            clear()