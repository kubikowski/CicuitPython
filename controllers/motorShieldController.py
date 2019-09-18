from MotorShield import MotorShield
from adafruit_motor import stepper
import time

# Setup
shield = MotorShield()

# Methods
def strikeGong():
    shield.steps(200, style=stepper.MICROSTEP)
    time.sleep(0.1)
    shield.steps(75, style=stepper.DOUBLE, direction=stepper.BACKWARD)
    time.sleep(0.1)
    shield.steps(75, style=stepper.DOUBLE)
    time.sleep(0.1)
    shield.steps(200, style=stepper.MICROSTEP, direction=stepper.BACKWARD)
    shield.release()
