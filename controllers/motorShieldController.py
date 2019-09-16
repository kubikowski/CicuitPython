from MotorShield import MotorShield
from adafruit_motor import stepper

# Setup
shield = MotorShield()

# Methods
def strikeGong():
    shield.steps(300, style=stepper.MICROSTEP)
    shield.release()
