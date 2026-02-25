from flask import Flask, render_template, request
import subprocess
import os

app = Flask(__name__)

def hex_to_rgb(hex):
    hex = hex.lstrip('#')
    return tuple(int(hex[i:i+2], 16) for i in (0, 2, 4))

def killall():
    os.system('pkill -f joystick.py')
    os.system('pkill -f sensors.py')
    os.system('pkill -f flipping_images.py')
    os.system('pkill -f messages.py')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/sensors', methods=['POST'])
def sensors():
    killall()
    subprocess.Popen(['sudo', 'nice', '-n', '-20', 'python3', 'sensors.py'])
    return render_template('index.html', message='Sensors Running')

@app.route('/joystick', methods=['POST'])
def joystick():
    killall()
    subprocess.Popen(['python3', 'joystick.py'])
    return render_template('index.html', message='Joystick Running')

@app.route('/images', methods=['POST'])
def images():
    killall()
    subprocess.Popen(['python3', 'flipping_images.py'])
    return render_template('index.html', message='Images Running')

@app.route('/messages', methods=['POST'])
def messages():
    killall()
    message = request.form['message']
    color = request.form['color']
    back_colour = request.form['back_colour']
    scrollspeed = float(request.form['scrollspeed'])
    
    if scrollspeed < 0.1:
        return "Invalid Scroll speed number, please enter a number which is 0.1 or higher", 400
    scrollspeed = str(scrollspeed)
    
    color = hex_to_rgb(color)
    back_colour = hex_to_rgb(back_colour)
    
    color = ','.join(map(str, color))
    back_colour = ','.join(map(str, back_colour))
    
    subprocess.Popen(['sudo', 'nice', '-n',  '-20', 'python3', 'messages.py', message, color, back_colour, scrollspeed])
    return render_template('index.html', message='messages Running')

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True,  host='0.0.0.0')
