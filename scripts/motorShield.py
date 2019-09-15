from MotorShield import MotorShield

# Globals
shield

# Methods
def setup():
    shield = MotorShield()

def strikeGong():
    shield.powerSteps(50)
    shield.release()
