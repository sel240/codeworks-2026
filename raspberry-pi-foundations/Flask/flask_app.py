from flask import Flask, render_template, request
from gpiozero import LED, TonalBuzzer
from time import sleep
from gpiozero.tones import Tone
import random

app = Flask(__name__)

# Initialize GPIO pins
led1 = LED(15)
led2 = LED(17)
led3 = LED(18)
led4 = LED(23)
led5 = LED(25)
led6 = LED(24)

buzzer = TonalBuzzer(8)
tempo = 100
whole_note = (6000 * 4) / tempo

# Tones
C4 = Tone(261.63)
D4 = Tone(293.66)
E4 = Tone(329.63)
F4 = Tone(349.23)
G4 = Tone(392.00)
A4 = Tone(440.00)
B4 = Tone(493.88)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/control', methods=['POST'])
def control():
    led = request.form.get('led')
    action = request.form.get('action')

    # Handle the "blink all" routine completely and exit early
    if led == 'blink all':
        for target in [led1, led2, led3, led4, led5, led6]:
            target.on()
            sleep(0.1)
            target.off()
        return render_template('index.html')
    elif led == 'buzzer':
        buzzer.play(D4)
        sleep(1)
        buzzer.stop()
        buzzer.play(A4)
        sleep(.5)
        buzzer.stop()
        buzzer.play(F4)
        sleep(1)
        buzzer.stop()
        return render_template('index.html')

    # Map individual LEDs
    if led == '1':
        target = led1
    elif led == '2':
        target = led2
    elif led == '3':
        target = led3
    elif led == '4':
        target = led4
    elif led == '5':
        target = led5
    elif led == '6':
        target = led6
    else:
        return "Invalid LED", 400

    # Execute individual action
    if action == 'on':
        target.on()
    elif action == 'off':
        target.off()
        buzzer.stop()
    elif action == 'blink': 
        target.on()
        sleep(0.5)
        target.off()
    elif action == 'sound':
        buzzer.play(C4)

    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
