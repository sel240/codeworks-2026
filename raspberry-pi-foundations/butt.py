from gpiozero import Button
import random

button = Button(2)

button.wait_for_press()
print(random.randint(1, 9000))
print('Hello There')
