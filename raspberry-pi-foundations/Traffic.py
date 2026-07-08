from gpiozero import LED
from time import sleep

# Pin definitions
bluelight = 17
yellowlight = 27
greenlight = 22

# Setup LED objects
blue = LED(bluelight)
yellow = LED(yellowlight)
green = LED(greenlight)

def loop():
    # Blue ON, others OFF
    blue.on()
    yellow.off()
    green.off()
    sleep(1.0)

    # Green ON, others OFF
    blue.off()
    yellow.off()
    green.on()
    sleep(0.7)

    # Yellow ON, others OFF
    blue.off()
    yellow.on()
    green.off()
    sleep(0.3)

if __name__ == "__main__":
    try:
        while True:
            loop()
    except KeyboardInterrupt:
        # Turn everything off on exit
        blue.off()
        yellow.off()
        green.off()
