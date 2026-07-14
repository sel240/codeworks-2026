from gpiozero import Button, PWMOutputDevice
from time import sleep
import random
import signal  # Used to keep the program running smoothly

# Initialize components
buzzer = PWMOutputDevice(8, frequency=500)
button = Button(2)

def handle_button_press():
    """This function runs every time the button is pressed."""
    print("\n--- Button Pressed! ---")
    print(f"Random Number: {random.randint(1, 9000)}")
    print('Hello There')
    
    # Sound the buzzer (2 beeps: 1s on, 0.5s off)
    for _ in range(2):
        buzzer.value = 0.5  
        sleep(1)            
        buzzer.off()        
        sleep(0.5)

# Assign the function to the button's press event
button.when_pressed = handle_button_press

print("System ready. Press the button to trigger... (Press Ctrl+C to exit)")

# Keep the script running forever so it can listen for button events
signal.pause()
