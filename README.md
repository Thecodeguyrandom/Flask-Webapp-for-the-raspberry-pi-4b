# Flask Webapp for the Raspberry Pi 4B

A Flask web app with preset code that can run the sensors, display a message, show an image which flips horizontally, and display images when you move the joystick.

---

## Requirements

You will need a **Raspberry Pi Sense HAT**. You can get one here:
👉 https://www.raspberrypi.com/products/sense-hat/

---

## Installation

### 1. Install Dependencies

Run the following commands on your Raspberry Pi:

```bash
sudo apt-get update
sudo apt-get upgrade
sudo apt-get install sense-hat
sudo apt install python3-flask
```

### 2. Clone the Repository

```bash
git clone https://github.com/Thecodeguyrandom/Flask-Webapp-for-the-raspberry-pi-4b
mv Flask-Webapp-for-the-raspberry-pi-4b/ Webapp
cd Webapp
```

---

## Running the App

Start the web server with:

```bash
python3 app.py
```

Then to view the app, **click the link** that appears in the terminal.
