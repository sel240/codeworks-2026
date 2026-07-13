from gpiozero import LED
from time import sleep

# Pin definitions
greenlight = 15
yellowlight = 17
redlight = 18

# Setup LED objects
blue = LED(redlight)
yellow = LED(yellowlight)
green = LED(greenlight)

def loop():
    # Blue ON, others OFF
    blue.on()
    yellow.off()
    green.off()
    sleep(10)

    # Green ON, others OFF
    blue.off()
    yellow.off()
    green.on()
    sleep(7)

    # Yellow ON, others OFF
    blue.off()
    yellow.on()
    green.off()
    sleep(3.3333333333333333333333333333333333)

if __name__ == "__main__":
    try:
        while True:
            loop()
    except KeyboardInterrupt:
        # Turn everything off on exit
        blue.off()
        yellow.off()
        green.off()
