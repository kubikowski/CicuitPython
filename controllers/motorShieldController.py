from MotorShield import MotorShield
from adafruit_motor import stepper
import time

# Setup
shield = MotorShield()

# Methods
def strikeGong():
    shield.step(200, style=stepper.MICROSTEP)
    time.sleep(0.1)
    shield.step(75, style=stepper.DOUBLE, direction=stepper.BACKWARD)
    time.sleep(0.1)
    shield.step(75, style=stepper.DOUBLE)
    time.sleep(0.1)
    shield.step(200, style=stepper.MICROSTEP, direction=stepper.BACKWARD)
    shield.release()
