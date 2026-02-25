This is how to create a flask web app with some preset code which can run the sensors, a message, an image which flips horizontally and code which some images will show when you move the joystick.
To run the webapp and the code, first you need raspberry pi sensehat or buy one. You can get one here:
  https://www.raspberrypi.com/products/sense-hat/
Then you have to install the libraries:
Use this code:
  sudo apt-get update
  sudo apt-get upgrade
  sudo apt-get install sense-hat
  sudo apt install python3-flask
Then install all the code by using the command:
  git clone https://github.com/Thecodeguyrandom/Flask-Webapp-for-the-raspberry-pi-4b
  mv Flask-Webapp-for-the-raspberry-pi-4b/ Webapp
  cd Webapp
Then to start hosting the webapp run:
  python3 app.py
Then to see the app, click the link the terminal posts.
