from flask import Flask, render_template
from gpiozero import LED

app = Flask(__name__)

# Define the three LEDs
try:
    led1 = LED(17)
    led2 = LED(7)
    led3 = LED(22)
    print("--- LEDs Initialized on Pins 17, 7, and 22 ---")
except Exception as e:
    print(f"--- Error Initializing LEDs: {e} ---")

@app.route('/')
def index():
    print("--- User visited the Home Page ---")
    return render_template('index.html')

@app.route('/<int:pin>/<action>')
def control_led(pin, action):
    # This prints to your Terminal so you can see the request
    print(f"--- Debug: Received request for Pin: {pin} | Action: {action} ---")
    
    led_map = {17: led1, 7: led2, 22: led3}
    selected_led = led_map.get(pin)
    
    if selected_led:
        if action == "on":
            selected_led.on()
            return f"<h1>Success!</h1><p>GPIO {pin} is now ON.</p><a href='/'>Back Home</a>"
        elif action == "off":
            selected_led.off()
            return f"<h1>Success!</h1><p>GPIO {pin} is now OFF.</p><a href='/'>Back Home</a>"
        else:
            print(f"--- Debug Error: Action '{action}' is not on or off ---")
            return f"Invalid action: {action}", 400
    
    print(f"--- Debug Error: Pin {pin} not found in led_map ---")
    return f"Pin {pin} is not configured.", 404

if __name__ == '__main__':
    # Start the server
    app.run(host='0.0.0.0', port=5000, debug=True)
