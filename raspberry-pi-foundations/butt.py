from gpiozero import Button, TonalBuzzer
from gpiozero.tones import Tone
from time import sleep
import random
import signal  # Used to keep the program running smoothly

# Initialize components
buzzer = TonalBuzzer(8)
button = Button(2)

def play_rickroll():
    """Plays the opening melody of 'Never Gonna Give You Up'"""
    # Notes array: (Note name, duration in seconds)
    melody = [
        ("D5", 0.15), ("E5", 0.15), ("A4", 0.15), ("E5", 0.15), ("F#5", 0.3),
        (None, 0.15),
        ("A5", 0.1), ("F#5", 0.15), ("E5", 0.3),
        (None, 0.15),
        ("D5", 0.15), ("E5", 0.15), ("A4", 0.15), ("D5", 0.15), ("E5", 0.3),
        (None, 0.15),
        ("C#5", 0.15), ("A4", 0.15), ("B4", 0.15), ("A4", 0.3)
    ]
    
    for note, duration in melody:
        if note is None:
            buzzer.off()
        else:
            # Fix: Use the built-in .play() method with a Tone object
            buzzer.play(Tone(note))
        sleep(duration)
        
    # Turn off the buzzer completely at the end of the song
    buzzer.off()

def handle_button_press():
    """This function runs every time the button is pressed."""
    print("\n--- Button Pressed! ---")
    print(f"Random Number: {random.randint(1, 9000)}")
    print('Hello There')
    
    # Trigger the Rickroll music function
    play_rickroll()

# Assign the function to the button's press event
button.when_pressed = handle_button_press

print("System ready. Press the button to trigger a Rickroll! (Press Ctrl+C to exit)")

# Keep the script running forever so it can listen for button events
signal.pause()
