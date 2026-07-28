import random
from time import sleep
from flask import Flask, render_template, request, jsonify
from gpiozero import LED, TonalBuzzer
from gpiozero.tones import Tone

# Optional: Force software PWM if hardware PWM isn't available on GPIO 8
# from gpiozero.pins.rpigpio import RPiGPIOFactory
# from gpiozero import Device
# Device.pin_factory = RPiGPIOFactory()

app = Flask(__name__)

# Initialize GPIO pins
led1 = LED(15)
led2 = LED(17)
led3 = LED(18)
led4 = LED(23)
led5 = LED(25)
led6 = LED(24)

buzzer = TonalBuzzer(8)

# Tempo and Timing (seconds)
tempo = 100
whole_note = (60 * 4) / tempo  # 2.4 seconds

# Musical Tones
C4 = Tone(261.63)
D4 = Tone(293.66)
E4 = Tone(329.63)
F4 = Tone(349.23)
G4 = Tone(392.00)
A4 = Tone(440.00)
B4 = Tone(493.88)

@app.route('/leds')
def leds():
    return render_template('control.html')


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/music')
def music():
    # Extract the JSON data sent by the JavaScript fetch request
    data = request.get_json()
    
    # Grab the specific key value
    pressed_key = data.get('key')
    
    # Print it to your Python console
    print(f"Python received key: {pressed_key}")
    
    # Send a confirmation response back to the browser
    return jsonify({"status": "success", "received": pressed_key}), 200
    return render_template('music.html')

@app.route('/control', methods=['POST'])
def control():
    led = request.form.get('led')
    action = request.form.get('action')

    # Handle "blink all" routine
    if led == 'blink all':
        for target in [led1, led2, led3, led4, led5, led6]:
            target.on()
        sleep(0.1)
        for target in [led1, led2, led3, led4, led5, led6]:
            target.off()
        return render_template('index.html')

    # Handle buzzer melody routine
    elif led == 'buzzer':
        if action == 'sound':
            buzzer.play(D4)
            sleep(1)
            buzzer.pause()

            buzzer.play(A4)
            sleep(0.5)
            buzzer.pause()

            buzzer.play(F4)
            sleep(1)
            buzzer.pause()
        if action == 'off':
            while action == 'sound':
               buzzer.stop()
               sleep(0.1)
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
        return "Invalid LED selection", 400

    # Execute individual action
    if action == 'on':
        target.on()
    elif action == 'off':
        target.off()
    elif action == 'blink':
        target.on()
        sleep(0.5)
        target.off()
    return render_template('index.html')





if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
