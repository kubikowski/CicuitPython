from MotorShield import MotorShield

# Setup
shield = MotorShield()

# Methods
def strikeGong(steps):
    shield.powerSteps(steps)
    shield.release()
