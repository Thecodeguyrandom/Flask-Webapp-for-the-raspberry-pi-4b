from sense_hat import SenseHat
import sys

sense = SenseHat()

def show_message(message, color, back_coluor, scrollspeed):
  sense.show_message(message, text_colour=color, back_colour=back_coluor, scroll_speed=scrollspeed)

message = sys.argv[1]
color = tuple(map(int, sys.argv[2].split(',')))
back_coluor = tuple(map(int, sys.argv[3].split(',')))
scrollspeed = float(sys.argv[4])

show_message(message, color, back_coluor, scrollspeed)
sense.clear()