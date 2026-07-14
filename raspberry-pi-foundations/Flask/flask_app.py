from flask import Flask, render_template, request
from gpiozero import LED
from time import sleep

app = Flask(__name__)

led1 = LED(15)
led2 = LED(17)
led3 = LED(18)
led4 = LED(23)
led5 = LED(25)
led6 = LED(24)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/control', methods=['POST'])
def control():
    led = request.form.get('led')
    action = request.form.get('action')

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
    elif led == 'blink all':
        for target in [led6, led5, led4, led3, led2, led1]:
            target.on()
            sleep(0.5)
            target.off()
    else:
        return "Invalid LED"

    if action == 'on':
        target.on()
    elif action == 'off':
        target.off()
    elif action == 'blink': 
        target.on()
        sleep(.5)
        target.off()
        sleep(.5)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

