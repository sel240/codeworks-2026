from time import sleep
from flask import Flask, render_template, request, jsonify
from gpiozero import LED, TonalBuzzer
from gpiozero.tones import Tone

app = Flask(__name__)

# Map your exact 6 LEDs (Pins: 15, 17, 18, 23, 25, 24)
leds = {
    '1': LED(15),  # Green
    '2': LED(17),  # Yellow
    '3': LED(18),  # Red
    '4': LED(23),  # White
    '5': LED(25),  # Blue
    '6': LED(24)   # Orange
}

buzzer = TonalBuzzer(8)

# Tempo and Timing
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


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/music', methods=['GET', 'POST'])
def music():
    # Handle incoming JavaScript fetch/POST requests safely
    if request.method == 'POST':
        data = request.get_json() or {}
        pressed_key = data.get('key')
        print(f"Python received key: {pressed_key}")
        return jsonify({"status": "success", "received": pressed_key}), 200

    return render_template('music.html')

    # Play tone on buzzer if key matches
    if pressed_key == 'C':
        buzzer.play(C4)
        sleep(0.2)
        buzzer.stop()
    elif pressed_key == 'D':
        buzzer.play(D4)
        sleep(0.2)
        buzzer.stop()

    return jsonify({"status": "success", "received": pressed_key}), 200

    # GET request: render the music page in browser
    return render_template('music.html')


@app.route('/leds', methods=['GET', 'POST'])
def control():
    # Direct GET requests render the page without triggering LED errors
    if request.method == 'GET':
        return render_template('control.html')

    led = request.form.get('led')
    action = request.form.get('action')

    # 1. Handle "Blink All" routine
    if led == 'blink all':
        for target in leds.values():
            target.on()
        sleep(0.1)
        for target in leds.values():
            target.off()
        return render_template('control.html')

    # 2. Handle group "blink1" (First 3 LEDs: Green, Yellow, Red)
    if led == 'blink1':
        for key in ['1', '2', '3']:
            leds[key].on()
        sleep(0.1)
        for key in ['1', '2', '3']:
            leds[key].off()
        return render_template('control.html')

    if led == 'blink2':
        for key in ['4', '5', '6']:
            leds[key].on()
        sleep(0.1)
        for key in ['4', '5', '6']:
            leds[key].off()
        return render_template('control.html')



    # 3. Handle Buzzer Sequence
    if led == 'buzzer':
        if action == 'sound':
            buzzer.play(D4)
            sleep(0.5)
            buzzer.stop()

            buzzer.play(A4)
            sleep(0.5)
            buzzer.stop()

            buzzer.play(F4)
            sleep(0.5)
            buzzer.stop()
        elif action == 'off':
            buzzer.stop()
        return render_template('index.html')

    # 4. Handle Individual LEDs ('1' through '6')
    if led in leds:
        target = leds[led]
        if action == 'on':
            target.on()
        elif action == 'off':
            target.off()
        elif action == 'blink':
            target.on()
            sleep(0.5)
            target.off()
        return render_template('control.html')

    # Catch-all for unmapped inputs
    return "Invalid LED selection", 400


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
