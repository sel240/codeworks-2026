from time import sleep
from flask import Flask, render_template, request, jsonify
from gpiozero import LED, TonalBuzzer, Button
from gpiozero.tones import Tone

app = Flask(__name__)

#We  fire the whole bullet!! Thats 65% more bullet
leds = {
    '1': LED(15),  # Green
    '2': LED(17),  # Yellow
    '3': LED(18),  # Red
    '4': LED(23),  # White
    '5': LED(25),  # Blue
    '6': LED(24),  # Orange
    '7': LED(22),   # Green
    '8': LED(3)    # Blue
}

# Piezo / Buzzer connected to GPIO 2
buzzer = TonalBuzzer(2)

# Musical Tones
C4 = Tone(261.63)
D4 = Tone(293.66)
E4 = Tone(329.63)
F4 = Tone(349.23)
G4 = Tone(392.00)
A4 = Tone(440.00)
B4 = Tone(493.88)
C5 = Tone(261.63 * 2)

# Key Mapping maps keypresses to LED object + Tone object
KEY_MAPPING = {
    'S': (leds['1'], C4),
    'D': (leds['2'], D4),
    'F': (leds['3'], E4),
    'G': (leds['4'], F4),
    'H': (leds['5'], G4),
    'J': (leds['6'], A4),
    'K': (leds['7'], B4),
    'L': (leds['8'], C5)
}

# Optional Physical Hardware Button on GPIO 10
try:
    button = Button(10)

    # Callback function for physical button press
    def on_physical_button_press():
        print("pressed")
        buzzer.play(C4)
        sleep(0.5)
        buzzer.stop()

        buzzer.play(G4)
        sleep(0.3)
        buzzer.stop()

        buzzer.play(F4)
        sleep(0.4)
        buzzer.stop()

        buzzer.play(C4)
        sleep(0.4)
        buzzer.stop()

        buzzer.play(E4)
        sleep(0.35)
        buzzer.stop()

        buzzer.play(C4)
        sleep(0.3)
        buzzer.stop()

        buzzer.play(E4)
        sleep(0.4)
        buzzer.stop()

        buzzer.play(F4)
        sleep(0.5)
        buzzer.stop()


    button.when_pressed = on_physical_button_press
except Exception as e:
    print(f"Button initialization note: {e}")


@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')

@app.route('/music', methods=['GET', 'POST'])
def music():
    if request.method == 'POST':
        data = request.get_json() or {}
        pressed_key = data.get('key', '').upper()

        print(f"Python received key: {pressed_key}")

        if pressed_key in KEY_MAPPING:
            led_target, tone_target = KEY_MAPPING[pressed_key]

            # Light up the LED and play tone
            led_target.on()
            buzzer.play(tone_target)

            # Keep active briefly for short keypress feel
            sleep(0.1)

            # Turn off LED and stop tone
            buzzer.stop()
            led_target.off()

            return jsonify({"status": "success", "played": pressed_key}), 200
        else:
            return jsonify({"status": "ignored", "reason": "unmapped key"}), 400

    # GET Request: Render the keyboard page
    return render_template('music.html')

@app.route('/control', methods=['GET', 'POST'])
def control():
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

    return "Invalid LED selection", 400


if __name__ == '__main__':
#    app.run(host='0.0.0.0', port=8080)
    app.run(host='0.0.0.0', port=8180)
